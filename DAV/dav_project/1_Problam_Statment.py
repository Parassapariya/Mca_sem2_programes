import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "watches.csv"
df = pd.read_csv(file_path)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Convert Brand column to lowercase for consistency
df["Brand"] = df["Brand"].str.lower()

# Count the number of listings per brand
brand_listings = df["Brand"].value_counts().head(10)

# Plot the top 10 brands by number of listings
plt.figure(figsize=(12, 5))
brand_listings.plot(kind="bar", color="skyblue")
plt.title("Top 10 Watch Brands by Listings")
plt.xlabel("Brand")
plt.ylabel("Number of Listings")
plt.xticks(rotation=45)
plt.show()

# Count the number of watches sold per brand
if "Watches Sold by the Seller" in df.columns:
    brand_sales = df.groupby("Brand")["Watches Sold by the Seller"].sum().sort_values(ascending=False).head(10)

    # Plot the top 10 brands by number of watches sold
    plt.figure(figsize=(12, 5))
    brand_sales.plot(kind="bar", color="green")
    plt.title("Top 10 Watch Brands by Sales")
    plt.xlabel("Brand")
    plt.ylabel("Total Watches Sold")
    plt.xticks(rotation=45)
    plt.show()
