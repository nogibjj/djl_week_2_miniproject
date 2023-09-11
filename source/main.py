"""
This fun prints descriptive analytics of a data set
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
def print_ds_info(data):
    """
    parameter:data
    uses data.columns and describe() to print descriptive info of dataset
    """
    print("The variables in this data set are the following:",list(data.columns))
    print("Data behaves as follows:\n", data.describe())
 
def data_vis(data):
    """this fun generates a simple plot of the data set"""
    sns.barplot(data=data,  x="descrip",y="sexostt", ci=None)
    plt.xlabel("Age group")
    plt.ylabel("Number of inmmates")
    plt.title("Number of inmates by age group in Mexican prisons in 2021")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.savefig('bar_plot.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    #dir=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'source'))
    #sys.path.append(dir)
    # Read the CSV file
    my_data = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1")
    # Print dataset info
    print_ds_info(my_data)
    # generate graph
    data_vis(my_data)
