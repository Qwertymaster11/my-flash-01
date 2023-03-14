import openai

# Load your API key from an environment variable or secret management service
openai.api_key = ""

ai = openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
print(ai)
