const fs = require('fs');
const path = require('path');

const dataset = JSON.parse(fs.readFileSync('company_questions_dataset.json', 'utf8'));
const qs = dataset['Apple'] || [];
const validIds = new Set(qs.map(q => q.questionId.toString()));

const cDir = 'companyWiseQuestions/Apple';
const files = fs.readdirSync(cDir).filter(f => f.endsWith('.json'));

let removed = 0;
files.forEach(f => {
    const qid = f.split('_')[0];
    if (!validIds.has(qid)) {
        console.log(`Removing extra file: ${f}`);
        fs.unlinkSync(path.join(cDir, f));
        removed++;
    }
});

console.log(`Total extra Apple files removed: ${removed}`);
