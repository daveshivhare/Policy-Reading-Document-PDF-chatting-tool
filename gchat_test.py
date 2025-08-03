from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # ✅ correct model name
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

response = llm.invoke("Hello Gemini, what can you do?")
print(response.content)



