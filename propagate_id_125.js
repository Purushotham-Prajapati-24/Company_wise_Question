const fs = require('fs');
const path = require('path');

const BASE_DIR = 'companyWiseQuestions';
const COMPANY_MAP = {
    "Google": 0, "Microsoft": 1, "Amazon": 2, "Apple": 3, "Meta": 4, "Netflix": 5, "Adobe": 6, "Salesforce": 7, "Uber": 8, "Spotify": 9, "IBM": 10, "Tesla": 11, "Oracle": 12, "JPMorgan Chase": 13, "Goldman Sachs": 14, "Bank of America": 15, "SAP": 16, "Intel": 17, "NVIDIA": 18, "Qualcomm": 19, "Cisco": 20, "Airbnb": 21, "Alibaba": 22, "Atlasssian": 23, "Bloomberg": 24, "Paypal": 25, "Quora": 26, "Twitter": 27, "Visa": 28, "Jane Street": 29, "Samsung": 30, "Morgan Stanley": 31
};

const ID = "125";
const SOURCE_FILE = "companyWiseQuestions/Meta/125_Valid_Palindrome.json";
const TARGET_FILENAME = "125_Valid_Palindrome.json";

function propagate() {
    if (!fs.existsSync(SOURCE_FILE)) {
        console.error(`Source file not found: ${SOURCE_FILE}`);
        return;
    }
    const sourceContent = JSON.parse(fs.readFileSync(SOURCE_FILE, 'utf8'));
    const companies = fs.readdirSync(BASE_DIR).filter(c => fs.statSync(path.join(BASE_DIR, c)).isDirectory());
    
    let count = 0;
    companies.forEach(company => {
        const index = COMPANY_MAP[company];
        if (index !== undefined) {
            const targetPath = path.join(BASE_DIR, company, TARGET_FILENAME);
            const updatedContent = { ...sourceContent, companyIndex: index };
            fs.writeFileSync(targetPath, JSON.stringify(updatedContent, null, 4));
            count++;
        }
    });
    console.log(`Propagated ID ${ID} to ${count} companies.`);
}
propagate();
