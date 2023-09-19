from descriptive import gen_stats
import polars as pl

nba = pl.read_csv("nba-teams-2017.csv")

def test_describe():
    gen_stats(data=nba)