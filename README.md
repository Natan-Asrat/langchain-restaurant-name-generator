# Restaurant Name Generator
This project uses LangChain to generate restaurant names and menu items based on selected cuisines. It utilizes a language model and sequential chaining to provide restaurant-related outputs.

## Contact
 - LinkedIn: [Natan Asrat](https://linkedin.com/in/natan-asrat)
 - Gmail: nathanyilmaasrat@gmail.com
 - Telegram: [Natan Asrat](https://t.me/fail_your_way_to_success)
 - Youtube: [Natville](https://www.youtube.com/@natvilletutor)

## Setup
### Prerequisistes
- Python 3.x installed on your system
- Installation of required Python packages:
  ```bash
  pip install langchain langchain_groq python-dotenv streamlit

## Environment Variables
 1. Create a .env file in the root directory of the project.
 2. Add your API key for GROQ as follows:
 ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   ```
## Running the Application

 1. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

 2. Access the application in your web browser at `http://localhost:8501`.

 3. Select a cuisine from the sidebar to generate a restaurant name and menu items.

## Code Explanation

### Backend Code

- Imports necessary modules:
  ```python
  from langchain.prompts import ChatPromptTemplate
  from langchain_groq import ChatGroq
  from langchain.chains import LLMChain, SequentialChain
  import os
  from dotenv import load_dotenv

  load_dotenv()
  ```

- Defines a sequential chain (`SequentialChain`) using LangChain to generate restaurant names and menu items based on prompts:
  ```python
  prompt1 = ChatPromptTemplate.from_messages([
      ("system", "Only answer with no description and with no disclaimers or notes."),
      ("user", "I want to open a restaurant for {cuisine}. Give me a restaurant name.")
  ])
  prompt2 = ChatPromptTemplate.from_messages([
      ("system", "Return as a comma separated string. Dont return other details."),
      ("user", "Suggest some menu items for {restaurant_name}")
  ])
  
  llm = ChatGroq(temperature=0.7)
  
  chain1 = LLMChain(prompt=prompt1, llm=llm, output_key="restaurant_name")
  chain2 = LLMChain(prompt=prompt2, llm=llm, output_key="menu_items")
  
  chain = SequentialChain(
      chains=[chain1, chain2],
      input_variables=["cuisine"],
      output_variables=["restaurant_name", "menu_items"]
  )
  ```

- Provides a function (`generate_restaurant_name_and_items`) that takes a cuisine as input and generates outputs using the defined chain:
  ```python
  def generate_restaurant_name_and_items(cuisine):
      return chain({'cuisine': cuisine})
  ```

### Frontend Interface (Streamlit)

- Uses Streamlit to create a user interface for selecting a cuisine and displaying generated restaurant names and menu items:
  ```python
  import streamlit as st
  import langchain_helper
  
  st.title("Restaurant Name Generator")
  
  cuisine = st.sidebar.selectbox("Pick a cuisine", (
      "Italian",
      "Ethiopian",
      "Mexican",
      "American"
  ))
  
  if cuisine:
      response = langchain_helper.generate_restaurant_name_and_items(cuisine)
      st.header(response['restaurant_name'].strip())
      st.write("**Menu Items**")
      menu_items = response['menu_items'].strip().split(",")
      for item in menu_items:
          st.write("-", item)
  ```