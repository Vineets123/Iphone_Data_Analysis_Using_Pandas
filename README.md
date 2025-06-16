# 📱 iPhone Dataset Analysis Project

This repository contains a comprehensive data analysis project conducted on an iPhone product dataset using **Python** and **pandas**. The analysis aims to extract insights related to pricing, specifications, ratings, and customer behavior.

## 📂 Dataset

- The dataset file used is: `iphone.csv`
- It contains information on various iPhone models, including:
  - Product Name
  - Sale Price
  - MRP
  - Star Rating
  - RAM
  - Number of Ratings & Reviews
  - And more...

---

## 🧹 Data Preprocessing Steps

Execute **1** and **2** before doing any of the analysis steps to get the fresh dataframe everytime
### 1. Standardize Column Names  
All column names were cleaned by replacing spaces with underscores (`_`) using:

```python
df.columns = df.columns.str.replace(' ', '_')
```

### 2. Fill Missing Star Ratings with Global Average  
Missing values in the `star_rating` column were initially filled using the dataset-wide average:

```python
df['star_rating'].fillna(df['star_rating'].mean(), inplace=True)
```

### 3. Fill Missing Star Ratings Based on RAM  
Missing ratings were then filled with the average rating of iPhones having the same RAM:

```python
avg_by_ram = df.groupby('ram')['star_rating'].transform('mean')
df['star_rating'] = df['star_rating'].fillna(avg_by_ram)
```

### 4. Calculate Discount Percentage  
A new column `discount_percentage` was created using:

```python
df['discount_percentage'] = (df['mrp'] - df['sale_price']) / df['mrp'] * 100
```

---

## 🔍 Analytical Insights

### 5. Model with the Highest Discount  
Identified the model offering the highest discount percentage.

### 6. Model Count by Storage Size  
Counted the total number of models for configurations like `64 GB`, `128 GB`, etc.

### 7. Model Count by Color  
Extracted color names from the product name and grouped models by color.

### 8. Model Count by iPhone Version  
Cleaned model names and grouped models by version (e.g., `iPhone 8`, `iPhone XR`, etc.).

### 9. Top 5 Most Reviewed Models  
Listed the top five models based on the highest number of reviews.

### 10. Price Range  
Calculated the difference between the highest and lowest sale prices.

### 11. Review Count for iPhone 11 and 12  
Filtered to calculate total number of reviews for `iPhone 11` and `iPhone 12`.  
*Only two rows in the output.*

### 12. Model with 3rd Highest MRP  
Identified the iPhone model with the third highest MRP.

### 13. Average MRP of High-End iPhones  
Calculated the average MRP of iPhones priced above ₹100,000.

### 14. Top Rated 128 GB iPhone (by Rating-to-Review Ratio)  
Among all `128 GB` models, found the one with the highest ratio of rating to number of reviews.

---

## 🛠 Requirements

- Python 3.x  
- pandas  
- numpy  
- Jupyter Notebook or any IDE

Install dependencies using:

```bash
pip install pandas numpy
```

---

## ▶️ How to Run

1. Clone this repository.
2. Ensure `iphone.csv` is placed in the root directory.
3. Run the script `Iphone Project.py` or open it in a Jupyter Notebook.

---

## 📌 Note

This analysis is structured to be educational and exploratory, ideal for those learning data wrangling, cleaning, and basic insights using pandas.
