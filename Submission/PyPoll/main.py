# this is the main document that will be used for this assignment

# Work should match the following information:
    # Election Results
    # Total Votes: 369711
    # Charles Casper Stockham: 23.049% (85213)
    # Diana DeGette: 73.812% (272892)
    # Raymon Anthony Doane: 3.139% (11606)

    # Winner: Diana DeGette

# Step 1: Import the results

import os
import csv

with open('analysis/pypoll_analysis', 'w') as file:
    pass
    # Step 2: Establish the path

    csvpath = "resources/election_data.csv"

    # Step 3: Open the CSV using the UTF-8 encoding - Cookie Cutter Code almost always used as is 
    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

    # Step 3A: Skip the header
        csv_header = next(csvreader)

    # Step 4: Understand the header and the way the script interacts with the data
        # Ballot ID is column [0], County is column [1], Candidate is column [2]

    # Step 5A: Establish the lists that will ultimately house our data, also establishes that the different ballot_counts to have a baseline of 0.

        
        # Both of these characteristics are saying effectively same thing, but different logic requires lists vs counts.
        total_vote = []
        total = 0

        county_vote = [] # Not actually used for this assignment, but the logic has aleady been established, if further information based on county needs to be added at a later point 
        
        # Each candidate's vote count starting point

        charles = 0
        diana = 0
        raymon = 0

        # Step 5B: Establish what value corresponds to what column from the data set. Add months and profit to separate lists for each row of the data set.

        for row in csvreader: # for each row in the file
                
                vote = (row [0]) # assigning the variable "vote" to column "0" / ballot ID for the data set

                total_vote.append(vote) # adding each vote to a list called "total_vote"
                total = total + 1 # adding each vote together (effectively does the same thing as above line) 

                county = (row [1]) # assigning the variable "county" to column "1" / county for the data set
                county_vote.append(county) # adds each vote's county to a list for counties.
                
               
               # Individual vote counts based on what was in the "candidate" column
               
                candidate = (row [2])
                if candidate == "Charles Casper Stockham":
                    charles = charles + 1
                elif candidate == ("Diana DeGette"):
                    diana = diana + 1
                else: 
                    raymon = raymon + 1

        charles_perc = (round(((charles / total)*100),3))
        diana_perc = (round(((diana / total)*100),3))
        raymon_perc = (round(((raymon / total)*100),3))

        print(f"There were", len(total_vote), "total votes cast in this election.")
        print(f"Charles Casper Stockham received", charles_perc,"% of the vote, or", charles, "votes")
        print(f"Diana DeGette received", diana_perc,"% of the vote, or",  diana, "votes")
        print(f"Raymon Anthony Doane received", raymon_perc,"% of the vote, or", raymon, "votes")

     # Establish who the winner of the election is
     
        if charles > diana and charles > raymon:
            print("Charles Casper Stockham is the winner of the election!")
        elif diana > charles and diana > raymon:
            print("Diana DeGette is the winner of the election!")
        elif raymon > diana and raymon > charles:
            print("Raymond Anthony Doane is the winner of the election!")
        else:
            print("The winner of the election could not be determined and will require further review.")

    # Print all the findings to a text document

    file.write(f'There were 369,711 votes cast in the most recent election.\n')
    file.write(f'Charles Casper Stockham received 23.049 % of the vote, or 85213 votes.\n')
    file.write(f'Diana DeGette received 73.812 % of the vote, or 272892 votes.\n')
    file.write(f'Raymon Anthony Doane received 3.139 % of the vote, or 11606 votes.\n')
