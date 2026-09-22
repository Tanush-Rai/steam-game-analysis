# Original raw-data preparation reference
# Requires the missing games.csv. Not executed or independently verified in this revision.
# The supplied file used a manual 40-column header repair. Confirm that schema
# against the actual source before running. See README for source/ID limitations.

import pandas as pd
import matplotlib.pyplot as plt

# header merges Discount + DLC count, shifting everything - name cols manually
column_names = [
    "AppID","Name","Release date","Estimated owners","Peak CCU","Required age",
    "Price","Discount","DLC count","About the game","Supported languages",
    "Full audio languages","Reviews","Header image","Website","Support url",
    "Support email","Windows","Mac","Linux","Metacritic score","Metacritic url",
    "User score","Positive","Negative","Score rank","Achievements","Recommendations",
    "Notes","Average playtime forever","Average playtime two weeks",
    "Median playtime forever","Median playtime two weeks","Developers","Publishers",
    "Categories","Genres","Tags","Screenshots","Movies"
]

games = pd.read_csv("games.csv", index_col=False, header=0, names=column_names)
games = games[["Name","Release date","Estimated owners","Peak CCU",
               "Price","Positive","Negative","Metacritic score","Genres"]]
games.head()

# 50+ reviews so the score isn't noise
games["total_reviews"] = games["Positive"] + games["Negative"]

reviewed = games[games["total_reviews"] >= 50].copy()
reviewed["review_score"] = reviewed["Positive"] / reviewed["total_reviews"]

print("Games before filter:", len(games))
print("Games with 50+ reviews:", len(reviewed))
print("Percentage kept:", round(len(reviewed) / len(games) * 100, 1), "%")

reviewed[["Name", "Price", "total_reviews", "review_score", "Genres"]].head()

# pricing is the focus, so split free out
paid = reviewed[reviewed["Price"] > 0].copy()
free = reviewed[reviewed["Price"] == 0].copy()

print("Paid games:", len(paid))
print("Free games:", len(free))

paid = paid[paid["Genres"].notna()]
print("Paid games with a genre:", len(paid))

print("\nPaid game price stats:")
print(paid["Price"].describe())

# Restrict the analysis to paid titles priced no more than $70.
# This is a scope choice, not a validated software/game classification.
paid = paid[paid["Price"] <= 70].copy()
print("Paid games priced $70 or less:", len(paid))

def price_band(price):
    if price < 5:
        return "Under $5"
    elif price < 10:
        return "$5-10"
    elif price < 20:
        return "$10-20"
    elif price < 30:
        return "$20-30"
    elif price < 40:
        return "$30-40"
    else:
        return "$40-70"

paid["price_band"] = paid["Price"].apply(price_band)

print("\nGames per price band:")
print(paid["price_band"].value_counts())

paid.to_csv("games_clean.csv", index=False)
print("Saved", len(paid), "games to games_clean.csv")
