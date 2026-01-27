import os
from langchain_mistralai import ChatMistralAI

os.environ["MISTRAL_API_KEY"] = "IsnRG8fdQhCI4OKXZ9U8OO4H7dMIVFgL"

llm = ChatMistralAI(model="mistral-small-latest")

response = llm.invoke("Bonjour ! dis-moi bonjour en 3 langues differentes.")

print("Reponse :", response.content)