from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

prompt = input("You: ")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)

print(response.output_text)