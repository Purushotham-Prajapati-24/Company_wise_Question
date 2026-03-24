const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, 'company_questions_dataset.json');
const dataset = JSON.parse(fs.readFileSync(datasetPath, 'utf8'));
const companies = Object.keys(dataset);
const targetCompany = 'Quora';
const targetIndex = 26; 
const targetQuestions = dataset[targetCompany];

const outDir = path.join(__dirname, 'companyWiseQuestions', targetCompany);
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

let copied = 0;
let missing = [];

for (const q of targetQuestions) {
    const qid = q.questionId;
    let foundPath = null;
    
    // Check if already in target dir
    const existingInTarget = fs.readdirSync(outDir).find(f => f.split('_')[0] === qid);
    if (existingInTarget) {
        copied++;
        continue;
    }

    for (const company of companies) {
        if (company === targetCompany) continue;
        const compDir = path.join(__dirname, 'companyWiseQuestions', company);
        if (fs.existsSync(compDir)) {
            const files = fs.readdirSync(compDir);
            for(const f of files) {
                if (f.split('_')[0] === qid) {
                    foundPath = path.join(compDir, f);
                    break;
                }
            }
        }
        if (foundPath) break;
    }
    
    if (foundPath) {
        const fileData = JSON.parse(fs.readFileSync(foundPath, 'utf8'));
        fileData.companyIndex = targetIndex;
        // Clean up filename to match Quora's title if possible, else keep original
        const cleanName = `${qid}_${q.question.replace(/[^a-zA-Z0-9-]/g, '_')}.json`;
        fs.writeFileSync(path.join(outDir, cleanName), JSON.stringify(fileData, null, 2));
        copied++;
    } else {
        missing.push(q);
    }
}

console.log(`\nResults: Total ${targetQuestions.length}. Copied ${copied}. Missing ${missing.length}.`);
if (missing.length > 0) {
    console.log("Missing Questions:");
    missing.forEach(m => console.log(`${m.questionId} - ${m.question}`));
}
