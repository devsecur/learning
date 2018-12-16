import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

def plot(history, cycles):
    sns.set_style('white')
    xvalues = range(len(history))
    yvalues = [i.accuracy for i in history]
    ax = plt.gca()
    ax.scatter(
        xvalues, yvalues, marker='.', facecolor=(0.0, 0.0, 0.0),
        edgecolor=(0.0, 0.0, 0.0), linewidth=1, s=1)
    ax.xaxis.set_major_locator(ticker.LinearLocator(numticks=2))
    ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.yaxis.set_major_locator(ticker.LinearLocator(numticks=2))
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    fig = plt.gcf()
    fig.set_size_inches(8, 6)
    fig.tight_layout()
    ax.tick_params(
        axis='x', which='both', bottom=True, top=False, labelbottom=True,
        labeltop=False, labelsize=14, pad=10)
    ax.tick_params(
        axis='y', which='both', left=True, right=False, labelleft=True,
        labelright=False, labelsize=14, pad=5)
    plt.xlabel('Number of Models Evaluated', labelpad=-16, fontsize=16)
    plt.ylabel('Accuracy', labelpad=-30, fontsize=16)
    plt.xlim(0, cycles)
    plt.ylim(0,1)
    plt.savefig('books_read.png')
    sns.despine()
