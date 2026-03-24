const fs = require('fs');
const path = require('path');

const outDir = path.join(__dirname, 'companyWiseQuestions', 'Quora');
const files = fs.readdirSync(outDir).filter(f => f.endsWith('.json'));

let badFiles = [];

files.forEach(f => {
  const content = fs.readFileSync(path.join(outDir, f), 'utf8');
  const data = JSON.parse(content);
  let issues = [];

  if (!data.question_text || data.question_text.length < 50) issues.push('short_qt');
  if (data.companyIndex !== 26) issues.push('wrong_index');
  if (!data.test_cases || data.test_cases.length !== 10) issues.push('tc_count_' + (data.test_cases ? data.test_cases.length : 0));
  
  if (issues.length > 0) badFiles.push(`${f} (${issues.join(', ')})`);
});

if (badFiles.length > 0) {
  console.log('BAD FILES:');
  badFiles.forEach(b => console.log(b));
} else {
  console.log(`ALL ${files.length} FILES PASSED STRUCTURAL AUDIT!`);
}
