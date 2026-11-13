from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI( model="gpt-4.1-mini")

result = llm.invoke("What is the capital of India")

print(result)
#The capital of India is New Delhi.