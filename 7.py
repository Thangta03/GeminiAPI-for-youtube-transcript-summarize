from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import os
import json
import pathlib
import textwrap
import IPython
import google.generativeai as genai
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key='AIzaSyDY05BBs50jLdrXfoGvgi2GCkNkV6lbtIw')
model = genai.GenerativeModel('gemini-pro')

try:
    video_url = input("Enter the YouTube video URL: ") 
    video_id = video_url.split("v=")[1]
    yt = YouTube(video_url)
    video_title = yt.title
    valid_filename = "".join(i for i in video_title if i not in ":*?<>|/")
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['vi', 'en'])
    YouTubeTranscriptApi.get_transcripts([video_id], languages=['vi', 'en'])

    os.makedirs('transcript', exist_ok=True)
    file_path = os.path.join('transcript', f'{valid_filename}.txt')

    with open(file_path, 'w') as file:
        for transcript in transcript_list:
            translated_transcript = transcript.translate('en').fetch()
            for entry in translated_transcript:
                del entry['start']
                del entry['duration']
            file.write('Translated Transcript:\n')
            for entry in translated_transcript:
                file.write(entry['text'] + '\n')
            file.write('\n\n')

    print("Transcript has been written to file.")

    with open(file_path, 'r') as file:
        transcript_text = file.read()

    response = model.generate_content(transcript_text)
    to_markdown(response.text)
    print(response.text)

except Exception as e:
    print("An error occurred:", str(e))