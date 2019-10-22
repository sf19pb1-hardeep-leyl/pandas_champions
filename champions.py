import sys
import pandas as pd

columns = ["Country", "Club", "Titles"]

massMurders = [
    ["Spain",             "Real Madrid",      13],
    ["Italy",                "AC Milan",      7],
    ["England",               "Liverpool",    6],
    ["Germany",           "Bayern Munich",    5],
    ["Holland",       "Ajax Amsterdam",    4],
    ["Italy",         "Inter Milan",      3],
    ["England",       "Manchester United",    3],
    ["Italy",         "Juventus",      2],
    ["Portugal",      "Benfica",   2],
    ["England",       "Nottingham Forest",    2],
    ["Portugal",      "Porto",   2],
    ["Scotland",      "Celtic",   1],
    ["Holland",       "Feyenoord",    1],
    ["Aston Villa",   "England",    1],
    ["Holland",       "PSV Eindhoven",    1],
    ["Yugoslavia",    "Red Star Belgrade", 1],
    ["Germany",       "Yugoslavia",    1],
    ["Romania",       "Steaua Bucharest",    1],
    ["France",        "Marseille",     1],
    ["Germany",       "Borussia Dortmund",    1],
    ["England",       "Chelsea",    1]
]

df = pd.DataFrame(data = massMurders, columns = columns)

print(df)
print()

print("Number of titles in each country, broken down by club:")
print(df.groupby(["Country", "Club"]).size())
print()

print("Total number of titles on each country:")
print(df.groupby(["Country", "Club"]).sum())
print()

print("Number of titles in each club's biggest mass murder:")
print(df.groupby(["Country", "Club"]).max())   #or min
print()

print("Average size of each trophy haul:")
print(df.groupby(["Country", "Club"]).mean())

sys.exit(0)
