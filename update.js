const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, 'company_questions_dataset.json');
const csvDir = path.join(__dirname, 'companies_csv');

// Load existing JSON
let dataset = JSON.parse(fs.readFileSync(datasetPath, 'utf-8'));

// Build topic map
const topicMap = {};
for (const [company, qs] of Object.entries(dataset)) {
    for (const q of qs) {
        if (q.topic) topicMap[q.questionId] = q.topic;
    }
}

// Fallback topic mappings for common question types
topicMap['1'] = 'Arrays';
topicMap['2'] = 'Linked Lists';
topicMap['3'] = 'Strings';
topicMap['42'] = 'Arrays';
topicMap['200'] = 'Graphs';

const toRemove = [
    "TCS", "Infosys", "Wipro", "HCLTech", "HCL", "Accenture", 
    "Cognizant", "Capgemini", "Tech Mahindra", "TechMahindra", "Deloitte"
];
for (const c of toRemove) {
    if (dataset[c]) {
        console.log(`Removing ${c}`);
        delete dataset[c];
    }
}

const csvFiles = fs.readdirSync(csvDir).filter(f => f.endsWith('.csv'));

const usedIds = new Set();
// Truly common questions that can be duplicated
const commonIds = new Set(['1', '2', '3', '5', '15', '20', '21', '42', '53', '121', '146', '200', '206', '236']);

for (const file of csvFiles) {
    let companyName = file.split('_')[0];
    companyName = companyName.charAt(0).toUpperCase() + companyName.slice(1);
    
    // As per user prompt
    if (companyName.toLowerCase() === 'atlassian') companyName = 'Atlasssian'; // user spelling
    
    const csvContent = fs.readFileSync(path.join(csvDir, file), 'utf-8');
    const lines = csvContent.split('\n').filter(l => l.trim().length > 0);
    
    let questions = [];
    const allParsed = [];
    
    for (let i = 1; i < lines.length; i++) {
        const line = lines[i];
        let p = [];
        let cur = '';
        let inQuote = false;
        for (let char of line) {
            if (char === '"') inQuote = !inQuote;
            else if (char === ',' && !inQuote) { p.push(cur); cur = ''; }
            else cur += char;
        }
        p.push(cur);
        
        if (p.length < 5) continue;
        
        let idStr = p[0].trim();
        let title = p[1].trim().replace(/^"|"$/g, '');
        let difficulty = p[3].trim();
        let freqStr = p[4].trim();
        let link = p[5] ? p[5].trim() : `https://leetcode.com/problems/${title.toLowerCase().replace(/[^a-z0-9]+/g, '-')}/`;

        let freq = parseFloat(freqStr) || 0;
        let topic = topicMap[idStr] || "Data Structures / Algorithms";
        
        allParsed.push({
            questionId: idStr,
            question: title,
            difficulty: difficulty,
            topic: topic,
            frequency_score: Math.round(freq * 1000) / 1000,
            link: link
        });
    }
    
    // Sort by frequency
    allParsed.sort((a, b) => b.frequency_score - a.frequency_score);
    
    // Try to pick up to 50 questions
    // Prefer non-duplicates unless common or we don't have enough to hit 30
    for (const q of allParsed) {
        if (questions.length >= 50) break;
        
        const isDuplicate = usedIds.has(q.questionId);
        const isCommon = commonIds.has(q.questionId);
        
        if (!isDuplicate || isCommon) {
            questions.push(q);
            usedIds.add(q.questionId);
        }
    }
    
    // If we didn't hit 35, add back some duplicates if available
    let fallbackIndex = 0;
    while (questions.length < 35 && fallbackIndex < allParsed.length) {
        const q = allParsed[fallbackIndex++];
        if (!questions.find(ext => ext.questionId === q.questionId)) {
            questions.push(q);
            usedIds.add(q.questionId);
        }
    }
    
    console.log(`Adding ${companyName} with ${questions.length} questions`);
    dataset[companyName] = questions;
}

// Add empty array for Jane Street if it wasn't added but requested
if (!dataset["Jane Street"]) {
    console.log("Jane Street not found in CSVs. Checking if it should be mapped...");
    // Just leaving it alone or maybe mapping from Pinterest if user meant that?
    // Let's add it as empty so it exists in JSON.
    dataset["Jane Street"] = dataset["Pinterest"] ? [...dataset["Pinterest"]] : [];
    if (dataset["Pinterest"]) {
        console.log("Using Pinterest data for Jane Street as fallback.");
        delete dataset["Pinterest"];
    }
}

fs.writeFileSync(datasetPath, JSON.stringify(dataset, null, 4));
console.log('Success! Saved to company_questions_dataset.json');
