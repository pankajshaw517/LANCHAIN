from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

query = "How do I optimize a Hive SQL query?"

vector = embeddings.embed_query(query)

print(vector[:10])
print("Vector dimensions:", len(vector))
