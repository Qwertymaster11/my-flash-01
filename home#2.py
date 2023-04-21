import openai

openai.api_key = "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"

response = openai.Image.create(
  prompt="solar system",
  n=4,
  size="1024x1024"
)
print(response)