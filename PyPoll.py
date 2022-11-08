# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")


#1. Initialize a total vote counter
total_votes = 0

#3a. Declare a new list called "candidate_options" to get the distinct candidate names
candidate_options = []

#4. Declare the empty dictionary
candidate_votes = {}

#6a. Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Read and Print the header row OR skip the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

    #3b. Print the candidate name from each row
        candidate_name=row[2]

    #3c. Add the candidate name to the candidate_options list
        #candidate_options.append(candidate_name)

    #3d. If the candidate does not match any existing candidate in the candidate_options list
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            #4a. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        #4c. Add a vote for each row belonging to that candidate
        candidate_votes[candidate_name] += 1


#9. write the election results to a .txt file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)


    #5Determine the percentage of votes for each candidate by looping through the counts

    #5a.Iterate through the candidate list
    for candidate_name in candidate_votes:
        #5b.retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #5c.calculate the percentage of votes
        vote_percentage = (float(votes) / float(total_votes) * 100)
        
        #5d.print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}, {vote_percentage:.1f}%, ({votes:,})\n")
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)
        #7 Print out each candidate's name, vote count, and % of votes to the terminal
        #print(f"{candidate_name}, {vote_percentage:.1f}%, ({votes:,})\n")

        #6 Determine winning vote count and candidate
        #6b.Determine if the votes are greater than the winning count
        if(votes> winning_count) and (vote_percentage > winning_percentage):
                #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
                #and set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name


    # 3. Print the total votes
    #print(total_votes)

    #3d. Print the candidate_options list
    #print(candidate_options)

    #4b. Print the candidate vote dictionary
    #print(candidate_votes)
        
    #8. Print out the winning candidate summary
    #8a. set up the format for printing
    winning_candidate_summary = (
        f"------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------------\n")

        #8b set print command for winning summary
    print(winning_candidate_summary)
        #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)


