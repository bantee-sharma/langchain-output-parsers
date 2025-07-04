from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field,BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Schema
class Person(BaseModel):

    name: str = Field(description="name of the person")
    age: int = Field(gt=18,description="Age of the person")
    city: str = Field(description="city of the person")

parser = PydanticOutputParser(pydantic_object=Person)

temp = PromptTemplate(
    template="Generate the name, age and city of the fictional {place} person \  {format_instruction}",
    input_variables=["place"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = temp | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)