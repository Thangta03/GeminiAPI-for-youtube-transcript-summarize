# GeminiAPI for YouTube Transcript Summarization

## Project Overview
This project focuses on enhancing educational resources by efficiently extracting YouTube video transcripts and titles, dividing the transcript into smaller, manageable segments, summarizing each segment using Gemini API, and merging these summaries into a comprehensive educational resource. The process is designed to maintain coherence across summaries, ensuring the final output is both informative and concise.

## Features
- **Transcript Extraction**: Utilizes YouTube API to fetch video transcripts and titles.
- **Segment Division**: Divides the transcript into smaller segments for easier processing.
- **Summarization**: Employs Gemini API to summarize each segment, focusing on maintaining coherence across the summaries.
- **Merging Summaries**: Combines the summarized segments to form a unified educational resource.

## Implementation
1. **Extracting Transcripts and Titles**: The system begins by extracting the video transcript and title using the YouTube API.
2. **Dividing the Transcript**: The transcript is then divided into smaller segments. This division is crucial for managing the summarization process, as it allows for each segment to be summarized individually, ensuring a more coherent and comprehensive summary.
3. **Summarizing Segments**: Each segment is summarized using Gemini API. This step is key to condensing the information while retaining the essential messages.
4. **Merging Summaries**: Finally, the individual summaries are merged to create a complete, summarized version of the original transcript. This merged summary serves as a valuable educational resource.

## Usage
To utilize this system, follow the documentation provided in `README.md`, which guides users through the implementation and usage of the project's features.

## Challenges and Solutions
- **Maintaining Coherence**: One of the main challenges was ensuring coherence when dividing the transcript into smaller segments for summarization. This was addressed by carefully designing the segment division process and fine-tuning the summarization parameters.
- **Technical Implementation**: The project leverages GitHub Copilot Workspace for assistance in overcoming technical challenges, streamlining the development process.

## Future Directions
The project's methodology can be expanded to other applications, such as speech-to-text conversion, offering a foundation for further innovation in educational technology.

## Acknowledgments
This project was made possible through the use of YouTube API for transcript extraction and Gemini API for summarization. Special thanks to GitHub Copilot Workspace for providing valuable assistance throughout the development process.
