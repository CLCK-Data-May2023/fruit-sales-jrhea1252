# add your code here

import pandas as pd
# Create the data 
data = {
    '': ['2017 Sales', '2018 Sales'],
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

# Turn the data into a Pandas DataFrame 
df = pd.DataFrame(data)

# Save to a CSV file in the project directory
df.to_csv('fruit.csv', index=False)

print("Data saved to 'fruit.csv'")
