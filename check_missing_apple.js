const fs = require('fs');
const path = require('path');

const dataset = JSON.parse(fs.readFileSync('company_questions_dataset.json', 'utf8'));
const qs = dataset['Apple'] || [];
const cDir = 'companyWiseQuestions/Apple';
const existing = fs.readdirSync(cDir).filter(f => f.endsWith('.json'));

const missing = qs.filter(q => !existing.some(f => f.startsWith(q.questionId + '_')));

console.log('Missing Apple Questions:');
missing.forEach(q => console.log(`  ID: ${q.questionId}, Title: ${q.question}`));
