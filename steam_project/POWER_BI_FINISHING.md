# Power BI finishing steps

The included PBIX is unchanged. Its report configuration was inspected, but it has not been opened, refreshed or visually tested in Power BI Desktop as part of this revision. Save after each change and check the results below.

## 1. Repoint the two CSV sources

Open Transform data and inspect the Source step for `games_clean` and `free_vs_paid`. Update paths to the two CSVs in this folder. Refresh and confirm 26,471 paid records and 30,533 comparison records. The original `games_clean.csv` does not contain `main_genre`; preserve the report's existing transformation that creates it, or add a column extracting the text before the first comma from Genres.

## 2. Use precise titles

Change the report title to `Steam pricing and review patterns`.
Change `Main genre` labels to `First-listed genre` without renaming the underlying column if that would break visuals.
Change the line-chart title to `Average positive-review share by review count`.
Add a small note: `50+ reviews. Paid sample: price > 0 and <= $70, genre present. Groups describe associations, not causal effects. First-listed genre is a proxy. Free/paid comparison uses different selection rules.`

## 3. Sort categories explicitly

Add calculated columns in the appropriate tables. These expressions are provided for Desktop entry and have not been executed here.

```dax
Price Band Order =
SWITCH(games_clean[price_band],
    "Under $5", 1,
    "$5-10", 2,
    "$10-20", 3,
    "$20-30", 4,
    "$30-40", 5,
    "$40-70", 6,
    BLANK()
)
```

Select `games_clean[price_band]`, choose Sort by column, then Price Band Order. Set the chart to ascending category order.

```dax
Review Bucket Order =
SWITCH(free_vs_paid[review_bucket],
    "50-200", 1,
    "200-1k", 2,
    "1k-10k", 3,
    "10k+", 4,
    BLANK()
)
```

Select `free_vs_paid[review_bucket]`, choose Sort by column, then Review Bucket Order. On the line chart, sort ascending by review_bucket, not average review_score.

## 4. Make the genre rule match Python and SQL

Create measures in games_clean:

```dax
Game Records = COUNTROWS(games_clean)

Mean Positive Review Share = AVERAGE(games_clean[review_score])

Mean Price = AVERAGE(games_clean[Price])
```

Enter these as three separate measures. Format the review measure as a percentage. Use Game Records for the record-count card and as a chart tooltip. This counts rows, not verified unique AppIDs.

On the genre chart remove the Top N filter. Add Game Records to visual-level filters and require it to be >= 100. Sort by Mean Positive Review Share descending. This rule updates with the current slicer context and may return fewer genres after filtering.

## 5. Make the comparison chart's scope clear

The free_vs_paid export lacks Name, AppID, price and genre. Do not create a relationship on review_score or total_reviews: those are not unique identifiers.

For this version, keep the free/paid chart as an independent whole-sample comparison. Use Edit interactions to prevent price/genre slicers and the paid charts from filtering that comparison, and prevent the comparison from misleadingly filtering the paid visuals. Label it `Whole comparison sample; independent of paid-title slicers`.

A later unified model requires regenerating free and paid rows with shared identifiers and fields from the raw source. The missing metadata cannot be reconstructed from this comparison export.

## 6. Check chart scales and results

Use zero-baseline percentage axes for bar charts. Format all review scores as percentages consistently. Ensure the line-chart range includes 86.7% (0–100% is a safe choice).

With slicers cleared, expected paid-data cards are approximately:

- Game Records: 26,471
- Mean Positive Review Share: 78.90%
- Mean Price: 6.28 in the source price unit

Expected full paid price-band means: Under $5 77.5%; $5–10 81.5%; $10–20 80.8%; $20–30 79.3%; $30–40 78.2%; $40–70 75.2%.

Select first-listed Action and verify the record count becomes 11,110. Its $5–10 subgroup has 2,434 records and a mean score around 80.6%. Confirm the independent free/paid chart stays unchanged and is clearly labeled.

Finally clear selections, save, and export one full-page screenshot for the README. Visually check category order, readable labels, unclipped values and percentage formatting.
