# Add dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_audit.txt")
# Initialize total vote and total resident voters counters.
total_votes = 0
total_resident_voters = 0
# Candidate options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}
# County options list and county resident dictionary.
county_options = []
county_resident_voters = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Track teh winning county, vote count, and percentage
top_county = ""
top_resident_voter_count = 0
top_resident_voter_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Do the same for county votes
        # Add to the total county voter count
        total_resident_voters += 1
        # Get the county from each row
        county_name = row[1]
        # if the county does not match any existing county, add it to the county list
        if county_name not in county_options:
            # Add the county name to the county list
            county_options.append(county_name)
            # And begin tracking that county's voter count
            county_resident_voters[county_name] = 0
        # Add a vote to the that county's resident voter count
        county_resident_voters[county_name] += 1

# Save the results to the text file.
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
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
    #  Print the county turnouts to terminal
    county_results = (
        f"=========================\n"
        f"\nCounty Results\n"
        f"-------------------------\n"
    )
    print(county_results, end="")
    # save the headding to the text file.
    txt_file.write(county_results)
    for county in county_resident_voters:
        # Retrieve turnout count and percentage.
        turnout = county_resident_voters[county]
        turnout_percentage = float(turnout) / float(total_votes) * 100
        county_results = f"{county}: {turnout_percentage:.1f}% ({turnout:,})\n"

        # Print each county's turnout and precentage of total vote
        print(county_results)
        #  Save the county results results to the text file.
        txt_file.write(county_results)

        # Determine winning turnout count, winning percentage, and winning candidate.
        if (turnout > top_resident_voter_count) and (
            turnout_percentage > top_resident_voter_percentage
        ):
            top_resident_voter_count = turnout
            top_county = county
            top_resident_voter_percentage = turnout_percentage
    # Print the winning county's results to the terminal.
    Winning_County_summary = (
        f"-------------------------\n"
        f"Highest County Turnout: {top_county}\n"
        f"Voter Count: {top_resident_voter_count:,}\n"
        f"County Percentage of total votes cast: {top_resident_voter_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(Winning_County_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(Winning_County_summary)
