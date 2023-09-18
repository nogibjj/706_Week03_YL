import polars as pl
import matplotlib.pyplot as plt

nba = pl.read_csv("nba-teams-2017.csv")
nba = nba.drop(columns=["team"])
print(nba.describe())


def gen_stats():
    data = pl.read_csv("nba-teams-2017.csv")
    data = data.drop(columns=["team"])
    return data.describe()


def build_histogram():
    plt.hist(nba["points"], bins=5, edgecolor="k")
    plt.xlabel("Points")
    plt.ylabel("Frequency")
    plt.title("Frequency distribution of Points across Teams")
    plt.show()
    return


def build_scatterplot():
    plt.scatter(nba["wins"], nba["points"], alpha=0.5, s=60)
    plt.xlabel("Wins")
    plt.ylabel("Points")
    plt.show()
    return


if __name__ == "__main__":
    gen_stats()
    build_histogram()
    build_scatterplot()
