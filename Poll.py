import pandas as pd
import statistics as stats
a = pd.read_csv('/Users/alexandergoldstein/Downloads/03-Python_Homework_PyPoll_Resources_election_data.csv')

d = a.rename(columns={"Voter ID" : "Votes Cast"})
#print(d)

b = d['Votes Cast'].count() #returns total votes cast

c = d['Candidate'].unique()
#returns each candidate who received votes

e = d['Candidate'].value_counts(normalize=True) * 100
#returns percentage of the vote received by each candidate

f = d['Candidate'].value_counts()
#returns total votes received by each candidate

g = stats.mode(d['Candidate'])
#returns candidate who received the most votes

with open("Poll.txt", "w") as text_file:
    print(f"Total votes cast: {b}", file=text_file)
    print(f"List of candidates: {c}", file=text_file)
    print(f"Percentage of the vote received by each candidate: {e}", file=text_file)
    print(f"Total votes received by each candidate: {f}", file=text_file)
    print(f"Winner: {g}", file=text_file)


 