# What Makes a Steam Game Well-Reviewed?

An analysis of ~26,000 Steam games looking at whether **price** and **genre** affect a game's review score — and, more importantly, whether the patterns hold up once you dig into them.

Data comes from the [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) (~126,000 games), scraped from the Steam API.

## The question

Is there a price "sweet spot" where games are best reviewed? And if there is, is it really about price — or is it just that certain genres cluster at certain prices?

## How success was measured

Review score = positive reviews / total reviews, counting only games with at least 50 reviews so the score actually means something (a game with 2 reviews showing 100% positive isn't meaningful). After filtering to paid games with a genre and a sensible price range ($0.49–$70), this left about 26,000 games.

## What the data showed

**There's a real mid-price sweet spot.** Games priced $5–10 have the highest average review score (~82%). The cheapest games (under $5) score worst (~78%), and scores decline again toward the high end (~75% for $40–70).

**The sweet spot survives the honest test.** Since different genres sit at different prices, the pattern could just be genre in disguise. Running the same analysis on Action games only (the most common genre) still showed the mid-price peak — so it's genuinely about price, not just genre mix. The decline at the very high end is less certain, since there are few expensive games and their samples are small.

**Popular games score better, and paid beats free.** The more reviews a game has, the higher its average score — for both free and paid games. Paid games score higher than free at every popularity level, and the gap widens among the most-reviewed games.

**By genre, Adventure and Casual review best; Simulation and Racing review worst.** Action is the most common genre (11,000+ games) but sits near the bottom — the most-produced genre isn't the best-received.

## Honest limitations

- The data leans heavily toward cheaper indie games; true AAA titles are a small slice, so the findings are really about the indie-to-mid-tier market.
- The most expensive price bands have small sample sizes, so those numbers are less reliable.
- The raw file had a column-alignment bug in the header (two columns merged into one), which had to be caught and fixed before any analysis — a reminder to sanity-check data against known values.

## What's in this repo

- `steam_analysis.ipynb` — the full Python analysis (cleaning, the sweet-spot finding, the honest test, free-vs-paid, genre ranking)
- `sql_analysis.ipynb` / `queries.sql` — the core questions answered in SQL
- `steam_project_dashboard.pbix` — an interactive Power BI dashboard (price, genre, and free-vs-paid charts with filters)
- `dashboard.png` — a screenshot of the dashboard
- `games_clean.csv` — the cleaned dataset used for the analysis

## Tools

Python (pandas, matplotlib), SQL (SQLite), Power BI.
