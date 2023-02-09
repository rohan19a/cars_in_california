import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv('vehicle-fuel-type-count-by-zip-code-2022-crunch.csv')

#plot a bar chart of the sum of each column in the dataframe (except for the zip code column)
#df.sum(axis=0).plot(kind='bar')


#plot a bar chart with top ten zip codes with most electric vehicles 
#make new dataframe with only the zip code and battery electric columns
df2 = df[['Zip Code', 'Battery Electric']]
df2.sort_values(by='Battery Electric', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.show()
plt.savefig('top-10-zip-codes-with-most-electric-vehicles.png')


#make new dataframe with only the zip code and Gasoline columns
df2 = df[['Zip Code', 'Gasoline']]
df2.sort_values(by='Gasoline', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.savefig('top-10-zip-codes-with-most-gasoline-vehicles.png')

#make new dataframe with only the zip code and Diesel columns
df2 = df[['Zip Code', 'Diesel']]
df2.sort_values(by='Diesel', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.show()
plt.savefig('top-10-zip-codes-with-most-diesel-vehicles.png')

#make new dataframe with only the zip code and Hybrid Gasoline columns
df2 = df[['Zip Code', 'Hybrid Gasoline']]
df2.sort_values(by='Hybrid Gasoline', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.show()
plt.savefig('top-10-zip-codes-with-most-hybrid-gasoline-vehicles.png')

#make new dataframe with only the zip code and Flex-Fuel columns
df2 = df[['Zip Code', 'Flex-Fuel']]
df2.sort_values(by='Flex-Fuel', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.show()
plt.savefig('top-10-zip-codes-with-most-flex-fuel-vehicles.png')

#make new dataframe with only the zip code and Diesel and Diesel Hybrid columns
df2 = df[['Zip Code', 'Diesel and Diesel Hybrid']]
df2.sort_values(by='Diesel and Diesel Hybrid', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.show()
plt.savefig('top-10-zip-codes-with-most-diesel-and-diesel-hybrid-vehicles.png')

#make new dataframe with only the zip code and Plug-in Hybrid columns
df2 = df[['Zip Code', 'Plug-in Hybrid']]
df2.sort_values(by='Plug-in Hybrid', ascending=False).head(10).plot(kind='bar', x='Zip Code')
plt.show()
plt.savefig('top-10-zip-codes-with-most-plug-in-hybrid-vehicles.png')

