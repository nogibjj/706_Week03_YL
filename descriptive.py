import polars as pl
import matplotlib.pyplot as plt

# nba = nba.drop(columns=["team"])
# print(nba.describe())


def gen_stats(data):
    data = data.drop(columns=["team"])
    return data.describe()


# def build_histogram(data):
#     plt.hist(data["points"], bins=35, edgecolor="k")
#     plt.xlabel("Points")
#     plt.ylabel("Frequency")
#     plt.title("Frequency distribution of Points across Teams")
#     plt.show()
#     return


# def build_scatterplot(data):
#     plt.scatter(data["wins"], data["points"], alpha=0.5, s=60)
#     plt.xlabel("Wins")
#     plt.ylabel("Points")
#     plt.show()
#     return


if __name__ == "__main__":
    nba = pl.read_csv("nba-teams-2017.csv")
    # print summary statistics
    summary = gen_stats(nba)
    # print histogram
    plt.hist(nba["points"], bins=35, edgecolor="k")
    plt.xlabel("Points")
    plt.ylabel("Frequency")
    plt.title("Frequency distribution of Points across Teams")
    plt.show()
    plt.savefig("figures/points-hist.png")
    # print scatterplot
    plt.scatter(nba["wins"], nba["points"], alpha=0.5, s=60)
    plt.xlabel("Wins")
    plt.ylabel("Points")
    plt.show()
    plt.savefig("figures/scatter.png")

    string = f'''
    # This is the generated report for summary statistics and visualization for [nba-teams-2017.csv](https://github.com/nogibjj/706_Week03_YL/blob/main/nba-teams-2017.csv).

    ## Descriptive statistics

    {summary}

    ## Here are some plots to visualize relations between the important variables described in README.

    ### Histogram for Cumulative Points for all the teams during the season
    ![Alt text](figures/points-hist.png)

    ### Scatterplot for number of games won versus cumulative points for all teams during the season
    ![Alt text](figures/scatter.png)

    '''

    file_path = "report.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(string)