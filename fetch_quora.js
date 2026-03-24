const https = require('https');
const fs = require('fs');

const missingQuestions = [
  { id: "525", title: "Contiguous Array", topic: "Prefix Sum" },
  { id: "437", title: "Path Sum III", topic: "Recursion" },
  { id: "452", title: "Minimum Number of Arrows to Burst Balloons", topic: "Greedy" },
  { id: "390", title: "Elimination Game", topic: "Math" },
  { id: "717", title: "1-bit and 2-bit Characters", topic: "Array" }
];

const results = {};
let idx = 0;

function fetchNext() {
  if (idx >= missingQuestions.length) {
    fs.writeFileSync('quora_raw_data.json', JSON.stringify(results, null, 2));
    console.log('Finished fetching Quora data. Total:', Object.keys(results).length);
    return;
  }
  const q = missingQuestions[idx++];
  const slug = q.title.toLowerCase().replace(/ \- /g, '-').replace(/ /g, '-').replace(/[^-a-z0-9]/g, '');

  console.log(`Fetching ${q.id}: ${q.title} (slug: ${slug})...`);
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
        results[q.id] = { 
          title: q.title, 
          topic: q.topic, 
          content: d.data && d.data.question ? d.data.question.content : null,
          difficulty: d.data && d.data.question ? d.data.question.difficulty : null
        };
      } catch(e) { results[q.id] = { title: q.title, topic: q.topic, content: null }; }
      setTimeout(fetchNext, 400);
    });
  });
  req.on('error', () => { results[q.id] = { title: q.title, topic: q.topic, content: null }; setTimeout(fetchNext, 400); });
  req.write(JSON.stringify({ query, variables: { titleSlug: slug } }));
  req.end();
}
fetchNext();
