const fs = require('fs');
const path = require('node:path');

const dir = 'companyWiseQuestions/Apple';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.json'));

console.log(`Auditing ${files.length} Apple files...`);
let errors = 0;

for (const f of files) {
    const data = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    const issues = [];

    if (data.companyIndex !== 3) issues.push(`companyIndex is ${data.companyIndex}, not 3`);

    const qt = data.question_text || '';
    if (qt.length < 150) issues.push(`question_text too short (${qt.length} chars)`);
    if (!qt.includes('<h3>')) issues.push(`question_text missing <h3> title tag`);
    if (!qt.includes('Example')) issues.push(`question_text missing Example keyword`);

    if (!data.test_cases || data.test_cases.length !== 10) {
        issues.push(`test_cases count is ${data.test_cases ? data.test_cases.length : 0}, not 10`);
    } else {
        for (let i = 7; i < 10; i++) {
            if (data.test_cases[i].is_sample !== false) {
                issues.push(`TC ${i+1} is_sample should be false`);
            }
        }
    }

    if (issues.length > 0) {
        console.log(`[FAIL] ${f}:`);
        issues.forEach(m => console.log(`  - ${m}`));
        errors++;
    }
}

if (errors === 0) {
    console.log(`SUCCESS: All ${files.length} Apple files passed rigorous inspection!`);
} else {
    console.log(`Errors in ${errors} file(s).`);
}
