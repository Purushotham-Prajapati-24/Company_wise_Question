const fs = require('fs');
const path = require('path');

const dataset = JSON.parse(fs.readFileSync('company_questions_dataset.json', 'utf8'));
const qs = dataset['Apple'] || [];
const cwqDir = 'companyWiseQuestions';
const cDir = path.join(cwqDir, 'Apple');
if (!fs.existsSync(cDir)) fs.mkdirSync(cDir, { recursive: true });

const allCompanies = fs.readdirSync(cwqDir).filter(c => fs.statSync(path.join(cwqDir, c)).isDirectory() && c !== 'Apple');
const existing = fs.readdirSync(cDir).filter(f => f.endsWith('.json'));

let copied = 0;
qs.forEach(oq => {
  const m = existing.find(f => f.startsWith(oq.questionId + '_'));
  if (m) { copied++; return; }
  let found = false;
  for (const c of allCompanies) {
    const files = fs.readdirSync(path.join(cwqDir, c));
    const cMatch = files.find(f => f.startsWith(oq.questionId + '_') && f.endsWith('.json'));
    if (cMatch) {
      const data = JSON.parse(fs.readFileSync(path.join(cwqDir, c, cMatch)));
      fs.writeFileSync(path.join(cDir, cMatch), JSON.stringify(data, null, 4));
      copied++; found = true; break;
    }
  }
});

const raw = JSON.parse(fs.readFileSync('apple_raw_data.json', 'utf8'));
const files = fs.readdirSync(cDir).filter(f => f.endsWith('.json'));

let patchedIndex = 0, patchedContent = 0, noContent = [];

for (const f of files) {
    const fpath = path.join(cDir, f);
    const data = JSON.parse(fs.readFileSync(fpath, 'utf8'));
    let changed = false;

    // 1. Force companyIndex to 3 (Apple)
    if (data.companyIndex !== 3) { data.companyIndex = 3; changed = true; patchedIndex++; }

    // 2. Inject full LeetCode content with <h3> title
    const qid = f.split('_')[0];
    const r = raw[qid];
    if (r && r.content) {
        data.question_text = `<h3>${qid}. ${r.title}</h3>${r.content}`;
        changed = true;
        patchedContent++;
    } else {
        noContent.push(f);
    }

    if (changed) fs.writeFileSync(fpath, JSON.stringify(data, null, 4));
}

console.log(`Total copied/existing: ${copied} (Expected: ${qs.length})`);
console.log(`companyIndex fixed: ${patchedIndex}`);
console.log(`question_text patched with <h3>: ${patchedContent}`);
console.log(`No HTML content (premium): ${noContent.length}`);
noContent.forEach(f => console.log(' ', f));

if (files.length < qs.length) {
    console.log(`Missing ${qs.length - files.length} files entirely!`);
}
