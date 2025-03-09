from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Give me the name, age and city of fictional person \n {format_instruction}",
    partial_variables={"format_instruction":parser.get_format_instructions()}
)


chain = template1 | model |parser


res = chain.invoke({})

print(res)