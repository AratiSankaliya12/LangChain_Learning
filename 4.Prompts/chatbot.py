from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5.2", temperature=0)

while True:
    user_input = input("YOU: ")
    if user_input.lower() == "q":
        print("Goodbye!")
        break

    response = model.invoke(user_input)
    print("AI:")
    print(response.content)
