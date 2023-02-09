import pandas as pd

# Read in the data
df = pd.read_csv('vehicle-fuel-type-count-by-zip-code-2022.csv')

#create a new dataframe called df2 with the columns zip, then a column for each fuel type
df2 = pd.DataFrame(columns=['Zip Code', 'Battery Electric', 'Gasoline', 'Diesel', 'Hybrid Gasoline', 'Flex-Fuel', 'Diesel and Diesel Hybrid', 'Plug-in Hybrid'])

#add the unique zip codes to the new dataframe
df2['Zip Code'] = df['Zip Code'].unique()

#create a function that returns the total amount of each fuel type for a given zip code
def get_fuel_type_count(zip_code, fuel_type):
    #create a new dataframe with only the rows that match the zip code and fuel type
    df3 = df.loc[(df['Zip Code'] == zip_code) & (df['Fuel'] == fuel_type)]
    return len(df3)

#for each zip code, run get_fuel_type_count for each fuel type and add the results to the new dataframe
for x in df2['Zip Code']:
    df2.loc[df2['Zip Code'] == x, 'Battery Electric'] = get_fuel_type_count(x, 'Battery Electric')
    df2.loc[df2['Zip Code'] == x, 'Gasoline'] = get_fuel_type_count(x, 'Gasoline')
    df2.loc[df2['Zip Code'] == x, 'Diesel'] = get_fuel_type_count(x, 'Diesel')
    df2.loc[df2['Zip Code'] == x, 'Hybrid Gasoline'] = get_fuel_type_count(x, 'Hybrid Gasoline')
    df2.loc[df2['Zip Code'] == x, 'Flex-Fuel'] = get_fuel_type_count(x, 'Flex-Fuel')
    df2.loc[df2['Zip Code'] == x, 'Diesel and Diesel Hybrid'] = get_fuel_type_count(x, 'Diesel and Diesel Hybrid')
    df2.loc[df2['Zip Code'] == x, 'Plug-in Hybrid'] = get_fuel_type_count(x, 'Plug-in Hybrid')
    df2.to_csv('vehicle-fuel-type-count-by-zip-code-2022-crunch.csv', index=False)
#save the df2 to a csv


