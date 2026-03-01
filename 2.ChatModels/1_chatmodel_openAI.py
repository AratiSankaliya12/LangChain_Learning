from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.5, max_completion_tokens=1024)

result = model.invoke([{"role": "user", "content": "Hello, world!"}])

print("Model invoked successfully.")

print(result.content)
