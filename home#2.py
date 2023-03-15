import openai

openai.api_key = ""

response = openai.Image.create(
  prompt="dog in 3d render.",
  n=1,
  size="1024x1024"
)
print(response)