# Add our dependencies
import csv
import os

# Assign a variable to load the file from a path (this is indirect path).
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path (this is indirect path).
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total_votes accumulator variable set to 0 that will increment by 1 as we read each row in for loop
total_votes = 0

# Initialize new Candidate Options variable as list
candidate_options = []

# Declare dictionary for candidate names + vote count incremented by 1
candidate_votes = {}

# Winning Candidate & Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
# Realize that I don't need the "r" below since it's default, but including to clarify for me
with open(file_to_load) as election_data: 

    # Read the file object with the reader function located within csv module. 
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # For loop 
    for row in file_reader: 
         # Add to total vote count / increment total_votes + 1 using Standard Python format
        total_votes += 1
        # Get the candidate's name from the row using index aka 3rd column, Index 2
        candidate_name = row[2]
        #If the candidate does not match any existing candidate. . . 
        if candidate_name not in candidate_options:            
            # Add the candidate name to the candidate_options list
            candidate_options.append(candidate_name)
            # Begin tracking each candidate's vote count / set initial vote count to 0 for each candidate
            candidate_votes[candidate_name] = 0
        # Add a vote to applicable candidate's count
        candidate_votes[candidate_name] += 1 

# Print total_votes cast in election:
print(f"Total Votes Cast: {total_votes:,}")

# Print candidate_options list:
print(f"Candidate Options: {candidate_options}")

# Print the candidate_votes dictionary:
print(candidate_votes)
        
# Determine percentage of votes each candidate won by looping through the counts
# Need to initiate for loop b/c votes are values of each candidate_name in the candidate_votes dictionary
# Iterate through the candidate list:
for candidate_name in candidate_votes:
    # Retrieve the vote count of a candidate from the candidate_votes = {} dictionary
    votes = candidate_votes[candidate_name]
    # Calculate % of votes - must convert votes & total_votes to floating-point decimal numbers
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print each candidate name & associated percentage of votes:
    candidate_summary = (
        f"-------------------------\n"
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        )
    print(candidate_summary)
   
    # Determine winning vote count and candidate
    # Determine if vote count > winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage): 
        # If true, set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes 
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
        
# Print the winning candidate summary:  
winning_candidate_summary = (
    f"-------------------------\n"
    f"Election Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,} votes\n"
    f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)

print(winning_candidate_summary)

# Write the results to a text file to be sent to the election commission
# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
