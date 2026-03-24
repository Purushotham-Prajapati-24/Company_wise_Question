const https = require('https');
const fs = require('fs');

const dataset = JSON.parse(fs.readFileSync('company_questions_dataset.json', 'utf8'));
const qs = dataset['Microsoft'] || [];

const results = {};
let idx = 0;

function fetchNext() {
  if (idx >= qs.length) {
    fs.writeFileSync('microsoft_raw_data.json', JSON.stringify(results, null, 2));
    console.log('Finished fetching Microsoft data. Total:', Object.keys(results).length);
    return;
  }
  const q = qs[idx++];
  console.log(`Fetching ${q.questionId}: ${q.question}...`);
  const query = `query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { content difficulty } }`;
  const slug = q.question.toLowerCase().replace(/ /g, '-').replace(/[^-a-z0-9]/g, '');
  const req = https.request('https://leetcode.com/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  }, res => {
    let body = '';
    res.on('data', d => body += d);
    res.on('end', () => {
      try {
        const d = JSON.parse(body);
        results[q.questionId] = { title: q.question, difficulty: q.difficulty, topic: q.topic, content: d.data.question ? d.data.question.content : null };
      } catch(e) { results[q.questionId] = { title: q.question, difficulty: q.difficulty, topic: q.topic, content: null }; }
      setTimeout(fetchNext, 400);
    });
  });
  req.on('error', () => { results[q.questionId] = { title: q.question, difficulty: q.difficulty, topic: q.topic, content: null }; setTimeout(fetchNext, 400); });
  req.write(JSON.stringify({ query, variables: { titleSlug: slug } }));
  req.end();
}
fetchNext();
