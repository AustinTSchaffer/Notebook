import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    df_stats = pd.read_json("./.stats/data/stats.json")
    df_stats = df_stats.T
    df_stats.timestamp = pd.Series.apply(df_stats.timestamp, datetime.datetime.fromisoformat)

    # The commits from merging in the "Foam" notebook base breaks
    # the graph a litte bit.
    df_stats = df_stats[df_stats.num_words > 5500]
    df_stats = df_stats.sort_values('timestamp')

    sns.set_theme()

    sns.lineplot(x=df_stats.timestamp, y=df_stats.num_words)
    plt.title("Word Count over Time")
    plt.xlabel("Timestamp")
    plt.savefig('./.stats/rendered/wordcount.png')

    plt.clf()

    sns.lineplot(x=df_stats.timestamp, y=df_stats.num_files)
    plt.title("File Count over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("File Count")
    plt.savefig('./.stats/rendered/filecount.png')
