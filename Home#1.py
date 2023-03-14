import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "Secret"

ai = openai.Completion.create(
  model="text-davinci-003",
  prompt="Tell me about apple.",
  max_tokens=1024,
  temperature=1
)
print(ai)
