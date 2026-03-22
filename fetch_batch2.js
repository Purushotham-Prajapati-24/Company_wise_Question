const fs = require('fs');
const path = require('path');
const https = require('https');

const datasetPath = path.join(__dirname, 'company_questions_dataset.json');
const dataset = JSON.parse(fs.readFileSync(datasetPath, 'utf-8'));

const outPath = path.join(__dirname, 'batch2_context.txt');
let outContent = "";

const company = "Google";
const questions = dataset[company].slice(10, 30); // overfetch to guarantee 4 public

outContent += `Company: ${company}\n\n`;

function fetchLeetcode(titleSlug) {
    return new Promise((resolve, reject) => {
        const query = `
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                content
                exampleTestcases
                isPaidOnly
            }
        }`;
        
        const data = JSON.stringify({ query: query, variables: { titleSlug } });
        
        const options = {
            hostname: 'leetcode.com',
            path: '/graphql',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(data),
                'User-Agent': 'Mozilla/5.0'
            }
        };
        
        const req = https.request(options, res => {
            let body = '';
            res.on('data', chunk => body += chunk);
            res.on('end', () => resolve(JSON.parse(body)));
        });
        
        req.on('error', e => reject(e));
        req.write(data);
        req.end();
    });
}

(async () => {
    let gathered = 0;
    for (const q of questions) {
        if (gathered >= 4) break;
        
        const match = q.link.match(/problems\/([^\/]+)/);
        if (!match) continue;
        const slug = match[1];
        
        try {
            const resp = await fetchLeetcode(slug);
            if (resp.data && resp.data.question && !resp.data.question.isPaidOnly) {
                const {questionId, title, content, exampleTestcases} = resp.data.question;
                
                // Some are interactive or complicated
                if (title === 'Guess the Word') continue;
                
                if (content) {    
                    const stripped = content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
                    outContent += `--- Question: ${title} (${questionId}) ---\n`;
                    outContent += `Topic: ${q.topic}, Difficulty: ${q.difficulty}\n`;
                    outContent += `Content:\n${stripped}\n\n`;
                    outContent += `Testcases:\n${exampleTestcases}\n\n`;
                    gathered++;
                }
            }
        } catch (e) {
            console.error(`Error with ${slug}: ${e.message}`);
        }
    }
    fs.writeFileSync(outPath, outContent);
    console.log(`Fetched 4 public questions into batch2_context.txt`);
})();
