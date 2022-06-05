from statistics import variance
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
fig = plt.figure(figsize=(20, 7))
sns.set_style("darkgrid")

df1 = pd.read_csv('../../Datasets/Android Apps/apps.csv')
df2 = pd.read_csv('../../Datasets/Android Apps/user_reviews.csv')

print(df2.head(10))
print(df1.head())

print(df1.info())
df1['Installs'] = df1['Installs'].str.replace('+', '')
df1['Installs'] = df1['Installs'].str.replace(',', '')
df1['Installs'] = df1['Installs'].astype('int')
apps = df1

# Grouping the app categories to get the statistics
app_category_info = apps.groupby(['Category']).agg(
    {'App': 'count', 'Price': 'mean', 'Rating': 'mean'})
app_category_info.columns = [
    'Number of apps', 'Average price', 'Average rating']
app_category_info.to_csv("outputs/App_category_info.csv", index=False)

# 10 categories with best user reviews
merged = df1.merge(df2, left_on='App', right_on='App')
finan = merged[merged['Category'] == 'FINANCE']
free = finan[finan['Type'] == 'Free']
grouped = free.groupby('App').agg({'Sentiment Score': 'mean'})
top_10_user_feedback = grouped.sort_values(
    by='Sentiment Score', ascending=False).head(10)
top_10_user_feedback.to_csv(
    "outputs/Top 10 categories with best sentiment score.csv", index=False)

# Understanding data using plots
most_apps_grouped_category = app_category_info.sort_values(
    by='Number of apps', ascending=False).head(5)

sns.barplot(x=most_apps_grouped_category.index,
            y=most_apps_grouped_category['Number of apps'], palette="Blues_d")
plt.title("Top 5 app category with the most ratings")
fig.savefig('imgs/apps with best ratings.svg', format='svg', dpi=1200)

plt.hist(apps['Rating'])
plt.title("Skewness of Ratings")
fig.savefig('imgs/Skewness of ratings.svg', format='svg', dpi=1200)


merged = merged.dropna(subset=['Sentiment Score'])
sns.boxplot(x='Type', y='Sentiment Score', data=merged)
fig.savefig('imgs/Sentiment score.svg', format='svg', dpi=1200)
