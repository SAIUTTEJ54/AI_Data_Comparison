import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY was not found.")
    exit()

print("API key loaded successfully.")

# Express Mode Gemini client
client = genai.Client(
    vertexai=True,
    api_key=api_key
)

# Test Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one short sentence."
)

print("\nGemini Response:")
print(response.text)