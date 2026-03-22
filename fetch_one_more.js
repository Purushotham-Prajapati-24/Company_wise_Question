const fs = require('fs');
const https = require('https');

const datasetPath = 'company_questions_dataset.json';
const dataset = JSON.parse(fs.readFileSync(datasetPath, 'utf-8'));

// Google
const questions = dataset['Google'].slice(10, 15);

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
        const data = JSON.stringify({ query: query, variables: { titleSlug } });
        const options = {
            hostname: 'leetcode.com', path: '/graphql', method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(data), 'User-Agent': 'Mozilla/5.0' }
        };
        const req = https.request(options, res => {
            let body = '';
            res.on('data', chunk => body += chunk);
            res.on('end', () => resolve(JSON.parse(body)));
        });
        req.on('error', e => reject(e)); req.write(data); req.end();
    });
}

(async () => {
    for (const q of questions) {
        const match = q.link.match(/problems\/([^\/]+)/);
        if (!match) continue;
        const slug = match[1];
        
        console.log(`--- Question: ${q.question} (${slug}) ---`);
        const resp = await fetchLeetcode(slug);
        if (resp.data && resp.data.question && resp.data.question.content) {
            const content = resp.data.question.content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
            console.log(`Content: ${content.substring(0, 300)}...`);
            console.log(`Testcases: ${resp.data.question.exampleTestcases}`);
            break; // just need one good one
        }
    }
})();
