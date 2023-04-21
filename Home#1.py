import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "-"
res = openai.Image.create(
  prompt="Modern house",
  n=1,
  size="1024x1024"
)
print(res)
