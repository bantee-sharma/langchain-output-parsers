from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

res = chain.invoke({"topic":"Artificial Intelligence"})

print(res)