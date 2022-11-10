# Election_Analysis
Module3

## Project Overview
Co-worker Tom assigned a project to complete the election audit of a recent local congressional election. The analysis will determine the county with the most votes and the winner of the election. Python and Visual Studio Code were used to perform this analysis. The full analysis is below as well as printed in the election_results.txt file.

## Election-Audit Results:
- There were 369,711 total votes cast in the election
- Votes were broken down by each county in the precinct using `for` and `if` statements in Python. The county restults are shown below:

  ![County_Votes](https://user-images.githubusercontent.com/114450503/200968319-24af45bd-58b5-4a5f-bbe7-868572cf96a0.png)
- Denver had the largest number of votes

- The candidates and their respective votes were also determined using `for` and `if` statements, their results are shown below:

  ![Votes_by_candidate](https://user-images.githubusercontent.com/114450503/200968172-4fe1afd8-50c4-47d3-a12f-04f30565ed56.png)
- The Winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 votes
  
## Election-Audit Summary
The code used to produce this analysis could easily be scaled to larger elections and more detailed data sources. If the raw data included states instead of (or in addition to) counties, the votes per state could be calculated using the same method as votes per county. Similar calculations could be used if any demographic information was provided in the raw data, such as age, declared party, or salary range of the voters.

The code could also be modified to include more in-depth analysis such as majority winner of the votes as well as the winner by total count. 
