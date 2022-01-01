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

# County with Highest Voter Turnout
highest_voter_county = ""
highest_county_votes = 0
highest_county_percentage = 0

# Winning Candidate & Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Initialize voting_county variable as list
voting_counties = []

# Declare dictionary for county names + vote count incremented by 1
county_votes = {}

# Open the election results and read the file.
# Realize that I don't need the "r" below since it's default, but including to clarify for me
with open(file_to_load) as election_data: 

    # Read the file object with the reader function located within csv module. 
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # For loop 
    for row in file_reader: 
        # Add to total vote count (i.e. increment total_votes + 1 using Standard Python format)
        total_votes += 1
        # Get the candidate's name from each row using index aka 3rd column, Index 2
        candidate_name = row[2]
        # Get the county name from each row using index aka 2nd column, Index 1
        county_name = row[1]
        # If the candidate does not match any existing candidate. . . 
        if candidate_name not in candidate_options:            
            # Add the candidate name to the candidate_options list
            candidate_options.append(candidate_name)
            # And begin tracking each candidate's voter count. Set initial vote count to 0 for each candidate.
            candidate_votes[candidate_name] = 0
        # Add a vote to applicable candidate's count
        candidate_votes[candidate_name] += 1 
        # If the county does  not match any existing candidate. . . 
        if county_name not in voting_counties:
            # Add the county name to the the voting_counties list
            voting_counties.append(county_name)
            # And begin tracking each county's voter count. Set initial vote count to 0 for each county.
            county_votes[county_name] = 0
        # Add a vote to the applicable county's count
        county_votes[county_name] += 1 

# Save the results to our text file
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal. 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
            
    # Determine percentage of votes from each county out of the total count by looping through the counts
    # Need to initiate for loop b/c votes are values of each county_name in the county_votes dictionary
    # Iterate through the voting_counties dictionary:
    for county_name in voting_counties:
        # Retrieve the vote count from a county from the voting_counties = {} dictionary
        county_vote_count = county_votes[county_name]
        # Calculate % of votes - must convert votes & total_votes to floating-point decimal numbers
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100
        # Print each county name, associated percentage of votes, & vote count):
        county_summary = (f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_summary)
        
        # Save the candidate results to our text file
        txt_file.write(county_summary) 

        # Determine county with highest voter turnout
        # Determine if highest_county_votes > county_votes
        if (county_vote_count > highest_county_votes) and (county_vote_percentage > highest_county_percentage):
            # If true, set highest_county_votes = county_votes and highest_county_percentage = county_vote_percent
            highest_county_votes = county_vote_count
            highest_county_percentage = county_vote_percentage
            # Set the county with the highest voter turnout = county_name
            highest_voter_county = county_name

    # Print Highest Voter Turnout summary
    highest_voter_turnout_summary = (
        f"-------------------------\n"
        f"County with Highest Voter Turnout: {highest_voter_county}\n"
        f"County Vote Count: {highest_county_votes:,}\n"
        f"County Vote Percentage: {highest_county_percentage:.1f}%\n"
        f"-------------------------\n"
    )

    print(highest_voter_turnout_summary)

    # Save the highest voter turnout summary to the text file: 
    txt_file.write(highest_voter_turnout_summary)
     
    # Determine percentage of votes each candidate won by looping through the counts
    # Need to initiate for loop b/c votes are values of each candidate_name in the candidate_votes dictionary
    # Iterate through the candidate list:
    for candidate_name in candidate_votes:
        # Retrieve the vote count of a candidate from the candidate_votes = {} dictionary
        votes = candidate_votes[candidate_name]
        # Calculate % of votes - must convert votes & total_votes to floating-point decimal numbers
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate name, associated percentage of votes, & vote count):
        candidate_summary = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_summary)
        
        # Save the candidate results to our text file
        txt_file.write(candidate_summary)
    
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

    # Save the winning candidate summary to the text file:
    txt_file.write(winning_candidate_summary)