#Import Libraries
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
# from google.colab import userdata

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
genai.configure(api_key='AIzaSyDY05BBs50jLdrXfoGvgi2GCkNkV6lbtIw')

# Initialize the chat:
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
chat

# Note: The vision model gemini-pro-vision is not optimized for multi-turn chat.
# The ChatSession.send_message method returns the same GenerateContentResponse type as GenerativeMode   l.generate_content. It also appends your message and the response to the chat history:

response = chat.send_message(" Similar to consumer theory, the optimization problem in producer theory assumes that there is an interior solution. Therefore, convexity of the producer choice set is important for finding a unique optimal interior solution. (a) Show graphically that a convex choice set leads to an interior solution. (b) Show graphically that when the choice set is non-convex we might end up with a corner solution. (c) Show graphically that when the choice set is non-convex we might have multiple solutions.")
to_markdown(response.text)
# Chat history
chat.history

# Steam (You can keep sending messages to continue the conversation. Use the stream=True argument to stream the chat)
response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

for chunk in response:
  print(chunk.text)
  print("_"*80)    

# glm.Content objects contain a list of glm.Part objects that each contain either a text (string) or inline_data (glm.Blob), where a blob contains binary data and a mime_type. The chat history is available as a list of glm.Content objects in ChatSession.history:  
for message in chat.history:
  display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))