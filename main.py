import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
airbnb_data = pd.read_csv("AB_NYC_2019.csv")

# Keep only necessary columns
selected_columns = ['room_type', 'price', 'number_of_reviews', 'neighbourhood_group']
airbnb_data = airbnb_data[selected_columns]

# Remove extreme price outliers (only keep listings within the 99th percentile)
price_threshold = airbnb_data['price'].quantile(0.99)
clean_data = airbnb_data[airbnb_data['price'] <= price_threshold]

# Split data by room type
homes = clean_data[clean_data['room_type'] == 'Entire home/apt']['price']
private_rooms = clean_data[clean_data['room_type'] == 'Private room']['price']

# Calculate means and standard deviations
home_avg_price = np.mean(homes)
home_std_dev = np.std(homes, ddof=1)
home_count = len(homes)

room_avg_price = np.mean(private_rooms)
room_std_dev = np.std(private_rooms, ddof=1)
room_count = len(private_rooms)

# Z-test calculation
z_score = (home_avg_price - room_avg_price) / np.sqrt(
    (home_std_dev**2 / home_count) + (room_std_dev**2 / room_count))

# Print Z-test results
print("\nWhat we found about NYC Airbnb prices:")
print(f" Average price for entire home/apartment: ${home_avg_price:.2f}")
print(f" Average price for private room: ${room_avg_price:.2f}")
print(f" Z-score from our test: {z_score:.2f}")

# Box Plot: Price Distribution by Room Type
plt.figure(figsize=(10, 6))
clean_data.boxplot(column='price', by='room_type', vert=False)
plt.title('How do prices vary by room type?')
plt.xlabel('Price ($)')
plt.ylabel('Room Type')
plt.suptitle('')  # This removes the automatic suptitle
plt.show()

# Scatter Plot: Price vs. Number of Reviews
plt.figure(figsize=(10, 6))
plt.scatter(clean_data['number_of_reviews'],
           clean_data['price'],
           alpha=0.3,
           color='darkblue')
plt.title('Are more reviewed places priced differently?')
plt.xlabel('Number of Reviews')
plt.ylabel('Price ($)')
plt.xlim(0, 200)  # Focus on listings with 0-200 reviews
plt.ylim(0, 500)  # Focus on listings under $500
plt.grid(True, alpha = 0.3)

# Bar Chart: Average Price by Neighbourhood Group
average_prices = clean_data.groupby('neighbourhood_group')['price'].mean()

plt.figure(figsize=(10, 6))
average_prices.plot(kind='bar', color='skyblue')
plt.title('Average Airbnb Prices by Neighborhood')
plt.xlabel('Neighborhood')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()  # Prevent label cutoff
plt.show()
