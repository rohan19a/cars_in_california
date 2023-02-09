import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv('vehicle-fuel-type-count-by-zip-code-2022-crunch.csv')
df1 = pd.read_csv('Personal_Income_Tax_Statistics_By_Zip_Code.csv')

#merge the two dataframes on the zip code column
df3 = pd.merge(df, df1, on='Zip Code')
#remove duplicate zip codes
df3 = df3.drop_duplicates(subset='Zip Code', keep='first')

#save the merged dataframe to a csv
df3.to_csv('vehicle-fuel-type-count-by-zip-code-2022-crunch-merge.csv', index=False)

#create a scatterplot of the top 100 zip codes with the most electric vehicles and the average income
df3.nlargest(100, 'Battery Electric').plot.scatter(x='Returns', y='Battery Electric')
plt.show()

from sklearn.linear_model import LinearRegression
import numpy as np

#make a new dataframe with only the returns and battery electric columns
df4 = df3[['Returns', 'Battery Electric']]

#run a linear regression on df4
X = df4['Returns'].values.reshape(-1, 1)
y = df4['Battery Electric'].values.reshape(-1, 1)

print("X:", X)
model = LinearRegression()
model.fit(X, y)

r_sq = model.score(X, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
