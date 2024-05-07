Aiming:
1, Get YouTube transcript
2, Use Gemini API to summarize
3, Merge the 2
4, Use scrapping/crawling technique to summarize new/study/research

The structure would connect:
1, Storage with a list of sites
2, Basic site scraper
3, Cleaning process to simplify scraped data into its simplest format

Locally run LLM model (AI) is prompted with this data with instructions to either extract data or locate relevant elements’ sectors

Second site scraper1, crawling: crawlee: command: npx crawlee create my-crawler27.2.2024
1, run youtube transcript, crawlee api for spiderum web /
2, met vclvlcvclvll ngu da /
3, chay dc youtube transcript api /
4, bat dau du an
- get transcript, summarize /
+ input: "nhap video url:" x<-
+ extract the video ID:
https://www.youtube.com/watch?v=mlPS9MK5FZ4 -> mlPS9MK5FZ4 
+ gan cho bien X, nhap X vao

- get thumpnail and caption for folder from youtube api
- merge 2 subject and add a interfare if possible and try to make it automation
- find if can use multiple languages if possible
- somehow use chatgpt API to summarize if possible

- chay api chat gpt offline to import data form research paper
truoc do co the chay de summarize 
+ download the file from the link and some how input word even if in pdf 

- 4/3/2024
1, open .txt when finish / (copilot said it already does)
2, delete the previous file if there is one with the same name /
3, save the .txt file to current folder /
4, cut the unnessery part (cut the part in cdm, the part in .txt need more research)
5, use gemini to summarize (half, got the API)

- 5/3/2024
continue the work
currently have Gemini API, Langchain API

- x/3/2024
1, change so can add multiple videos ( not priority )
2, khong in dc nhieu vid vi open multiple .txt

4, auto design advance pptw.
idea for next project: chrome extension that can scraping and summarize, after that at to a list of new headlines in chrome

- x/4/2024
get NewAPI to read new every day.
New atcher API promote to get API for 1 month
https://docs.google.com/forms/d/e/1FAIpQLSejrsj4a1ZQkIasiKCtyaWbeaMb7iZ-TOPi5BHyUEGwnVSR9A/viewform7/3/2024 
1, fix to only save the .txt
2, now need to use Gemini API to summarize

7/5/2024
Update: 
1, Can use YoutubeAPI to get transcript only of the video
2, Can get name, language, translated script, thumbnail of the video
3, Can use Gemini API to summarize short text
4, Video transcript is way too long (norm >20000 characters/words) > study from Langchain to split the text file to smaller trunk to summarize, but struggle to keep the coherence, may need fine-tuning
5, Try to use Github Copilot Workspace
