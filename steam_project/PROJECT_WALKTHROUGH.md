# Explaining the project

## Short description

I analyzed Steam pricing and review patterns using Python, SQLite and Power BI. I compared average positive-review proportions across price bands, genre groups and free versus paid titles. I also checked whether results changed with stricter review-count thresholds. The results describe patterns in the selected data; they do not show that changing price causes better reviews.

Use this description after reviewing and running the revised work yourself.

## What happens in the workflow?

1. The original preparation selected records with at least 50 reviews, calculated positive-review proportions, and separated free from paid titles. Paid analysis also excluded missing genres and prices above $70. The original raw input still needs to be sourced and documented.
2. The revised Python notebook starts from the provided extracts, validates them, then summarizes scores and group sizes. It also checks stricter review thresholds and all-genre memberships.
3. The SQL notebook loads the prepared paid rows into SQLite and runs four queries.
4. Power BI uses the CSV extracts for charts, cards and filters. It is a separate reporting branch; it does not currently read directly from SQLite.

## Understand the new SQL

The `grouped` CTE creates one row per price-band/first-listed-genre combination, calculates its count and mean score, and keeps groups with at least 100 records. The outer query uses DENSE_RANK, partitioned by price band, to rank the genre groups inside each band. Equal unrounded scores receive the same rank.

The 100-record rule is a practical inclusion threshold, not proof that a comparison is statistically significant. No join is needed for this single-table question.

## Questions to prepare for

- Why average title-level scores rather than pool all reviews? The question compares typical records, so each gets equal weight. Pooling would let heavily reviewed titles dominate and would answer a different question.
- Why 50 reviews? It excludes extremely sparse review histories, but remains a choice. The new sensitivity table checks 200 and 1,000 as alternatives.
- Why a $70 cap? It defines the chosen scope; it is not a reliable game/software classifier.
- Does price cause higher scores? No. Snapshot prices, discounts, release age, audience and other factors prevent that conclusion.
- Is first-listed genre the main genre? Not necessarily. Many lists are alphabetically ordered. The all-genre analysis is a useful alternative, but its groups overlap.
- Why didn't you remove duplicate names? Different apps can share names. AppID is required to make a defensible identity-based decision.

## Before claiming new skills

The sensitivity checks, validations and fourth SQL query were added during an assistant-supported review. Explain and modify them yourself before presenting them as independent proficiency. Keep the original project work and later improvements distinct when asked.
