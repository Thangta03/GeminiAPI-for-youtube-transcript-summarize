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

# Fetch API key from environment variable
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def divide_transcript_into_segments(transcript, segment_length=1000):
    """
    Divides the transcript into smaller segments of approximately segment_length characters.
    """
    segments = []
    current_segment = ""
    for paragraph in transcript.split('\n'):
        if len(current_segment) + len(paragraph) > segment_length:
            segments.append(current_segment)
            current_segment = paragraph + '\n'
        else:
            current_segment += paragraph + '\n'
    segments.append(current_segment)  # Add the last segment
    return segments

def summarize_segment(segment):
    """
    Summarizes a segment of the transcript using Gemini API.
    """
    response = model.generate_content(segment)
    return response.text

def merge_summaries(summaries):
    """
    Merges the summarized segments into a single summary.
    """
    return '\n'.join(summaries)

try:
    video_url = input("Enter the YouTube video URL: ") 
    video_id = video_url.split("v=")[1]
    yt = YouTube(video_url)
    video_title = yt.title
    valid_filename = "".join(i for i in video_title if i not in ":*?<>|/")
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['vi', 'en']).fetch()
    full_transcript = ' '.join([item['text'] for item in transcript])
    
    segments = divide_transcript_into_segments(full_transcript)
    summaries = [summarize_segment(segment) for segment in segments]
    final_summary = merge_summaries(summaries)
    
    os.makedirs('summaries', exist_ok=True)
    summary_file_path = os.path.join('summaries', f'{valid_filename}_summary.txt')
    with open(summary_file_path, 'w') as file:
        file.write(final_summary)
    
    print(f"Summary has been written to {summary_file_path}")

except Exception as e:
    print("An error occurred:", str(e))
