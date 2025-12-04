import pandas as pd


csv_files = ["data1.csv", "data2.csv", "data3.csv"]
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

final_df = combined_df.drop_duplicates()

print("Final DataFrame size after removing duplicates:", len(final_df))
print(final_df.head())