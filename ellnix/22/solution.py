import os

dirname = os.path.dirname(os.path.realpath(__file__))
score = 0
with open(f"{dirname}/0022_names.txt") as names_file:
    names = names_file.read().split(",")
    names.sort()

    for idx, name in enumerate(names):
        score += (idx+1) * sum(ord(char)-64 for char in name.strip('"'))

print(score)
