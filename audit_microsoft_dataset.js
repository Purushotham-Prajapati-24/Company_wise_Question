const fs = require('fs');
const path = require('path');

const dir = 'companyWiseQuestions/Microsoft';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.json'));

console.log(`Auditing ${files.length} Microsoft files...`);
let errors = 0;

for (const f of files) {
    const data = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    const issues = [];

    if (data.companyIndex !== 1) issues.push(`companyIndex is ${data.companyIndex}, not 1`);

    const qt = data.question_text || '';
    if (qt.length < 200) issues.push(`question_text too short (${qt.length} chars)`);
    if (!qt.includes('Example') && !qt.toLowerCase().includes('input')) issues.push(`question_text missing Example/Input keywords`);

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
    console.log(`SUCCESS: All ${files.length} Microsoft files passed rigorous inspection!`);
} else {
    console.log(`Errors in ${errors} file(s).`);
}
