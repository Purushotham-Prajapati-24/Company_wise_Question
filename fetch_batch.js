const fs = require('fs');
const path = require('path');
const https = require('https');

const datasetPath = path.join(__dirname, 'company_questions_dataset.json');
const dataset = JSON.parse(fs.readFileSync(datasetPath, 'utf-8'));

const outPath = path.join(__dirname, 'batch1_context.txt');
let outContent = "";

// We'll take the first company: Google
const company = Object.keys(dataset)[0];
const questions = dataset[company].slice(0, 10);

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
            }
        }`;
        
        const data = JSON.stringify({
            query: query,
            variables: { titleSlug }
        });
        
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
    for (const q of questions) {
        // extract slug from link
        // e.g. https://leetcode.com/problems/longest-absolute-file-path/
        const match = q.link.match(/problems\/([^\/]+)/);
        if (!match) continue;
        const slug = match[1];
        
        outContent += `--- Question: ${q.question} (${slug}) ---\n`;
        outContent += `Topic: ${q.topic}, Difficulty: ${q.difficulty}\n`;
        try {
            const resp = await fetchLeetcode(slug);
            if (resp.data && resp.data.question) {
                const {content, exampleTestcases} = resp.data.question;
                // strip HTML nicely for terminal reading
                const stripped = content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
                outContent += `Content:\n${stripped}\n\n`;
                outContent += `Testcases:\n${exampleTestcases}\n\n`;
            } else {
                outContent += `Failed to fetch from GraphQL.\n\n`;
            }
        } catch (e) {
            outContent += `Error: ${e.message}\n\n`;
        }
    }
    fs.writeFileSync(outPath, outContent);
    console.log("Written batch1_context.txt");
})();
