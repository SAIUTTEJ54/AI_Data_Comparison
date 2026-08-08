# AI Data Comparison System

## 1. Project Title

AI-Based Data Comparison and Information Consistency Checking System

## 2. Objective

The objective of this project is to compare user-provided form data with database data and identify differences between them.

The system detects:
- Missing Information
- Incorrect Information
- Conflicting Information
- Extra Information

## 3. Problem Statement

When information is collected through forms, it may differ from the information stored in a database. Manually checking these differences is time-consuming and error-prone.

This project provides an automated solution to compare both records and clearly report the differences.

## 4. System Workflow

The system follows these steps:

1. Receive form data.
2. Receive database data.
3. Compare the fields in both records.
4. Identify missing information.
5. Identify incorrect information.
6. Identify conflicting information.
7. Identify extra information.
8. Store the comparison results.
9. Evaluate the results using predefined test cases.

## 5. Types of Differences

### Missing Information

A field is available in the form data but is not available in the database.

### Incorrect Information

A field exists in both records, but the values are different.

### Conflicting Information

The same field contains different values in the form and database.

### Extra Information

A field is available in the database but is not available in the form.

## 6. Technologies Used

- Python
- JSON
- Google Gemini API
- python-dotenv
- Google GenAI Python SDK
- VS Code

## 7. Project Structure

```text
AI_Data_Comparison/
│
├── dataset/
│   └── test_cases.json
│
├── outputs/
│   └── evaluation_results.json
│
├── screenshots/
│
├── app.py
├── comparator.py
├── evaluator.py
├── gemini_test.py
├── .env
├── requirements.txt
├── README.md
└── REPORT.md
## 8. Implementation Details

The project is implemented using Python and JSON-based test data.

### 8.1 app.py

The `app.py` file is the main execution file of the project. It loads the test cases, compares the form data with the database data, displays the comparison results, and stores the results in the output file.

### 8.2 comparator.py

The `comparator.py` file contains the main comparison logic.

The system compares both records field by field and identifies:

- Missing Information
- Incorrect Information
- Conflicting Information
- Extra Information

The comparison results are returned in a structured JSON format.

### 8.3 evaluator.py

The `evaluator.py` file evaluates the generated comparison results.

It calculates:

- Total Test Cases
- Perfect Matches
- Cases With Differences
- Missing Information
- Incorrect Information
- Conflicting Information
- Extra Information
- Perfect Match Rate
- Difference Rate
- Individual Case Rates

### 8.4 gemini_test.py

The `gemini_test.py` file is used to verify the Google Gemini API connection and generate a test response.

The Gemini API key is securely loaded from the `.env` file using `python-dotenv`.

## 9. Test Cases

The system was tested using 15 predefined test cases.

The test cases cover different data comparison scenarios, including:

1. Perfect Match
2. Incorrect Value
3. Extra Information
4. Missing Information
5. Incorrect Department
6. Multiple Differences
7. Missing College
8. Extra Email
9. Incorrect Name
10. Perfect Match
11. Missing Multiple Fields
12. Extra Multiple Fields
13. Age Conflict
14. Sensitive Information Difference
15. Perfect Match

These test cases are stored in:

`dataset/test_cases.json`

## 10. Evaluation Results

The system was evaluated using 15 test cases.

| Metric | Result |
|---|---:|
| Total Test Cases | 15 |
| Perfect Matches | 3 |
| Cases With Differences | 12 |
| Missing Information | 3 |
| Incorrect Information | 6 |
| Conflicting Information | 6 |
| Extra Information | 3 |
| Perfect Match Rate | 20.00% |
| Difference Rate | 80.00% |
| Missing Case Rate | 20.00% |
| Incorrect Case Rate | 40.00% |
| Conflict Case Rate | 40.00% |
| Extra Case Rate | 20.00% |

The evaluation results are stored in:

`outputs/evaluation_results.json`

## 11. Screenshots

The project execution and evaluation results were captured as screenshots.

The screenshots include:

- Evaluation results
- Test cases 1–4
- Test cases 5–8
- Test cases 9–12
- Test cases 13–15

All screenshots are stored in the `screenshots/` folder.

## 12. Conclusion

The AI Data Comparison System provides an automated approach for comparing form data with database data.

The system successfully identifies missing, incorrect, conflicting, and extra information between two records.

The predefined test cases demonstrate that the comparison logic can identify different types of data inconsistencies and generate structured evaluation results.