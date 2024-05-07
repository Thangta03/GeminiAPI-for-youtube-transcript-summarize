# pip install -q -U google-generativeai
import pathlib
import textwrap
import IPython
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
# Used to securely store your API key
# from google.colab import userdada

# API key
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key='AIzaSyDY05BBs50jLdrXfoGvgi2GCkNkV6lbtIw')

# for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

# Choose model
model = genai.GenerativeModel('gemini-pro')

# Get the question from the user
question = input("Please enter your question: ")

# Generate a response using the model
response = model.generate_content(question)

# Convert the response to markdown and print it
to_markdown(response.text)
print(response.text)
# Get feedback from the user about the response

# test 2
#model = genai.GenerativeModel('gemini-pro')
#chat = model.start_chat(history=[])
#chat

#response = chat.send_message("In one sentence, explain how a computer works to a young child.")
#to_markdown(response.text)
#response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

#for chunk in response:
  #print(chunk.text)
  #print("_"*80)
#for message in chat.history:
  #display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))

# Count tokens
model.count_tokens(response.text)


#Embedding
#result = genai.embed_content(
   # model="models/embedding-001",
    #content="What is the meaning of life?",
    #task_type="retrieval_document",
    #title="Embedding of single string")

# 1 input > 1 vector output
#print(str(result['embedding'])[:50], '... TRIMMED]')

#result = genai.embed_content(
    #model="models/embedding-001",
    #content=[
     # 'What is the meaning of life?',
      #'How much wood would a woodchuck chuck?',
      #'How does the brain work?'],
    #task_type="retrieval_document",
    #title="Embedding of list of strings")

# A list of inputs > A list of vectors output
#for v in result['embedding']:
 # print(str(v)[:50], '... TRIMMED ...')


# Multi optionals 
#response.candidates[0].content
#result = genai.embed_content(
 #   model = 'models/embedding-001',
  #  content = response.candidates[0].content)

#result = genai.embed_content(
 # model = 'models/embedding-001',
  #content = chat.history)

# 1 input > 1 vector output
# print(str(result['embedding'])[:50], '... TRIMMED ...')
# 1 input > 1 vector output
# for i,v in enumerate(result['embedding']):
  #print(str(v)[:50], '... TRIMMED...')


# Configeration
# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content(
  #  'Tell me a story about a magic backpack.',
   # generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
    #    candidate_count=1,
     #   stop_sequences=['x'],
      #  max_output_tokens=20,
       # temperature=1.0)

# text = response.text

# if response.candidates[0].finish_reason.name == "MAX_TOKENS":
  #  text += '...'

# to_markdown(text)
