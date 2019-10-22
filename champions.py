import sys
import pandas as pd

columns = ["Country", "Club", "Titles"]

euroChampions = [
    ["Spain",       "Real Madrid",      13],
    ["Italy",       "AC Milan",      7],
    ["England",     "Liverpool",    6],
    ["Germany",     "Bayern Munich",    5],
    ["Spain",       "Barcelona",      5],
    ["Holland",     "Ajax Amsterdam",    4],
    ["Italy",       "Inter Milan",      3],
    ["England",     "Manchester United",    3],
    ["Italy",       "Juventus",      2],
    ["Portugal",    "Benfica",   2],
    ["England",     "Nottingham Forest",    2],
    ["Portugal",    "Porto",   2],
    ["Scotland",    "Celtic",   1],
    ["Holland",     "Feyenoord",    1],
    ["England",     "Aston Villa",    1],
    ["Holland",     "PSV Eindhoven",    1],
    ["Yugoslavia",  "Red Star Belgrade", 1],
    ["Germany",     "Hamburg",    1],
    ["Romania",     "Steaua Bucharest",    1],
    ["France",      "Marseille",     1],
    ["Germany",     "Borussia Dortmund",    1],
    ["England",     "Chelsea",    1]
]

df = pd.DataFrame(data = euroChampions, columns = columns)

print(df)
print()

print("Number of European champions per country:")
print(df.groupby(["Country"]).size())
print()

print("Total number of titles per country:")
print(df.groupby(["Country"]).sum())
print()

print("Average size of each trophy haul by country:")
print(df.groupby(["Country"]).mean())

sys.exit(0)
