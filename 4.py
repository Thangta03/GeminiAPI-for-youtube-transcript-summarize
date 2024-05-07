from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import os
import json

try:
    video_url = input("Enter the YouTube video URL: ") 
    video_id = video_url.split("v=")[1]
    yt = YouTube(video_url)
    video_title = yt.title
    # Replace characters in title that are not allowed in file names
    valid_filename = "".join(i for i in video_title if i not in ":*?<>|/")
    # Translate the transcript to other languages
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['vi', 'en'])
    YouTubeTranscriptApi.get_transcripts([video_id], languages=['vi', 'en'])
    
    # Metadata for the video transcript
    print(
            video_title + '\n   ',  
            transcript.language + ' - ',
            transcript.language_code + ' - ',
            transcript.video_id  ,
)
except Exception as e:
    print("An error occurred:", str(e))

# Create a new directory named "transcript" in the current directory if it does not already exist
os.makedirs('transcript', exist_ok=True)

# Define the file path
file_path = os.path.join('transcript', f'{valid_filename}.txt')

# Open a text file in write mode
with open(file_path, 'w') as file:
    # Iterate over all available transcripts
    for transcript in transcript_list:
        # Translate the transcript to English
        translated_transcript = transcript.translate('en').fetch()

        # Remove the timestamp from the translated transcript
        for entry in translated_transcript:
            del entry['start']
            del entry['duration']

        # Write the translated transcript to the file
        file.write('Translated Transcript:\n')
        for entry in translated_transcript:
            file.write(entry['text'] + '\n')
        file.write('\n\n')

print("Transcript has been written to file.")

# Open the file with its associated application
import subprocess
subprocess.call(["xdg-open", file_path])
# os.startfile(file_path)