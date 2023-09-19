
    # This is the generated report for summary statistics and visualization for [nba-teams-2017.csv](https://github.com/nogibjj/706_Week03_YL/blob/main/nba-teams-2017.csv).

    ## Descriptive statistics

    shape: (9, 27)
┌───────────┬───────────┬───────────┬───────────┬───┬───────────┬───────────┬───────────┬──────────┐
│ describe  ┆ games_pla ┆ wins      ┆ losses    ┆ … ┆ block_fga ┆ personal_ ┆ personal_ ┆ plus_min │
│ ---       ┆ yed       ┆ ---       ┆ ---       ┆   ┆ ---       ┆ fouls     ┆ fouls_dra ┆ us       │
│ str       ┆ ---       ┆ f64       ┆ f64       ┆   ┆ f64       ┆ ---       ┆ wn        ┆ ---      │
│           ┆ f64       ┆           ┆           ┆   ┆           ┆ f64       ┆ ---       ┆ f64      │
│           ┆           ┆           ┆           ┆   ┆           ┆           ┆ f64       ┆          │
╞═══════════╪═══════════╪═══════════╪═══════════╪═══╪═══════════╪═══════════╪═══════════╪══════════╡
│ count     ┆ 30.0      ┆ 30.0      ┆ 30.0      ┆ … ┆ 30.0      ┆ 30.0      ┆ 30.0      ┆ 30.0     │
│ null_coun ┆ 0.0       ┆ 0.0       ┆ 0.0       ┆ … ┆ 0.0       ┆ 0.0       ┆ 0.0       ┆ 0.0      │
│ t         ┆           ┆           ┆           ┆   ┆           ┆           ┆           ┆          │
│ mean      ┆ 82.0      ┆ 41.0      ┆ 41.0      ┆ … ┆ 4.746667  ┆ 19.893333 ┆ 19.906667 ┆ -2.9606e │
│           ┆           ┆           ┆           ┆   ┆           ┆           ┆           ┆ -17      │
│ std       ┆ 0.0       ┆ 11.188048 ┆ 11.188048 ┆ … ┆ 0.644196  ┆ 1.635371  ┆ 1.067363  ┆ 4.312612 │
│ min       ┆ 82.0      ┆ 20.0      ┆ 15.0      ┆ … ┆ 3.1       ┆ 16.6      ┆ 17.5      ┆ -6.9     │
│ 25%       ┆ 82.0      ┆ 32.0      ┆ 31.0      ┆ … ┆ 4.3       ┆ 18.8      ┆ 19.3      ┆ -2.9     │
│ 50%       ┆ 82.0      ┆ 41.0      ┆ 41.0      ┆ … ┆ 5.0       ┆ 20.1      ┆ 19.9      ┆ 0.2      │
│ 75%       ┆ 82.0      ┆ 51.0      ┆ 50.0      ┆ … ┆ 5.2       ┆ 20.8      ┆ 20.4      ┆ 2.6      │
│ max       ┆ 82.0      ┆ 67.0      ┆ 62.0      ┆ … ┆ 5.6       ┆ 24.8      ┆ 22.4      ┆ 11.6     │
└───────────┴───────────┴───────────┴───────────┴───┴───────────┴───────────┴───────────┴──────────┘

    ## Here are some plots to visualize relations between the important variables described in README.

    ### Histogram for Cumulative Points for all the teams during the season
    ![Alt text](figures/points-hist.png)

    ### Scatterplot for number of games won versus cumulative points for all teams during the season
    ![Alt text](figures/scatter.png)
