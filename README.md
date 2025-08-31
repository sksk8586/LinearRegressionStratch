# LinearRegressionStratch
# Linear Regression from Scratch

This project implements linear regression using gradient descent from scratch in Python, without using scikit-learn's built-in regression algorithms.

## Overview

The code performs simple linear regression on an advertising dataset to predict sales based on TV advertising spending. It implements the gradient descent algorithm manually to find the optimal slope (m) and intercept (b) for the linear relationship.

## Dataset

The project uses an `advertising.csv` dataset with the following features:
- **TV**: TV advertising spending
- **Radio**: Radio advertising spending (dropped in this analysis)
- **Newspaper**: Newspaper advertising spending (dropped in this analysis)
- **Sales**: Target variable (sales figures)

Only the TV advertising column is used as the predictor variable for this simple linear regression.

## Implementation Details

### Key Components

1. **Data Preprocessing**: Loads the CSV file and removes Radio and Newspaper columns to focus on TV vs Sales relationship

2. **Gradient Descent Algorithm**: 
   - Implements the gradient descent optimization algorithm manually
   - Updates model parameters (slope and intercept) iteratively
   - Uses learning rate of 0.000001 and runs for 10,000 epochs

3. **Model Evaluation**: Calculates R² score to measure model performance

### Parameters
- **Learning Rate (L)**: 0.000001
- **Epochs**: 10,000
- **Progress Updates**: Every 50 epochs

## Results

The model outputs:
- Final slope (m) and intercept (b) values
- R² score for model evaluation
- Scatter plot with fitted regression line

## Performance Note

**Important**: The R² score from this implementation will be significantly lower than what you would get using scikit-learn's linear regression algorithms. This is because:

- Scikit-learn uses optimized algorithms (like ordinary least squares) that find the exact analytical solution
- This implementation uses gradient descent, which is an iterative approximation method
- The learning rate and number of epochs may not be perfectly tuned for optimal convergence
- Gradient descent can get stuck in local minima or converge slowly

Scikit-learn's `LinearRegression` uses mathematical optimizations that directly solve for the best-fit line, while this implementation demonstrates the underlying learning process step by step.

## Usage

```python
python linear_regression.py
```

Make sure you have the required dependencies:
- pandas
- matplotlib

## Files

- `advertising.csv`: Input dataset
- Main script: Contains the complete implementation

## Learning Objectives

This project demonstrates:
- Manual implementation of gradient descent
- Understanding of linear regression fundamentals  
- Visualization of regression results
- Performance comparison with optimized algorithms
