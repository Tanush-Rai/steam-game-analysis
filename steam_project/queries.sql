-- Run sql_analysis.ipynb first to load games_clean.csv into SQLite.
-- main_genre is the first-listed source genre, not a verified primary genre.
-- Scores are unweighted means across selected paid records.

-- Review score across price bands
SELECT price_band,
       ROUND(AVG(review_score) * 100, 1) AS avg_score,
       COUNT(*) AS num_games
FROM games
GROUP BY price_band
ORDER BY avg_score DESC;


-- Review score by genre, restricting the comparison to groups with at least 100 records
SELECT main_genre,
       ROUND(AVG(review_score) * 100, 1) AS avg_score,
       COUNT(*) AS num_games
FROM games
GROUP BY main_genre
HAVING COUNT(*) >= 100
ORDER BY avg_score DESC;


-- Highly rated games under $10 with a substantial number of reviews
SELECT Name,
       Price,
       ROUND(review_score * 100, 1) AS score,
       total_reviews
FROM games
WHERE Price < 10
  AND total_reviews >= 1000
ORDER BY review_score DESC
LIMIT 10;
-- Rank first-listed genre groups within each price band (minimum 100 records).
-- DENSE_RANK retains ties in the unrounded mean.
WITH grouped AS (
 SELECT price_band, main_genre, COUNT(*) AS num_games, AVG(review_score) AS mean_score
 FROM games
 GROUP BY price_band, main_genre
 HAVING COUNT(*) >= 100
)
SELECT price_band, main_genre, num_games, ROUND(mean_score * 100, 2) AS avg_score,
 DENSE_RANK() OVER (PARTITION BY price_band ORDER BY mean_score DESC) AS rank_within_band
FROM grouped
ORDER BY price_band, rank_within_band;
