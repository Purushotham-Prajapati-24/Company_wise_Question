# Question Strategy Role Model

**Reference Document:** `companyWiseQuestions/Google/939_Minimum_Area_Rectangle.json`

This file serves as the definitive role model for generating High-Quality FAANG coding interview questions in this dataset. It perfectly conforms to the schema layout, extremity limits, and multi-language standard configurations dictated by the project.

## 1. Top-Level Data Structure
Every question MUST contain the following explicit fields matching the JSON schema:
- **`question_text`**: HTML-formatted text including strong tags, lists, and accurate constraints.
- **`difficulty`**: Capitalized string (e.g. "EASY", "MEDIUM", "HARD").
- **`marks`**: Weightage of the question (e.g. 5, 10, 20).
- **`input_format` & `output_format`**: Clear, unambiguous I/O instructions.
- **`constraints`**: Real-world limitations (e.g. `1 <= points.length <= 500`).
- **`explanation`**: A thorough, logical breakdown demonstrating competitive-programming and FAANG-level maturity.
- **`answer`**: The **Python** optimum solution exclusively.
- **`boilerplate`**: A robust 5-language dictionary containing `python`, `cpp`, `java`, `javascript`, and `c` keys with complete standard I/O execution parsers.
- **`metadata`**: Time & Space limits. **Crucially**, `allowed_languages` MUST be explicitly declared as: `["python", "cpp", "java", "javascript", "c"]`.
- **`topics`**: Array of topics categorizing the algorithmic needs.
- **`companyIndex`**: Index value corresponding to the parent array.

## 2. Test Cases and Extremity Analysis
Each file mandates **exactly 10 test cases**, carefully divided into logical testing blocks.
An analysis of the role-model (939_Minimum_Area_Rectangle) demonstrates proper stratification:

### A. Visibility Band (Test Cases 1-2)
- Target: Basic sanity validation provided dynamically by platform prompt.
- Structure: Standard, obvious configurations. 
- Flag: `"is_sample": true`

### B. Standard/Algorithmic Edges (Test Cases 3-7)
- Target: Tricking greedy algorithms or testing isolated boundary scenarios.
- Structure for 939: Collinear lines (unable to form rectangles), 0-area overlapping points, disjoint grids.
- Flag: `"is_sample": false`

### C. Extreme / Stress Band (Test Cases 8-10)
- Target: Stress testing the time limit ($O(N^2)$ algorithm) and maximal coordinate boundaries ($4 * 10^4$).
- Extremity Strategy ("A little bit extreme"): We do NOT dump massive 100,000 line arrays because it crashes lightweight code viewers and breaks valid JSON syntaxes. Instead, we use controlled boundaries (e.g., $N=500$ points) which perfectly reaches the `points.length` maximum without arbitrarily blowing up file sizes.
- Structure for 939: 
   - A grid spaced wildly apart (`0 0` vs `40000 40000`) testing overflow math calculations.
   - An array with maximum allowed nodes dynamically mapped programmatically to simulate stress validation.
- Flag: `"is_sample": false`

## 3. Strict Execution Policy
When automatically generating any subsequent question:
- Do NOT utilize complex inline string math evaluation (e.g. `+ Array().join()`) directly inside `write_to_file` arguments format, as it results in corrupt SyntaxError un-parsed string injection. 
- You must programmatically structure multi-language wrappers perfectly mapping standard input string inputs to expected function arguments.
