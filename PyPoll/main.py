#import modules required for the analyis
import os
import csv

#assingning the absolute path of the csv file for data retrieval
csvpath = os.path.abspath("/Users/srinivasjayaram1987/Downloads/Starter_Code/PyPoll/Resources/election_data.csv")

#initializing the total votes variable as 0, this will store the total votes in the election.
total_votes = 0

#code to open and read the file and retrieve the total now
with open(csvpath,'r') as PyPollfile:
    PyPollreader = csv.reader(PyPollfile)

    Header_row = next(PyPollreader) # Assign the first row of the dataset to a variable header row and skips this row 

    data = [row for row in PyPollreader]

    #retrieve the total number of votes casted in the polls
    total_votes = len(data)   
    
    #creates a set called candidates, by iterating through each row in the data list and retrieving the candidate's name. By using a dictionary we are ensuring that only unique candidate names are included in the candidates set.
    candidates = set([row[2] for row in data])
    
    # Initialize a dictionary to store the number of votes for each candidate and inititate it to 0
    votes_per_candidate = {candidate:0 for candidate in candidates}

    # Using a for loop to calculate the Count the number of votes for each candidate
    for row in data:
        candidate = row[2]
        votes_per_candidate[candidate]+= 1

    # Initialize a dictionary to store the percentage of votes for each candidate
    percentages_per_candidate = {}

    # Calculate the percentage of votes for each candidate and store it in the dictionary
    for candidate, votes in votes_per_candidate.items():
        percentage = (votes / total_votes) * 100
        percentages_per_candidate[candidate] = percentage

    # Find the winner of the election based on popular vote where the key value i.e name is retrieved for 
    winner = max(votes_per_candidate, key=votes_per_candidate.get)

    # Print the analysis results in the format desired
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in votes_per_candidate.items():
        percentage = round(percentages_per_candidate[candidate], 3)
        print(f"{candidate}: {percentage}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Open a file for writing the results as a text file
with open("election_results.txt", "w") as file:

    # Write the header information into the text file in the desired format
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    # Write the results for each candidate into the text file in the desired format
    for candidate, votes in votes_per_candidate.items():
        percentage = round(percentages_per_candidate[candidate], 3)
        file.write(f"{candidate}: {percentage}% ({votes})\n")

    # Write the election winner information to text file in the desired format
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
