#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv("contestant_table.csv", encoding="latin")
    return df

def main():
    dataframe = load_data()
    homestate = dataframe.loc[:,"hometown"][-2:]
    plot = sns.countplot(x="hometown", data=homestate)
    plt.show()


if __name__ == "__main__": 
    main()
