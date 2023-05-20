import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./fcc-forum-pageviews.csv", parse_dates=["date"], index_col=["date"])

# Clean data
df = df[(df["value"] <= df["value"].quantile(0.025))&
        (df["value"] >= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(17, 5))
    plt.plot(df.index, df["value"], "r-")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(by=[df.index.year, df.index.month]).mean()
    df_bar.index = df_bar.index.rename(["year", "month"])

    # Draw bar plot
    fig = df_bar.unstack().plot(kind="bar", figsize=(6.5, 6.5)).get_figure()
    plt.xlabel("Year")
    plt.ylabel("Average Page Views")
    plt.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], title="Months");

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax =plt.subplots(1,2, figsize=(20, 10))
    fig1 = sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    fig1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)", ylim=(0, 200000))
    fig2 = sns.boxplot(x="month", y="value", data=df_box, order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=ax[1])
    fig2.set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)", ylim=(0, 200000))

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
