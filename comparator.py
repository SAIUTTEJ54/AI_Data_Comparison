# comparator.py

# ----------------------------------------
# Generate a simple explanation locally
# ----------------------------------------

def get_local_explanation(field, form_value, database_value):
    return (
        f"The {field} value in the form "
        f"({form_value}) does not match the database value "
        f"({database_value})."
    )


# ----------------------------------------
# Compare two records
# ----------------------------------------

def compare_records(form_data, database_data):

    missing_information = []
    incorrect_information = []
    conflicting_information = []
    extra_information = []

    # ----------------------------------------
    # Check every field from the form
    # ----------------------------------------

    for field, form_value in form_data.items():

        # Field exists in form but not in database
        if field not in database_data:

            missing_information.append({
                "field": field,
                "value": form_value
            })

        else:

            database_value = database_data[field]

            # Same value
            if form_value == database_value:
                continue

            # Different value
            incorrect_information.append({
                "field": field,
                "form_value": form_value,
                "database_value": database_value
            })

            # Generate explanation locally
            explanation = get_local_explanation(
                field,
                form_value,
                database_value
            )

            conflicting_information.append(explanation)

    # ----------------------------------------
    # Check fields that exist only in database
    # ----------------------------------------

    for field, database_value in database_data.items():

        if field not in form_data:

            extra_information.append({
                "field": field,
                "value": database_value
            })

    # ----------------------------------------
    # Return comparison result
    # ----------------------------------------

    return {
        "missing_information": missing_information,
        "incorrect_information": incorrect_information,
        "conflicting_information": conflicting_information,
        "extra_information": extra_information
    }