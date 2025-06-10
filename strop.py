from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

template1 = PromptTemplate(
    template="write a detail report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="write a 5 line summary on following text. /n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic":"Black Hole"})

res = model.invoke(prompt1)

prompt2 = template2.invoke({"text":res.content})

res1 = model.invoke(prompt2)

print(res1.content)