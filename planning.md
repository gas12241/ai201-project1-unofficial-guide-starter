# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

My Domain will be "Places to eat around the University of Washington".

This knowledge is valuable because there are a wide variety of places to eat around the university, and some might not be well known. It isn't necesarily hard to find this information through official channels, per se, but to find a comprehensive list might be a little hard, which is why I think collecting documents about it (and creating my own RAG) is important.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| #   | Source                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | URL or location                                                                                                   |
| --- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | The Best Restaurants in Seattle's University District                                        | This webpage has a map on the right that showcases where the restaurants are. On the left side of the screen, there is the list of the best restaurants in the University District (which is near the University of Washington). After a brief intro, there is the name of the restaurant, followed by a description of the place, their address, their number, and a link to their website.                                                                                                                                                                                                                                                         | https://seattle.eater.com/maps/where-to-eat-u-district-university-of-washington-seattle                           |
| 2   | Restaurants near University of Washington                                                    | This web page has a list of restaurants. It shows an image of the restaurant, the name, it's rating out of 5, the number of reviews, the cuisine it falls under, when they open or close, a link to their menu, and some reviews.                                                                                                                                                                                                                                                                                                                                                                                                                    | https://www.tripadvisor.com/RestaurantsNear-g60878-d269796-University_of_Washington-Seattle_Washington.html       |
| 3   | What are the favorite restaurants among students around the University of Washington campus? | This web page is a thread where people mention their favorite restaurants, and include reasons why.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | https://www.quora.com/What-are-the-favorite-restaurants-among-students-around-the-University-of-Washington-campus |
| 4   | Restaurants near University of Washington                                                    | This webpage shows a list of restaurants. Each restaurant shown displays its Name, how many stars and reviews it has, how pricey it is out of four stars, the cuisine it falls under, the location, and a description of the restaurant (where you can hit read more at the bottom to see more of the descrption).                                                                                                                                                                                                                                                                                                                                   | https://www.opentable.com/landmark/restaurants-near-university-of-washington                                      |
| 5   | EATING THE AVE                                                                               | This website is made up of a bunch of small modules. Each of the modules has a title which may or may not be the name of the restaurant (it might not even be related to food, and if that's the case, you should skip it). You should look at the description below to see if you can find the restaurant name and it's address. The description can detail the food, as well as the restaurant itself.                                                                                                                                                                                                                                             | https://eatingtheave.com/                                                                                         |
| 6   | The Best Restaurants In The University District                                              | This website has a map on the right side that shows the location of the best restaurants in the University District (which resides right next to the University of Washington). On the left side of the web page are "The Spots," which list the restaurants. Every restaurant being shown has an image with the rating at the top right, the name of the restaurant, a scale out of 4 dollar signs that shows its price range, the cuisine it belongs to, it's location (along with it's address), a "Perfect for" section that shows what occasion would fit the restaurant, a small description of the restaurant, and a link to the full review. | https://www.theinfatuation.com/seattle/guides/best-restaurants-bars-university-district                           |
| 7   | Top 10 Best Restaurants Close To Uw Near Seattle, Washington                                 | Webpage that shows the best restaurants near the University of Washington. In the middle of the page, there are results that include the Name of the restaurant, how many stars it has out of 5 (including the number of reviews it has), when it opens or closes, a description of the restaurant given by one of the reviews, and a few lables that tell you what kind of cuisine the restaurant falls under. please skip the sponsored results at the top of the page. The first restaurant is numbered (i.e. 1.)                                                                                                                                 | https://www.yelp.com/search?find_desc=Restaurants+Close+To+Uw&find_loc=Seattle%2C+WA&dd_referrer=                 |
| 8   | Where to Eat in the University District                                                      | This webpage shows places to eat in the University District, also known as the U-district (which is close to the University of Washington). Following the headers of every Restaurant name is the description of the restaurant itself. Some of the descriptions will also include a photo.                                                                                                                                                                                                                                                                                                                                                          | https://www.seattlemet.com/eat-and-drink/where-to-eat-in-the-university-district-uw-restaurants                   |
| 9   | Best Food Near the University of Washington                                                  | This webpage has a table of contents that has every restaurant they mention throughout the article. Below the table of contents is a small intro of the list, followed by the names of each restaurant, with their personal description. There are ads on the right side of the page that should not be read.                                                                                                                                                                                                                                                                                                                                        | https://tripalink.com/blog/best-food-near-university-of-washington                                                |
| 10  | Where To Have A Casual Meal Near UW                                                          | This webpage has a map on the right side that shows the location of the 11 places named in the article. Underneath the "The Spots" header is the list of the 11 places you can eat around the University of Washington (also known as UW). Every restaurant being shown has an image with the rating at the top right, the name of the restaurant, a scale out of 4 dollar signs that shows its price range, the cuisine it belongs to, it's location (along with it's address), a "Perfect for" section that shows what occasion would fit the restaurant, a small description of the restaurant, and a link to the full review.                    | https://www.theinfatuation.com/seattle/guides/restaurants-near-uw                                                 |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
I think 200 characters as a chunk size isn't too bad, most of the descriptions of places
aren't too long, so I'll test it out, but 200 seems like a good place to start.

**Overlap:**
I think an overlap of 50 characters sounds good to start.

**Reasoning:**
From the lab, they had chunks of 300 with an overlap of 50. The overlap of 50 seems reasonable but considering that the descriptions are not on average as long as some rules, I toned both down and went with a chunk size of 200.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
I will use all-MiniLM-L6-v2 via sentence-transformers as it is the recommended option.

**Top-k:**
Considering how many restaurants are mentioned in the sources, I think 5 is a good amount. More than that, and you might get restaurants that don't fit the query, and dilute the answer given.

**Production tradeoff reflection:**
If there aren't enough results for a prompt, 5 results could dilute the answer. Will see if I have to lower.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| #   | Question                                                                                                              | Expected answer                                                                    |
| --- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1   | Are there any bakeries you would recommend in Portage? Bay                                                            | Saint Bread is a former motor boatyard in Portage Bay that is a bakery.            |
| 2   | I want a Caribbean sandwich near the University of Washington. Could you tell me of a place that sells them?          | Paseo Caribbean Food sells Caribbean Sandwiches near the University of Washington. |
| 3   | Thai food sounds good right now. Can you recommend me a place near the University of Washington that sells Thai Food? | Should Include Jai Thai and Thai Tom's or something similar                        |
| 4   | Pizza near the University                                                                                             | MOD Pizza, Pagliaci                                                                |
| 5   | I'd like a bagel near the University Distrcit, got any ideas?                                                         | Hey bagel.                                                                         |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. There is a web page that is semi consistent. The person either named their headers by the food, or the restaurant. I think querying something from there might lead to some bad retrievals.

2. I am scared that the chunk size is too big and that I'll get results that aren't the most relevant.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

User query
│
▼
[1] DOCUMENT INGESTION ──► Web pages are collected and stored once at startup
ingest.py
│
▼
[2] CHUNKING ──► Text is split into chunks for embedding
│
▼
[3] EMBEDDING (all-MiniLM-L6-v2) + VECTOR STORE (ChromaDB) ──► Chunks are embedded and stored in a similarity index
│
▼
[4] RETRIEVAL ──► Query is embedded and matched against stored chunks
retriever.py via semantic similarity search
│
▼
[5] GENERATION ──► Retrieved chunks are passed as context to an LLM,
generator.py which produces a grounded, cited answer

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

<!-- - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.) -->

Claude

<!-- - What you'll give it as input (which sections of this planning.md, which requirements) -->

I created a chunk-document-spec.md, which I based off of the lab that we did. I will give it that,
and then ask it to make an ingest.py file similar to the one from class.

<!-- - What you expect it to produce -->

I expect it to make me a file similar to the the one in class BUT with some things changed. Considering
I don't need the game name like we did in the lab, but we do need the Source Name and URL, I am expecting
the ingest.py file to account for those.

<!-- - How you'll verify the output matches your spec -->

The variable names in the file make it pretty clear that they are following what is most important,
my chunking strategy.

**Milestone 4 — Embedding and retrieval:**

<!-- - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.) -->

Claude

<!-- - What you'll give it as input (which sections of this planning.md, which requirements) -->

My ingest.py file as well as the example retriever.py file from class.

<!-- - What you expect it to produce -->

A retriever that takes into account the source and URL instead of game name like in the lab.

<!-- - How you'll verify the output matches your spec -->

Compare it to the one we did in class.

**Milestone 5 — Generation and interface:**

<!-- - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.) -->

Claude

<!-- - What you'll give it as input (which sections of this planning.md, which requirements) -->

Examples from the lab (the generator and app for the interface). Explicit instructions on what I
want to be generated (for example grounding instructions as well as explicit inclusion of the
source it was taken from - which may also include the URL).

<!-- - What you expect it to produce -->

A Gradio interface that will work with my project, as well as a generator that gives information based
soley on what I trained it on and nothing else. It will also generate the source and URL where applicable.

<!-- - How you'll verify the output matches your spec -->

The generator and interface can be checked when running the app. Are the questions grounded? If
they are, then I know they followed my spec.
