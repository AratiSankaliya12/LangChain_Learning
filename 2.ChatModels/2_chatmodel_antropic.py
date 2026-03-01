from langchain import ChatAntropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAntropic(model="claude-2", temperature=1.5, max_tokens=1024)

result = model.invoke("What is capital of india? ")

print(result)
