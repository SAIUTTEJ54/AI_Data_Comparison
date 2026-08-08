import json


# --------------------------------------------------
# Load evaluation results
# --------------------------------------------------

with open(
    "outputs/evaluation_results.json",
    "r"
) as file:

    results = json.load(file)


# --------------------------------------------------
# Total test cases
# --------------------------------------------------

total_cases = len(results)


# --------------------------------------------------
# Counters
# --------------------------------------------------

perfect_matches = 0
cases_with_differences = 0

missing_cases = 0
incorrect_cases = 0
conflicting_cases = 0
extra_cases = 0


# --------------------------------------------------
# Analyze every test case
# --------------------------------------------------

for result in results:

    missing = result["missing_information"]
    incorrect = result["incorrect_information"]
    conflicting = result["conflicting_information"]
    extra = result["extra_information"]

    has_difference = (
        len(missing) > 0
        or
        len(incorrect) > 0
        or
        len(conflicting) > 0
        or
        len(extra) > 0
    )

    # Perfect match
    if not has_difference:

        perfect_matches += 1

    # Case contains differences
    else:

        cases_with_differences += 1

    # Category-wise counts
    if len(missing) > 0:
        missing_cases += 1

    if len(incorrect) > 0:
        incorrect_cases += 1

    if len(conflicting) > 0:
        conflicting_cases += 1

    if len(extra) > 0:
        extra_cases += 1


# --------------------------------------------------
# Calculate percentages
# --------------------------------------------------

if total_cases > 0:

    perfect_match_rate = (
        perfect_matches / total_cases
    ) * 100

    difference_rate = (
        cases_with_differences / total_cases
    ) * 100

    missing_rate = (
        missing_cases / total_cases
    ) * 100

    incorrect_rate = (
        incorrect_cases / total_cases
    ) * 100

    conflicting_rate = (
        conflicting_cases / total_cases
    ) * 100

    extra_rate = (
        extra_cases / total_cases
    ) * 100

else:

    perfect_match_rate = 0
    difference_rate = 0
    missing_rate = 0
    incorrect_rate = 0
    conflicting_rate = 0
    extra_rate = 0


# --------------------------------------------------
# Display evaluation results
# --------------------------------------------------

print("\n========================================")
print("        EVALUATION RESULTS")
print("========================================")

print(f"Total Test Cases        : {total_cases}")
print(f"Perfect Matches         : {perfect_matches}")
print(f"Cases With Differences  : {cases_with_differences}")

print("----------------------------------------")

print(f"Missing Information     : {missing_cases}")
print(f"Incorrect Information   : {incorrect_cases}")
print(f"Conflicting Information : {conflicting_cases}")
print(f"Extra Information       : {extra_cases}")

print("----------------------------------------")

print(f"Perfect Match Rate      : {perfect_match_rate:.2f}%")
print(f"Difference Rate         : {difference_rate:.2f}%")

print("----------------------------------------")

print(f"Missing Case Rate       : {missing_rate:.2f}%")
print(f"Incorrect Case Rate     : {incorrect_rate:.2f}%")
print(f"Conflict Case Rate      : {conflicting_rate:.2f}%")
print(f"Extra Case Rate         : {extra_rate:.2f}%")

print("========================================")