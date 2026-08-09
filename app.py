import json
import os

from comparator import compare_records


# ----------------------------------------
# 1. Load test cases
# ----------------------------------------

with open("dataset/test_cases.json", "r") as file:
    test_cases = json.load(file)


# ----------------------------------------
# 2. Store all results
# ----------------------------------------

all_results = []


# ----------------------------------------
# 3. Compare every test case
# ----------------------------------------

for test_case in test_cases:

    test_id = test_case["test_id"]
    case_type = test_case["case_type"]

    form_data = test_case["form_data"]
    database_data = test_case["database_data"]

    # Compare the two records
    result = compare_records(
        form_data,
        database_data
    )

    # Add test information to result
    result["test_id"] = test_id
    result["case_type"] = case_type

    # Store result
    all_results.append(result)

    # ----------------------------------------
    # Display result in terminal
    # ----------------------------------------

    print("\n========================================")
    print(f"Test Case : {test_id}")
    print(f"Case Type : {case_type}")
    print("========================================")

    print("\nMissing Information:")
    print(result["missing_information"])

    print("\nIncorrect Information:")
    print(result["incorrect_information"])

    print("\nConflicting Information:")
    print(result["conflicting_information"])

    print("\nExtra Information:")
    print(result["extra_information"])


# ----------------------------------------
# 4. Save results
# ----------------------------------------

os.makedirs("outputs", exist_ok=True)

with open(
    "outputs/evaluation_results.json",
    "w"
) as file:

    json.dump(
        all_results,
        file,
        indent=4
    )


print("\n========================================")
print("All test cases completed successfully!")
print("Results saved to:")
print("outputs/evaluation_results.json")
print("========================================")