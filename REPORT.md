# AI Data Comparison System

## 1. Project Title

AI-Based Data Comparison and Information Consistency Checking System

## 2. Objective

The objective of this project is to compare user-provided form data with database data and identify differences between them.

The system detects four major types of differences:

- Missing Information
- Incorrect Information
- Conflicting Information
- Extra Information

The comparison results are generated in a structured format and evaluated using predefined test cases.

## 3. Problem Statement

When information is collected through forms, it may differ from the information stored in a database. Manually checking these differences is time-consuming and error-prone.

This project provides an automated solution to compare both records and clearly report the differences between them.

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

### 5.1 Missing Information

A field is available in the form data but is not available in the database.

### 5.2 Incorrect Information

A field exists in both records, but the values are different due to incorrect information.

### 5.3 Conflicting Information

The same field contains different values in the form and database records.

### 5.4 Extra Information

A field is available in the database but is not available in the form data.

## 6. Technologies Used

The following technologies were used in the project:

- Python
- JSON
- Google Gemini API
- python-dotenv
- Google GenAI Python SDK
- VS Code
- Git
- GitHub

## 7. Project Structure

The project is organized as follows:

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
├── requirements.txt
├── README.md
└── REPORT.md