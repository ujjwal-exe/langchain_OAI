

#**Dependencies**



#!pip install langchain
#!pip install openai

import os
OPENAI_API_KEY = 'Enter_API_KEY'
os.environ["OPENAI_API_KEY"] = ""

from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9,openai_api_key=OPENAI_API_KEY)



while True:
    text = input('User:')
    if text == 'END':
        break
    else:
        print(llm(text))

# **API calls**


#**Prompt Template Management**

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(input_variables=["food"],
                        template= "What are 3 destinations for someoneone who likes to eat {food}?",)

print(prompt.format(food="dessert"))

print(llm(prompt.format(food="Seafood")))

"""# **just editing/ do not use in main**"""



from langchain.prompts import PromptTemplate

prompt = PromptTemplate(input_variables=["Education"],
                        template= input('User:'),)

print(llm(prompt.format))

# **Chains: Combine LLM and prompt in multi-step workflows**

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9,openai_api_key=OPENAI_API_KEY)

prompt = PromptTemplate(input_variables= ["food"],
                        template="What are the 5 destinations for someone who likes to eat {food}?",)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("fruit"))

# Agents: Dynamically call chains based on user **input**

pip install google-search-results

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

#load the model
llm = OpenAI(temperature=0,openai_api_key=OPENAI_API_KEY)

#load some tools
#------------/ code/-------------------------

#Serpapi dependencies
SERPAPI_API_KEY = 'Enter_API_KEY'

tools =load_tools(["serpapi","llm-math"], llm=llm, serpapi_api_key=SERPAPI_API_KEY)

# initialize agent with: 
#1)The Tools 
#2)The Language model
#3) The type of agent you want to use

agent = initialize_agent(tools,llm,agent= "zero-shot-react-description", verbose=True)

#Now lets test
agent.run("Who is the current leader of North korea? What is the largest prime number that is smaller than their age?")

"""# **Memory: Add state ro chains and agents**"""

from langchain import OpenAI , ConversationChain

#load the model
llm = OpenAI(temperature=0 , openai_api_key=OPENAI_API_KEY)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input='Hello!')

conversation.predict(input="I am doing great; Just having conversation with an AI!")

conversation.predict(input="What was the First thing i said to you?")

conversation.predict(input="What is the alternative phrase for the first thing i said to you")