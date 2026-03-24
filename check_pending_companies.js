const fs = require('fs');
const path = require('path');

const dataset = JSON.parse(fs.readFileSync('company_questions_dataset.json', 'utf8'));
const cwqDir = 'companyWiseQuestions';

const results = [];

for (const company in dataset) {
    const questions = dataset[company];
    const cDir = path.join(cwqDir, company);
    
    if (!fs.existsSync(cDir)) {
        results.push({ company, status: 'Missing Directory', count: 0, target: questions.length });
        continue;
    }

    const files = fs.readdirSync(cDir).filter(f => f.endsWith('.json'));
    let badQt = 0;
    let badTc = 0;

    files.forEach(f => {
        try {
            const data = JSON.parse(fs.readFileSync(path.join(cDir, f), 'utf8'));
            if (!data.question_text || data.question_text.length < 100 || data.question_text.includes('placeholder')) {
                badQt++;
            }
            if (!data.test_cases || data.test_cases.length !== 10) {
                badTc++;
            }
        } catch (e) {
            badQt++;
        }
    });

    if (files.length < questions.length || badQt > 0 || badTc > 0) {
        results.push({ 
            company, 
            status: 'Unfinished', 
            files: files.length, 
            target: questions.length, 
            badQt, 
            badTc 
        });
    } else {
        results.push({ company, status: 'Finished', files: files.length });
    }
}

console.log('--- DATASET STATUS REPORT ---');
results.forEach(r => {
    if (r.status !== 'Finished') {
        process.stdout.write(`${r.status}: ${r.company.padEnd(15)} | Files: ${String(r.files).padStart(2)}/${String(r.target).padStart(2)} | Bad QT: ${String(r.badQt).padStart(2)} | Bad TC: ${String(r.badTc).padStart(2)}\n`);
    }
});
console.log('-----------------------------');
const finished = results.filter(r => r.status === 'Finished').map(r => r.company);
console.log('Finished companies:', finished.join(', '));
