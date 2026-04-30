# Week 3 Competency Claim



## Claim
This week I demonstrated that I can load messy CSV data in Python, use error messages to diagnose failures, and refactor the code so it runs reliably and produces consistent outputs. 

I was able to use the agent to help explain what the error was to me and what would be the best next steps. When the output was "Fixed error: ValueError invalid literal" I was able to understadn that the there was number that was an invalid intger typed as 'fifteen'. To fix that I converted  experience_years with try/except, and skip rows that aren't numeric. 

ADDED:
 The second bug was a logic error in the ranking. The top 5 satisfaction scores were being sorted low to high, which meant the slice [:5] was grabbing the five lowest scores instead of the five highest. So the "top 5" results were actually the bottom 5. The fix was adding reverse=True to the sort so the list goes high to low first, and [:5] correctly pulls the top five

