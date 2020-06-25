#PyPoll
#import libraries
import os
import csv

#path to collect data
vote_csv = os.path.join('..','Resources', 'election_data.csv')
election_analysis_output = os.path.join("election_analysis.txt")

#Define initial variables
#Define initial variables
total_votes = 0
winning_votes = 0
list_candidates = []
votes_per_candidates = {}
winner = ""
candidate_name = ""
list_to_export = {}

#read CSV
with open (vote_csv,'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #read header
    header = next(csvreader)

    #loop each line to get values
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in list_candidates:
            list_candidates.append(candidate_name)
            votes_per_candidates[candidate_name] = 0
        
        votes_per_candidates[candidate_name] = votes_per_candidates[candidate_name] +1

#Print to terminal
print("ELECTION RESULTS")
print("------------------------------")
print(f"Total votes: {total_votes}")
print("------------------------------")


for candidate in votes_per_candidates:
    vote = votes_per_candidates.get(candidate)
    percentage = float((float(vote) / float(total_votes))*100)
    if vote > winning_votes :
        winning_votes = vote
        winner = candidate
    #Print to terminal each of te options
    print (f"{candidate}: {round(percentage)}% out of {vote} votes")
    list_to_export[candidate] = (f"{round(percentage)}% out of {vote} votes")

#Print the winner to the terminal   
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")


#extrct results in a file
export = (
    f"\nELECTION RESULTS\n"
    f"----------------------------------\n"
    f"Total votes: {total_votes}\n"
    f"----------------------------------\n"
    f"Results per candidate: {list_to_export}\n"
    f"----------------------------------\n"
    f"Winner: {winner}\n"
)      

with open (election_analysis_output, "w") as analysis_txt:
    analysis_txt.write(export)






