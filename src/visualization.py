import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df, col):
    sns.histplot(df[col], kde=True)
    plt.title(col)
    plt.show()

def plot_box(df, col):
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()