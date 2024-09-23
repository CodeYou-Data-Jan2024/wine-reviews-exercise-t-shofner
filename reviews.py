# add your code here
import pandas as pd
import zipfile

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')



reviews_per_country = df.country.value_counts()

mean_points_per_country = df.groupby('country')['points'].mean().round(1)



combined_df = pd.DataFrame({
    'Count': reviews_per_country,
    'Points': mean_points_per_country
}).reset_index()


combined_df.columns = ['Country', 'Count', 'Points']
combined_df = combined_df.sort_values(by='Count', ascending=False)


combined_df.to_csv('reviews-per-country.csv')

#print(combined_df)