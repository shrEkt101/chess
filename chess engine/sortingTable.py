import pandas as pd

# assign dataset
csvData = pd.read_csv("tictactoeTable.csv")
                                       
# displaying unsorted data frame
print("\nBefore sorting:")
csvData.to_csv("unsorted.csv")

# sort data frame
csvData.sort_values(["Depth"], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)

# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)

csvData.to_csv("sorted.csv")