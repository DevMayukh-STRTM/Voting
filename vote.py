#this will simulate voting by simple means

#let's start by creating parties:

from random import randint
nrk = 0
parties = ["A", "B", "C", "D", "E"]

#let's create 243 voting seats with some ammount of voters
total = 0
boxes = []
new_boxes = []
seats = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0
}

poles = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0
}

def winner():
    a = poles["A"]
    b = poles["B"]
    c = poles["C"]
    d = poles["D"]
    e = poles["E"]

    k = max(a, b, c, d, e)

    if k == a:
        return f"A with {seats['A']} votes and {poles['A']} seats"
    if k == b:
        return f"B with {seats['B']} votes and {poles['B']} seats"
    if k == c:
        return f"C with {seats['C']} votes and {poles['C']} seats"
    if k == d:
        return f"D with {seats['D']} votes and {poles['D']} seats"
    if k == e:
        return f"E with {seats['E']} votes and {poles['E']} seats"

"""
    It will be a json:
    {
        0: voter_count
        "A": votes,
        "B": votes,
        "C": votes,
        "D": votes,
        "E": votes
    }
"""
#will create the boxes

for x in range(2000):
    boxes.append(
        {
            0: randint(95000, 100000),
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0
        }
    )

for y in boxes:
    total += y[0]

#Now let's start the voting:
"""
Rules:
select from 1 - 5
if 1, vote A
if 2,  vote B and so on


"""

for votes in boxes:
    for n in range(votes[0]):
        nl = randint(1, 5)
        if nl == 1:
            votes["A"] += 1
            nrk += 1
            print(f"A got a vote, {nrk}/{total}")
        elif nl == 2:
            nrk += 1
            votes["B"] += 1
            print(f"B got a vote, {nrk}/{total}")
        elif nl == 3:
            nrk += 1
            votes["C"] += 1
            print(f"C got a vote, {nrk}/{total}")
        elif nl == 4:
            nrk += 1
            votes["D"] += 1
            print(f"D got a vote, {nrk}/{total}")
        elif nl == 5:
            nrk += 1
            votes["E"] += 1
            print(f"E got a vote, {nrk}/{total}")
    new_boxes.append(votes)
print("Voting Complete, Calculating Results")

for que in new_boxes:
    seats["A"] += que["A"]
    seats["B"] += que["B"]
    seats["C"] += que["C"]
    seats["D"] += que["D"]
    seats["E"] += que["E"]

for lque in new_boxes:
    a = lque["A"]
    b = lque["B"]
    c = lque["C"]
    d = lque["D"]
    e = lque["E"]

    k = max(a, b, c, d, e)
    if k == a:
        poles["A"] += 1
    if k == b:
        poles["B"] += 1
    if k == c:
        poles["C"] += 1
    if k == d:
        poles["D"] += 1
    if k == e:
        poles["E"] += 1

boxes = None

print(f"Total Voters: {total}, Total Seats: 243\nA: {seats['A']}, {poles['A']}\nB: {seats['B']}, {poles['B']}\nC: {seats['C']}, {poles['C']}\nD: {seats['D']}, {poles['D']}\nE: {seats['E']}, {poles['E']}\nWinner: {winner()}")

#now let's see the winners:
