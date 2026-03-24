const https = require('https');
const fs = require('fs');
const path = require('path');

const outDir = path.join(__dirname, 'companyWiseQuestions', 'Quora');
const files = fs.readdirSync(outDir).filter(f => f.endsWith('.json'));

let badFiles = [];
files.forEach(f => {
  const content = fs.readFileSync(path.join(outDir, f), 'utf8');
  const data = JSON.parse(content);
  if (!data.question_text || data.question_text.length < 50) badFiles.push(f);
});

let idx = 0;

function fetchNext() {
  if (idx >= badFiles.length) {
    console.log('Finished patching Quora data.');
    return;
  }
  const f = badFiles[idx++];
  const p = path.join(outDir, f);
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  
  const idStr = f.split('_')[0];
  let titleStr = f.substring(idStr.length + 1).replace(/.json$/, '').replace(/_/g, '-').replace(/---/g, '-').replace(/--/g, '-');
  
  // Custom overrides for known slugs
  if (idStr === "69") titleStr = "sqrtx";

  let slug = titleStr.toLowerCase().replace(/[^a-z0-9-]/g, '').replace(/-+$/, '');

  console.log(`Fetching ${idStr} (slug: ${slug})...`);
  const query = `query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { content difficulty } }`;
  
  const req = https.request('https://leetcode.com/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  }, res => {
    let body = '';
    res.on('data', d => body += d);
    res.on('end', () => {
      try {
        const d = JSON.parse(body);
        if (d.data && d.data.question && d.data.question.content) {
             data.question_text = d.data.question.content;
             fs.writeFileSync(p, JSON.stringify(data, null, 2));
             console.log(`Patched ${f}`);
        } else {
             console.log(`No content for ${f} (Premium or slug mismatch)`);
        }
      } catch(e) { console.log(`Error parsing for ${f}`); }
      setTimeout(fetchNext, 400);
    });
  });
  req.on('error', () => { console.log(`Req Error for ${f}`); setTimeout(fetchNext, 400); });
  req.write(JSON.stringify({ query, variables: { titleSlug: slug } }));
  req.end();
}

console.log(`Starting patch for ${badFiles.length} files...`);
fetchNext();
