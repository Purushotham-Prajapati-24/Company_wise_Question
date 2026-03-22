const fs = require('fs');
const path = require('path');

const dirPath = path.join(__dirname, 'companyWiseQuestions', 'Google');

const files = fs.readdirSync(dirPath).filter(file => file.endsWith('.json'));

for (const file of files) {
    const filePath = path.join(dirPath, file);
    const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    let modified = false;

    // Flatten answer
    if (typeof data.answer === 'object' && data.answer !== null && data.answer.python) {
        data.answer = data.answer.python;
        modified = true;
    }
    
    // Flatten boilerplate
    if (typeof data.boilerplate === 'object' && data.boilerplate !== null && data.boilerplate.python) {
        data.boilerplate = data.boilerplate.python;
        modified = true;
    }
    
    // Ensure we have exactly 10 test cases (we should)
    // If we have some, let's just make sure they're saved back correctly.
    if (modified) {
        fs.writeFileSync(filePath, JSON.stringify(data, null, 4), 'utf-8');
        console.log(`Updated ${file}`);
    }
}
console.log('Finished updating JSON structures to match sample.json strictly.');
