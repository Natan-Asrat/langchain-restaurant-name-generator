from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.chains import SequentialChain

# os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", "Only answer with no description and with no disclaimers or notes."),
        ("user", "I want to open a restaurant for {cuisine}. Give me a restaurant name.")
    ]
)
prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "Return as a comma separated string. Dont return other details."),
        ("user", "Suggest some menu items for {restaurant_name}")
    ]
)
llm = ChatGroq(
    temperature=0.7
)

chain1 = LLMChain(prompt= prompt1, llm = llm, output_key="restaurant_name")
chain2 = LLMChain(prompt= prompt2, llm = llm, output_key="menu_items")
chain = SequentialChain(
    chains = [chain1, chain2],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"]
)



def generate_restaurant_name_and_items(cuisine):
    return chain({'cuisine': cuisine})

if __name__ == "__main__":
    print(generate_restaurant_name_and_items('Ethiopian'))