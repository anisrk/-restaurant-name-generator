from langchain_openai import OpenAI  # Use updated import
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret_key import openapi_key
import os

# Set API key
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Prompt for restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Prompt for menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # SequentialChain to execute in order
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        return_all=True  # Ensures full output
    )

    # Execute the chain
    response = chain.invoke({'cuisine': cuisine})

    return response

# Run function if executed as script
if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
