import sys
import pandas as pd

columns = ["Club", "Country", "Titles"]

massMurders = [
    ["Real Madrid",             "Spain",      13],
    ["AC Milan",                "Italy",      7],
    ["Liverpool",               "England",    6],
    ["Bayern Munich",           "Germany",    5],
    ["Ajax Amsterdam",          "Holland",    4],
    ["Inter Milan",             "Italy",      3],
    ["Manchester United",       "England",    3],
    ["Juventus",                "Italy",      2],
    ["Benfica",                 "Portugal",   2],
    ["Nottingham Forest",       "England",    2],
    ["Porto",                   "Portugal",   2],
    ["Celtic",                  "Scotland",   1],
    ["Feyenoord",               "Holland",    1],
    ["Aston Villa",             "England",    1],
    ["PSV Eindhoven",           "Holland",    1],
    ["Red Star Belgrade",       "Yugoslavia", 1],
    ["Hamburg",                 "Germany",    1],
    ["Steaua Bucharest",        "Romania",    1],
    ["Marseille",               "France",     1],
    ["Borussia Dortmund",       "Germany",    1],
    ["Chelsea",                 "England",    1]
]

df = pd.DataFrame(data = massMurders, columns = columns)

print(df)
print()

print("Number of mass murders in each club, broken down by country:")
print(df.groupby(["Club", "Country"]).size())
print()

print("Total number of titles on each country:")
print(df.groupby(["Club", "Country"]).sum())
print()

print("Number of titles in each club's biggest mass murder:")
print(df.groupby(["Club", "Country"]).max())   #or min
print()

print("Average size of each trophy haul:")
print(df.groupby(["Club", "Country"]).mean())

sys.exit(0)
