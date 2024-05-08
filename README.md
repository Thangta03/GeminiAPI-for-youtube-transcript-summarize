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

### Installing Required Packages
To install the required Python packages for this project, run the following command in your terminal:
```
pip install -r requirements.txt
```
This will install all the necessary packages listed in the `requirements.txt` file, ensuring that the project's dependencies are met.

## Configuring API Keys
To enhance security and flexibility, it's recommended to store your Gemini API key in environment variables. This approach allows you to keep your API keys secure while also making it easy to update them without changing your application's code.

### Setting Up Environment Variables
#### For Windows:
1. Open the Start Search, type in "env", and choose "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables..." button.
3. In the Environment Variables window, click on the "New..." button under the "User variables" section.
4. Enter `GEMINI_API_KEY` as the Variable name and your Gemini API key as the Variable value.
5. Click OK and apply the changes.

#### For Unix-based Systems (Linux/Mac):
1. Open your terminal.
2. Edit your profile file (e.g., `~/.bash_profile`, `~/.zshrc`, `~/.profile`, etc.) using a text editor.
3. Add the following line to the file: `export GEMINI_API_KEY="your_gemini_api_key"`.
4. Save the file and reload your profile (e.g., run `source ~/.bash_profile`).

After setting up the environment variable, you can access your Gemini API key in your application using the appropriate method for your programming language (e.g., `os.getenv('GEMINI_API_KEY')` in Python).

## Challenges and Solutions
- **Maintaining Coherence**: One of the main challenges was ensuring coherence when dividing the transcript into smaller segments for summarization. This was addressed by carefully designing the segment division process and fine-tuning the summarization parameters.
- **Technical Implementation**: The project leverages GitHub Copilot Workspace for assistance in overcoming technical challenges, streamlining the development process.

## Future Directions
The project's methodology can be expanded to other applications, such as speech-to-text conversion, offering a foundation for further innovation in educational technology.

## Acknowledgments
This project was made possible through the use of YouTube API for transcript extraction and Gemini API for summarization. Special thanks to GitHub Copilot Workspace for providing valuable assistance throughout the development process.
