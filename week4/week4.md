Competency Claim: C4 


This week, I called the TVMaze Schedule API, which is a public API that does not require a key or authentication. I looked through the TVMaze API documentation at tvmaze.com/api to understand what the schedule endpoint does and what it returns. The endpoint takes a date query parameter and returns a list of every episode that aired on that date, with details like the show name, episode name, and airdate.

I chose the date 2001-09-17 because it is my birthday, and I was curious what shows were on the day I was born. Since TVMaze does not have a single category field, the script combines the show's type and genre into one readable label for example Scripted Drama Crime. The script goes through the results, prints each show's category, and saves everything to a CSV file.

Evidence in my repo: the script is week4/shows_on_mybday.py, and the main output is week4/shows_on_mybday_2001-09-17.csv.

TVMaze did not require an API key. A .env file and .gitignore were set up in week4/ anyway, because if an API key had been needed, that would be the correct way to keep it out of a public repository.


