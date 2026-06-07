# Week 2 — Competency 2: Code literacy & documentation

*Reflection captured through interview (add below sections anytime you want.)*

## What competency 2 means to me

I believe my instructor wants me to **read and write scripts**, **run them**, and **understand what each line is doing**—building practical literacy rather than memorizing syntax for its own sake.

For **documentation**, I’m framing competency 2 around **comments in code** and **context engineering** (giving the right background so tools and collaborators understand intent, constraints, and how to run or extend the work).

## Observations from this week’s work

A small frustration was when **`demo_word_count.py` wouldn’t run** (for example, the CSV path / working-directory issue). Separately, I found it **easy to read and to write short comments above a line of code**—that helped me connect what the script was doing to plain language.

## What I want to get better at next


Something I want to get better at is understanding what each ling of code is doing, as well as when youre running the code, where is it running from. After some frustration in class i was able to figure it wasn't looking in the right place. I also want to get more familiar with cursor and gihub as it a bit intimidating. One problem I am having it when clicking the commit button it doesn't load at github and I have to prompt the agent. 


UPDATE: 
For documentation, I'm framing competency 2 around writing comments
that explain the reasoning behind decisions, not just what the code
is doing. For example, I commented that start=1 in enumerate() is a
deliberate choice so review numbers match natural counting instead of
zero-based indexing. I also explained why the validation check sits
before the loop — so errors are caught before any output prints, not
halfway through. And inside count_words I noted that splitting on
whitespace was a deliberate choice to stay consistent with
demo_word_count.py. These comments show that documentation is most
useful when it captures intent, not just action.