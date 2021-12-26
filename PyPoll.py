# Add our dependencies
import csv
import os

# Assign a variable to load the file from a path (this is indirect path).
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path (this is indirect path).
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load, "r") as election_data: 

    # Read the file object with the reader function located within csv module. 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the csv file.
    for row in file_reader: 
        print(row)

# Analyze the data here: 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Write the results to a text file to be sent to the election commission

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Write 3 counties to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
