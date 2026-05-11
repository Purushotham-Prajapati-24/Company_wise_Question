# MNC Company-wise Interview Questions Dataset

![Interview Preparation](https://img.shields.io/badge/Prep-MNC_Interview-blue?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-Python_|_C++_|_Java_|_JS_|_C-orange?style=for-the-badge)

A premium, standardized collection of coding interview questions from top Multi-National Corporations (MNCs) like **Google, Microsoft, Amazon, Meta, Adobe**, and more. This repository serves as a robust backend for interview preparation platforms, providing high-quality problem data, test cases, and multi-language support.

## 🚀 Key Features

- **Standardized Data**: Every problem is stored in a consistent JSON format including description, constraints, and metadata.
- **Multi-Language Support**: Each problem comes with ready-to-use boilerplate code for Python, C++, Java, JavaScript, and C.
- **Company Mapping**: Questions are mapped to companies with frequency scores and direct LeetCode links.
- **Rich Descriptions**: Problem statements include formatted HTML for easy rendering in web applications.
- **Extensive Test Cases**: Each problem includes both sample and hidden test cases for robust validation.

## 📁 Project Structure

```text
├── 0-200/, 201-400/, 401-600/ ...  # Standardized JSON problem files
├── 1-500/                          # Python scripts (make_standard_N.py) for generation
├── archive/scripts/                # Maintenance and utility scripts
├── company_questions_dataset.json  # Master mapping: Company -> List of Questions
├── question_id_map.json           # Detailed ID mapping with company frequencies
└── image_verification_report.json # Diagnostic reports for asset integrity
```

---

## 🛠️ How to Generate and Propagate Questions

The project uses a script-driven approach to ensure data consistency across thousands of problems.

### 1. Generating a Standardized Question
New questions are created using the `make_standard_N.py` template system.

1.  **Template Setup**: Navigate to the script directory (e.g., `1-500/`) and create/modify a script for your problem ID.
2.  **Input Data**: Provide the problem details in the `generate_json()` function:
    - `problem_id` & `title`
    - `html_description` (HTML formatted)
    - `test_cases` (JSON array with input/output pairs)
    - `boilerplate` (Starter code for all supported languages)
3.  **Execution**: Run the script to generate the JSON file:
    ```powershell
    python 1-500/make_standard_496.py
    ```
4.  **Output**: The script automatically calculates the output path (e.g., `401-600/496_Next_Greater_Element_I.json`) and creates the directory if it doesn't exist.

### 2. Propagating Questions Company-Wise
Propagation ensures that the newly generated question is correctly indexed under the relevant companies.

#### Workflow for Propagation:
- **Metadata Association**: Each question in `question_id_map.json` contains a `companies` array listing the MNCs that ask that problem.
- **Updating the Master Dataset**: After generating a standardized JSON, the question must be "propagated" to `company_questions_dataset.json`. 
- **The Propagation Logic**:
    1.  Read the `problem_id` from the generated JSON.
    2.  Lookup the problem in `question_id_map.json` to find associated companies.
    3.  For each associated company, add the question summary (ID, Title, Difficulty, Link) to the corresponding list in `company_questions_dataset.json`.
    4.  Update the `frequency_score` to reflect the latest data.

---


## 📈 SEO & Discovery
This dataset is optimized for building interview prep tools. Every question has unique IDs and structured metadata, making it highly searchable and easy to integrate into databases or frontend frameworks.

---

