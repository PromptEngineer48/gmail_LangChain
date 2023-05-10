# https://python.langchain.com/en/latest/modules/agents/toolkits/examples/gmail.html

# Step 1: Create a json file and download the same in the working folder: https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application

# Step 2: pip install google-api-python-client, google-auth-oauthlib, google-auth-httplib2, beautifulsoup4, langchain

# Step 3: Add Users for testing this app In Authconsent Screen
# Issues resolved: https://stackoverflow.com/questions/65184355/error-403-access-denied-from-google-authentication-web-api-despite-google-acc

# Step 4: Enable it by visiting https://console.developers.google.com/apis/api/gmail.googleapis.com/overview?project=26982114008



from langchain.agents.agent_toolkits import GmailToolkit

toolkit = GmailToolkit() 

# tools = toolkit.get_tools()
# print(tools)

import os
os.environ['OPENAI_API_KEY'] = 'YOUR-API-KEY'

from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType

llm = OpenAI(temperature=0)

agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)


agent.run("Create a gmail draft for me to editor of a letter from the perspective of a sentient parrot"
          " who is looking to collaborate on some research with her"
          " estranged friend, a cat. Under no circumstances may you send the message, however.")

print(agent.run("Could you search in my drafts for the latest email?"))


