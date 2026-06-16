# The Unofficial Guide — Project 1

**Link to Demo**
https://www.youtube.com/watch?v=Q8PAcSbdoRg

> **How to use this template:**
> Complete each section _after_ you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover? -->

My Domain will be "Places to eat around the University of Washington".

<!-- Why is this knowledge valuable, and why is it hard to find through official channels?
Example: "Student reviews of CS professors at [university] — useful because official
course descriptions don't reflect teaching style, exam difficulty, or workload." -->

This knowledge is valuable because there are a wide variety of places to eat around the university, and some might not be well known. It isn't necesarily hard to find this information through official channels, per se, but to find a comprehensive list might be a little hard, which is why I think collecting documents about it (and creating my own RAG) is important.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives.
     Document, page, or thread -->

| #   | Source                                                                                       | Type     | URL or file path                                                                                                  |
| --- | -------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | The Best Restaurants in Seattle's University District                                        | Web Page | https://seattle.eater.com/maps/where-to-eat-u-district-university-of-washington-seattle                           |
| 2   | Restaurants near University of Washington                                                    | Web Page | https://www.tripadvisor.com/RestaurantsNear-g60878-d269796-University_of_Washington-Seattle_Washington.html       |
| 3   | What are the favorite restaurants among students around the University of Washington campus? | Web Page | https://www.quora.com/What-are-the-favorite-restaurants-among-students-around-the-University-of-Washington-campus |
| 4   | Restaurants near University of Washington                                                    | Web Page | https://www.opentable.com/landmark/restaurants-near-university-of-washington                                      |
| 5   | EATING THE AVE                                                                               | Web Page | https://eatingtheave.com/                                                                                         |
| 6   | The Best Restaurants In The University District                                              | Web Page | https://www.theinfatuation.com/seattle/guides/best-restaurants-bars-university-district                           |
| 7   | Top 10 Best Restaurants Close To Uw Near Seattle, Washington                                 | Web Page | https://www.yelp.com/search?find_desc=Restaurants+Close+To+Uw&find_loc=Seattle%2C+WA&dd_referrer=                 |
| 8   | Where to Eat in the University District                                                      | Web Page | https://www.seattlemet.com/eat-and-drink/where-to-eat-in-the-university-district-uw-restaurants                   |
| 9   | Best Food Near the University of Washington                                                  | Web Page | https://tripalink.com/blog/best-food-near-university-of-washington                                                |
| 10  | Where To Have A Casual Meal Near UW                                                          | Web Page | https://www.theinfatuation.com/seattle/guides/restaurants-near-uw                                                 |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
I went with a chunk size of 200. 300 was used in the lab, and I felt like the reviews/descriptions
for the restaurants are shorter than that, so I lowered the number.

**Overlap:**
I went with an overlap of 50, basing it off the lab.

**Why these choices fit your documents:**
Like I stated above, I shortened both the chunk size and overlap because of how long parts of
the texts were in comparison to the lab. Longer chunks would lead to a lower Retrieval score.

**Final chunk count:**
I finished with the smallest bit north of 500; 501 chunks.

**5 labeled Sample chunks with their source document name**
Here I am showing chunk #2 from 5 different sources:

[best_food_near_the_university_of_washington_1]
rsity of Washington
Date: Jun 4, 2025

1. Thai Tom - Small Thai restaurant on the Ave known for Pad Thai and Spicy Basil Noodle with casual atmosphere
2. Agua Verde Café & Paddle Club - Waterfront Mex

---

[eating_the_ave_1]
again cherry blossom festival

Apr 12, 2022 2. U District Cherry Blossom Festival
My first stop was Kai’s Thai Street Food and Bar, which had pink cherry blossom noodle soup as its special. The soup

---

[restaurants_near_university_of_washington_(tripadvisor)_1]
on-Seattle_Washington.html

Restaurants Near University of Washington - Seattle (2026)

Top Ranked Restaurants

1. Portage Bay Cafe - Roosevelt
   - Rating: 4.4/5 (531 reviews)
   - Distance: 0.5

---

[restaurants_near_university_of_washington_(opentable)_1]
he Pink Door
Exceptional
(10026)
• Italian • Belltown / Pike Place Market
The Pink Door is an independently owned (never cloned, never genetically modified) restaurant that has been quietly dedic

---

[the_best_restaurants_in_seattle’s_university_district_1]
ttle

Dining Out in Seattle
The Best Restaurants in Seattle’s University District
A guide to University of Washington’s neighborhood, for Huskies and visitors alike

Updated Dec 8, 2025, 10:59 AM PS

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

## 3 retrieval test examples, each showing the query and the top returned chunks (with explanations)\*\*

I used the first 3 chunks because although I use 5, I feel like it would elongate the README more than necessary.

**Query 1**
Thai food near UW?

**Top Chunks**
Result 1:
Source : EATING THE AVE
Distance: 0.339
Text : raw gai and kao mun gai are among my favorite dishes in the U District. The place reminds me a lot of Thailand - I spent about two months there in 2007. In Thailand, most of my dining experiences were

Result 2:
Source : EATING THE AVE
Distance: 0.351
Text : nd share a meal together. I thought through where I wanted to order food from - I knew it had to be the U District. I thought about getting more Thai food, but decided on the Indian restaurant Cedars

Result 3:
Source : What are the favorite restaurants among students around the University of Washington campus?
Distance: 0.352
Text : er Place.

- Krua: Thai Family Kitchen (http://www.kruaseattle.com/). Can't recommend this enough. Ask them for their secret Thai menu.

**Explanation**
Mentions Thai food, Thailand, it's specific food, or a Thai restaurant.

**Query 2**
Coffee UW?

**Top Chunks**
Result 1:
Source : EATING THE AVE
Distance: 0.501
Text : 9 Seattle Magazine story, titled “One Family Looks to Bring Brazil’s Hospitality and Pastries to Seattle.” Kitanda is one of my favorite cafes - I love the Brazilian latte, kitanda bread and chicken c

Result 2:
Source : Where to Eat in the University District
Distance: 0.554
Text : arugula, peppery aioli, and egg yolk drizzling down folds of prosciutto—will impress you with its nuance, but also slay that hangover.

Off the Rez Cafe
Seattle’s first Native American food truck sp

Result 3:
Source : What are the favorite restaurants among students around the University of Washington campus?
Distance: 0.558
Text : falutin' attitude of the patrons & employees.

Near campus:
Orange King - burgers, burgers, burgers.
Schultzy's - best draught beer in the U-District, delicious sausages, crispy fries.
Flowers - food

**Explanation**
Result 1 and 2 mention coffee. I've tested this when generated and it finds that the 3rd closest chunk isn't related and doesn't use it.

**Query 3**
I'm craving sushi, where can I go?

**Top Chunks**
Result 1:
Source : Where To Have A Casual Meal Near UW
Distance: 0.327
Text : Japanese

- Address: 5211 University Way Northeast, Seattle, WA 98105
- Perfect For: Casual Dinners, Gluten-Free Options, Walk-Ins
- Description: "The dining room at Village Sushi looks kind of looks l

Result 2:
Source : The Best Restaurants in Seattle’s University District
Distance: 0.359
Text : or excellent starters.
5259 University Way NE, Seattle, WA, 98105, US
(206) 522-8888

Village Sushi
Village Sushi might be the coziest sushi restaurant in the city. It’s in a vintage space (formerly

Result 3:
Source : EATING THE AVE
Distance: 0.367
Text : i, so we headed there before catching a movie. The sushi is delicious, but a highlight is the tatsutage, the fried chicken (on the left in the picture). They had limited capacity, but we sat at a tabl

**Explanation**
Result 1 and 2 show places that include sushi in the name or include the word sushi.

**Model used:**
all-MiniLM-L6-v2

**Production tradeoff reflection:**
I actually wasn't aware that we were allowed to switch models. It was considered part of the recommended stack at the top of the assignment, so I figured there was a good reason for that.

That being said, if I had to do it again, one thing I would have liked to have researched is chunking based on paragraphs. It was something that I saw as a suggestion a couple times throughout the assingment, and I think it would have benefitted a RAG like this one (Because of the way the text is setup).

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**Example system response with source attribution 1**
_Input_
Any good Mexican food near UW?

_Output_
According to the provided text, there are a few options for Mexican food near UW.

From the source "What are the favorite restaurants among students around the University of
Washington campus?" (https://www.quora.com/), Chipotle is mentioned as the "Only good Mexican
on the Ave proper."

Additionally, from the source "Best Food Near the University of Washington"
(https://tripalink.com/blog/best-food-near-university-of-washington), Tacos Chukis is
mentioned as a "Mexican restaurant featuring al pastor tacos cooked on a rotating spit."

These are the only two sources that mention Mexican food options near UW based on the provided context.

**Example system response with source attribution 2**
_Input_
I'd like some pizza, where could I go for Pizza near UW?

_Output_
You can go to Pagliacci Pizza (Source: Best Food Near the University of Washington |
https://tripalink.com/blog/best-food-near-university-of-washington) or MOD Pizza
(Source: Restaurants near University of Washington (TripAdvisor) |
https://www.tripadvisor.com/RestaurantsNear-g60878-d269796-University_of_Washington-Seattle_Washington.html)
for pizza near the University of Washington.

**Example out-of-scope query with system refusal response shown**
_Input_
Where can I get pufferfish near UW?

_Output_
The provided context does not mention pufferfish or any restaurants serving pufferfish near UW. [Source: All provided sources]

**System prompt grounding instruction:**
My system message told says a few things to prompt grounded instruction. It tells the LLM that they are a restaurant guide for the University of Washington. It goes on to say to ONLY answer given information provided below (and not to guess/infer based on things they know about Seattle). If the answer is not contained in the context, it will say so clearly.
**How source attribution is surfaced in the response:**
The system message also states to "Always identify which source your answer comes from."

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| #   | Question                                                                                                              | Expected answer                                                                    | System response (summarized)                                                                           | Retrieval quality  | Response accuracy |
| --- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------ | ----------------- |
| 1   | Are there any bakeries you would recommend in Portage?                                                                | Saint Bread is a former motor boatyard in Portage Bay that is a bakery.            | Answers affirmatively, also tells the user about Saint Bread and some of the things they sell          | Relevant           | Accurate          |
| 2   | I want a Caribbean sandwich near the University of Washington. Could you tell me of a place that sells them?          | Paseo Caribbean Food sells Caribbean Sandwiches near the University of Washington. | Replies that there isn't any provided context that mentions caribbean Sandwiches or Caribbean cuisine. | Off-target         | Inaccurate        |
| 3   | Thai food sounds good right now. Can you recommend me a place near the University of Washington that sells Thai Food? | Should Include Jai Thai and Thai Tom's or something similar.                       | Mentions fice places to get Thai food, including the ones I wanted originally.                         | Relevant           | Accurate          |
| 4   | Pizza near the University.                                                                                            | MOD Pizza, Pagliacci.                                                              | Mentions Pagliacci, but not MOD Pizza.                                                                 | Partially Relevant | Off-target        |
| 5   | I'd like a bagel near the University Distrcit, got any ideas?                                                         | Hey bagel.                                                                         | Mentions Hey Bagel, along with their address, their rating, and a review of theirs.                    | Relevant           | Accurate          |

**Retrieval quality:** Relevant / Partially relevant / Off-target
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
The question about Caribbean Sandwiches:
"I want a Caribbean sandwich near the University of Washington. Could you tell me of a place that sells them?"
**What the system returned:**
"Based on the provided context, there is no mention of a Caribbean sandwich or a restaurant that sells Caribbean cuisine near the University of Washington. The sources provided only mention restaurants serving burgers, Vietnamese, and Thai cuisine.

Source: The provided context from various sources, including TripAdvisor, The Infatuation, and Eater."
**Root cause (tied to a specific pipeline stage):**
Document Cleaning/chunking
**What you would change to fix it:**
Add lines between reviews in the file that the answer is supposed to come from. I would also play with
the chunk size and overlap. The chunks might be too big to get a high retrieval score. Lastly, if neither
worked, I would try changing how the chunks were embedded. I would do this because in the file, it talks
about "Caribbean-influcenced sandwiches," and that was enough to not get a match, so I'm assuming if I
had a different model, I could have gotten a better response (I also asked about Caribbean food without
the sandwiches part, and got back what I wanted).

---

## Query Interface

**Sample Input**
Where can I get coffee near UW?

**Sample Output**
According to the provided context, there are a few options to get coffee near UW,
but only one is explicitly mentioned as a cafe.

From the source "EATING THE AVE | https://eatingtheave.com/", Kitanda is mentioned as a cafe
where you can get a Brazilian latte.

Additionally, from the source "Restaurants near University of Washington (TripAdvisor) |
https://www.tripadvisor.com/RestaurantsNear-g60878-d269796-University_of_Washington-Seattle_Washington.html",
Ioula's Offshore Cafe is listed, which may also serve coffee, but it's not explicitly stated.

No other sources mention coffee or cafes explicitly.

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
It was easier to ask Claude for assistance when you had an idea of what you wanted already.
**One way your implementation diverged from the spec, and why:**
I changed them back, but I did diverge from the spec to see if I could get the LLM to answer the carribean sandwiches question, but it didn't work.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- _What I gave the AI:_ I gave AI code snippets from the lab to help with this project, alongside
  the md files for this project.
- _What it produced:_ Claude produced code that worked for my project given my changes because I
  believe I did a good enough job with the md files.
- _What I changed or overrode:_ I didn't have to change much because of the work I did in my md files.

**Instance 2**

- _What I gave the AI:_ The links to the 10 web pages, asking Claude if I could get back th text from them.
- _What it produced:_ 4 of the ten web pages were scraped, and turned into documents named after their source slug.
- _What I changed or overrode:_ I had to make the 6 other files that weren't able to be made given the webpage URLs.
