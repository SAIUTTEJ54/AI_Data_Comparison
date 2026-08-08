import os
from dotenv import load_dotenv
from google import genai


# --------------------------------------------------
# Load Gemini API key
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in .env")


# --------------------------------------------------
# Create Gemini client
# --------------------------------------------------

client = genai.Client(
    vertexai=True,
    api_key=api_key
)


# --------------------------------------------------
# Gemini explanation for conflicting information
# --------------------------------------------------

def get_ai_explanation(field, form_value, database_value):

    prompt = f"""
You are an AI data comparison assistant.

A form and a database contain information about the same person.

Field: {field}
Form value: {form_value}
Database value: {database_value}

The two values are different.

Explain in one short and simple sentence why this should be considered
a data conflict or mismatch.

Do not change either value.
Do not invent any information.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return f"{field} values do not match"


# --------------------------------------------------
# Compare two records
# --------------------------------------------------

def compare_records(form_data, database_data):

    missing_information = []
    incorrect_information = []
    conflicting_information = []
    extra_information = []

    # --------------------------------------------------
    # Check every field from the form
    # --------------------------------------------------

    for field, form_value in form_data.items():

        # Field exists in form but not in database
        if field not in database_data:

            missing_information.append({
                "field": field,
                "value": form_value
            })

        else:

            database_value = database_data[field]

            # Same field but different values
            if form_value != database_value:

                incorrect_information.append({
                    "field": field,
                    "form_value": form_value,
                    "database_value": database_value
                })

                # Ask Gemini to explain the conflict
                ai_explanation = get_ai_explanation(
                    field,
                    form_value,
                    database_value
                )

                conflicting_information.append(
                    ai_explanation
                )

    # --------------------------------------------------
    # Check for fields that exist only in database
    # --------------------------------------------------

    for field, database_value in database_data.items():

        if field not in form_data:

            extra_information.append({
                "field": field,
                "value": database_value
            })

    # --------------------------------------------------
    # Return comparison result
    # --------------------------------------------------

    return {
        "missing_information": missing_information,
        "incorrect_information": incorrect_information,
        "conflicting_information": conflicting_information,
        "extra_information": extra_information
    }