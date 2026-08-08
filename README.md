# AI Data Comparison System

## Overview

AI Data Comparison System is a Python-based application that compares user-provided form data with database data and identifies differences between the two records.

The system identifies four types of information:

- Missing Information
- Incorrect Information
- Conflicting Information
- Extra Information

## Objective

The main objective of this project is to automate the process of comparing user-provided information with existing database information.

This reduces manual checking and makes data inconsistencies easier to identify.

## Problem Statement

Information collected through forms may differ from the information stored in a database. Manually checking these differences can be time-consuming and error-prone.

This project provides an automated solution to compare both records and clearly report the differences.

## System Workflow

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

## Types of Differences

### Missing Information

A field is available in the form data but is not available in the database.

### Incorrect Information

A field exists in both records, but the values are different.

### Conflicting Information

The same field contains different values in the form and database.

### Extra Information

A field is available in the database but is not available in the form.

## Technologies Used

- Python
- JSON
- Google Gemini API
- python-dotenv
- Google GenAI Python SDK
- Visual Studio Code

## Project Structure

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
│   ├── evaluation_results.png
│   ├── test_cases_output_1-4.png
│   ├── test_cases_output_5-8.png
│   ├── test_cases_output_9-12.png
│   └── test_cases_output_13-15.png
│
├── app.py
├── comparator.py
├── evaluator.py
├── gemini_test.py
├── .env
├── requirements.txt
├── README.md
└── REPORT.md