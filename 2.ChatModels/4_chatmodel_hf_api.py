from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    # Adding these helps the Chat wrapper recognize the endpoint state
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France?")

print(result.content)
