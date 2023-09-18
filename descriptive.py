import polars as pl
import matplotlib.pyplot as plt

nba = pl.read_csv("nba-teams-2017.csv")
nba = nba.drop(columns=["team"])
print(nba.describe())

def gen_stats():
    data = pl.read_csv("nba-teams-2017.csv")
    data = data.drop["team"]
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

    # calculate the median/mean/standard deviation for the log wine prices
    # price_median = df["Price"].dropna().median()
    # price_mean = df["Price"].dropna().mean()
    # price_sd = df["Price"].dropna().std()
    # print("The median log wine price is " + str(price_median))
    # print("The mean log wine price is " + str(price_mean))
    # print("The standard deviation for log wine price is " + str(price_sd))

    # visualization: histogram for log wine price
    # plt.hist(df["Price"], bins=5, edgecolor="k")
    # plt.xlabel("Log wine price")
    # plt.ylabel("Frequency")
    # plt.title("Frequency distribution of log wine price")
    # plt.show()

    # visualization: correlation plot between columns
    # sns.pairplot(df)


if __name__ == "__main__":
    gen_stats()
    build_histogram()
    build_scatterplot()