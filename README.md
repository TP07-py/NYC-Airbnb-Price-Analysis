# NYC-Airbnb-Price-Analysis

This project analyzes Airbnb listing prices in New York City using Python and Pandas. The analysis includes removing extreme outliers, comparing room types, and visualizing price trends.

## Features
- Cleans the dataset by selecting relevant columns
- Removes extreme price outliers beyond the 99th percentile
- Performs a Z-test to compare price differences between room types
- Generates visualizations:
  - Box plot of price distribution by room type
  - Scatter plot of price vs. number of reviews
  - Bar chart of average price by neighborhood

## Requirements
Ensure you have Python installed along with the following dependencies:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

## How It Works
1. Reads the dataset `AB_NYC_2019.csv`.
2. Filters relevant columns: `room_type`, `price`, `number_of_reviews`, `neighbourhood_group`.
3. Removes price outliers by keeping only values within the 99th percentile.
4. Splits data by `room_type` and calculates:
   - Mean and standard deviation for each category
   - Z-score to measure price differences
5. Visualizes trends with plots for better insights.

## File Structure
```
.
├── AB_NYC_2019.csv    # NYC Airbnb dataset
├── main.py            # Script for data analysis and visualization
```

## Future Improvements
- Incorporate additional factors influencing pricing
- Implement interactive visualizations
- Extend analysis to other cities

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request.

