import pandas as pd

# Create the dataframe
data = {
    'food_name': ['Pizza', 'Salad', 'Burger', 'Pasta', 'Sandwich', 'Soup', 'Sushi', 'Steak', 'Fries', 'Cake'],
    'food_type': ['Italian', 'Healthy', 'Fast Food', 'Italian', 'Sandwich', 'Soup', 'Japanese', 'Steak', 'Fast Food', 'Dessert'],
    'food_price': [700, 300, 450, 600, 250, 150, 800, 1200, 200, 350],
    'healthy_or_unhealthy': ['Unhealthy', 'Healthy', 'Unhealthy', 'Healthy', 'Healthy', 'Healthy', 'Healthy', 'Unhealthy', 'Unhealthy', 'Unhealthy'],
    'rating': [4, 5, 3, 4, 3, 4, 5, 4, 2, 5],
    'life_spend': ['2 hours', '5 hours', '3 hours', '4 hours', '2 hours', '6 hours', '8 hours', '12 hours', '1 hour', '4 hours']
}

df = pd.DataFrame(data)

# 1) Print food name which has 3 hours of life and which price is greater than 500rs
filtered1 = df[(df['life_spend'] == '3 hours') & (df['food_price'] > 500)]
print("1) Food name with 3 hours life and price greater than 500rs:")
print(filtered1['food_name'].tolist())

# 2) Print top 3 food categories which are healthy and least expensive
filtered2 = df[df['healthy_or_unhealthy'] == 'Healthy'].sort_values(by='food_price').head(3)
print("\n2) Top 3 healthy and least expensive food categories:")
print(filtered2['food_type'].tolist())

# 3) Print food in ascending order and food price in descending order
sorted_df = df.sort_values(by=['food_name', 'food_price'], ascending=[True, False])
print("\n3) Food in ascending order and food price in descending order:")
print(sorted_df[['food_name', 'food_price']].to_string(index=False))

# 4) Print all food items specific categories
categories = ['Italian', 'Healthy']
filtered4 = df[df['food_type'].isin(categories)]
print("\n4) All food items in specific categories:")
print(filtered4[['food_name', 'food_type']].to_string(index=False))

# 5) Print all the food items starting with 'P'
filtered5 = df[df['food_name'].str.startswith('P')]
print("\n5) Food items starting with 'P':")
print(filtered5['food_name'].tolist())

# 6) Print all the food items which have exactly unit price 500
filtered6 = df[df['food_price'] == 500]
print("\n6) Food items with exactly unit price 500:")
print(filtered6['food_name'].tolist())

# 7) Print all the food items which are unhealthy and expensive
filtered7 = df[(df['healthy_or_unhealthy'] == 'Unhealthy') & (df['food_price'] > 500)]
print("\n7) Unhealthy and expensive food items:")
print(filtered7['food_name'].tolist())

# 8) Print food items in descending order as per price
sorted_by_price_desc = df.sort_values(by='food_price', ascending=False)
print("\n8) Food items in descending order by price:")
print(sorted_by_price_desc['food_name'].tolist())

# 9) Print all the categories which have life span greater than 12 hours
filtered9 = df[df['life_spend'].str.extract(r'(\d+)').astype(int) > 12]
unique_categories = filtered9['food_type'].unique()
print("\n9) Categories with life span greater than 12 hours:")
print(unique_categories.tolist())

# 10) Print all the food items starting with 'D' or 'P' and unit prices between 500rs to 1000rs
filtered10 = df[(df['food_name'].str.startswith(('D', 'P'))) & (df['food_price'].between(500, 1000))]
print("\n10) Food items starting with 'D' or 'P' and unit prices between 500rs to 1000rs:")
print(filtered10[['food_name', 'food_price']].to_string(index=False))
