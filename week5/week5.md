Week 5 Comptency claim:
C5 — Data Analysis with Pandas



I was able to load the data from Seattle's Business license dataset from the city's open portal API. There were 50,000 rows in the json and it filterted down to 309 Seattle coffee shops by matching trade manes that had the words coffee,cafe, and espresso. I used the df.head() and df.info() operations to preview the raw data structure and the df.isnull().sum() operation to check for the missing values. 

Using the operation groupby() I found that the Zip code  98122 (cap hill) had the more coffee licenses with 30, and the second runner was downtown seattle 98101. I was expecting to see Capitol hill as the number one runner since I know many coffee shops in that area, and with recent marketing on Tiktok I've seen so many new coffee shops opening in the Cap hill area.  

Also with the operation groupby() on the license start data I found that new coffee shops openings were low through the 2000's and then it jumped to 22 in 2018, and then dropped down to 13 in 2020, most likey due to the COVID pandemic which makes sense. After that the opening jumped up to 30 in 2023. 

 The value_counts operation on the trade names to help classify which were chain and independent, any name that appereard more than once was flagged as a chain. And out of the 309 total locations 253 of them had a unique name to it, suggesting it was an independent owned which is 81.9%. Only 56 of the locations were chain locations which was 18.1%. This kinda makes sense to me, considering how many Starbucks coffee shops have been shut down near me, due to union issues or whatever reasons but this wasn't as shocking to me. 