import sys

candidates = []

voters = []

if len(sys.argv) <= 1:
    quit("Please Input Candidate Names")

for i in range(1, len(sys.argv) - 1):
    candidates.append(sys.argv[i])

votersCount = input("Number of voters? ")



for i in range(1, int(votersCount)):
    first = input("Rank 1: ")
    voters.append({"Vote1": first})

    second = input("Rank 2: ")
    voters.append({"Vote2": second})
    
    third = input("Rank 3: ")
    voters.append({"Vote3": third})

# Number of voters who have a candidate over another
C1overC2 = 0
C1overC3 = 0
C2overC1 = 0
C2overC3 = 0
C3overC1 = 0
C3overC2 = 0

for i in range(1, votersCount*3 - 1):
    if voters[i]["Vote2"] == candidates[0]: #Candidate 1 in the middle
        if voters[i - 1]["Vote1"] == candidates[1]: #2 > 1 > 3
            C2overC1 += 1
            C2overC3 += 1
            C1overC3 += 1
        if voters[i - 1]["Vote1"] == candidates[2]: #3 > 1 > 2
            C3overC1 += 1
            C3overC2 += 1
            C1overC2 += 1
    if voters[i]["Vote2"] == candidates[1]: #Candidate 2 in the middle
        if voters[i - 1]["Vote1"] == candidates[0]: #1 > 2 > 3
            C1overC2 += 1
            C1overC3 += 1
            C2overC3 += 1
        if voters[i - 1]["Vote1"] == candidates[2]: #3 > 2 > 1
            C3overC2 += 1
            C3overC1 += 1
            C2overC1 += 1
    if voters[i]["Vote2"] == candidates[2]: #Candidate 3 in the middle
        if voters[i - 1]["Vote1"] == candidates[0]: #1 > 3 > 2
            C1overC3 += 1
            C1overC2 += 1
            C3overC2 += 1
        if voters[i - 1]["Vote1"] == candidates[1]: #2 > 3 > 1
            C2overC3 += 1
            C2overC1 += 1
            C3overC1 += 1 