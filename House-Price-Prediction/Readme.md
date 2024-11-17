# House Price Prediction Using Linear Regression

This project demonstrates how to use **Linear Regression** to predict house prices based on various features such as the number of bedrooms, area size, and other relevant attributes. The goal is to create a machine learning model that can accurately predict house prices.

## Project Overview

The project uses a dataset of house prices with features such as:
- Number of bedrooms
- Area of the house (in square feet)
- Location (e.g., city or neighborhood)
- Age of the house
- Number of bathrooms

The model is built using **scikit-learn**'s Linear Regression algorithm.

## Requirements

- Python 3.x
- `pandas` for data manipulation
- `numpy` for numerical operations
- `matplotlib` and `seaborn` for data visualization
- `scikit-learn` for machine learning and model evaluation

You can install the necessary libraries using the following command:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Project Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Download the Dataset**:
   - Download the dataset from the [link](https://example.com/dataset) (or include a link to your dataset if hosted).
   - Ensure the dataset is saved as `house_data.csv` in the root directory.

3. **Run the Code**:
   - Run the `house_price_prediction.py` script to train the model and make predictions:

   ```bash
   python house_price_prediction.py
   ```

## Project Workflow

1. **Data Loading and Preprocessing**:
   - Load the dataset using `pandas`.
   - Handle missing values and preprocess categorical variables (if any).

2. **Exploratory Data Analysis (EDA)**:
   - Visualize the relationship between features and target variable (price).
   - Check for correlations between features.

3. **Feature Engineering**:
   - Select relevant features for the model.
   - Split the dataset into training and testing sets.

4. **Model Training**:
   - Train a Linear Regression model using `scikit-learn`.

5. **Model Evaluation**:
   - Evaluate the model's performance using metrics like **Mean Squared Error (MSE)** and **R-squared**.

6. **Prediction**:
   - Use the trained model to predict house prices based on new input data.

## Example Usage

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('house_data.csv')

# Feature selection and preprocessing steps

# Split data into features and target variable
X = df.drop('Price', axis=1)  # All columns except 'Price'
y = df['Price']  # Target variable (house price)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
```

## Results

After running the model, you should get the Mean Squared Error and R-squared values that indicate the model's accuracy in predicting house prices.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
