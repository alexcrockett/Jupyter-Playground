# README (notes)

Hi and welcome to the playground. In the spirit of live-learning this repo contains Jupyter notebooks I am using in real time to learn both Python and a little about data-science and machine learning. 

In this repo projects each have a sub-directory. The file structure reflects process. 

So the general structure is:

- Notes (including my own refe
- Any data (spreadhseets mostly)
- Explore (initial explorations, get a general sense how the data is structured)
- -  In general any exports for other files to use will also be found here
- Descriptives (Explore content like means, variances and defined variables) will be listed and shown
- Analysis (This will almost always be some kind of exploratory analysis)
- Further analysis (here is where more involved analysis and/or models will be found)

## Analyses I am interested in exploring

### 1. Correlation Analysis

- **Purpose**: To find relationships between different variables.
- **Method**: Use Pearson or Spearman correlation coefficients.
- **Python Tools**: `pandas.DataFrame.corr()` for correlation matrices, `seaborn` for heatmap visualizations.

### 2. Time Series Analysis

- **Purpose**: To understand trends, seasonality, and cyclic patterns.
- **Method**: Use ARIMA (Autoregressive Integrated Moving Average) models, or simpler moving average models.
- **Python Tools**: `statsmodels` library, particularly `ARIMA` or `SARIMAX` for seasonal data.

### 3. Cluster Analysis

- **Purpose**: To group similar variables based on certain characteristics.
- **Method**: K-means clustering or hierarchical clustering.
- **Python Tools**: `scikit-learn` for K-means, `scipy` for hierarchical clustering.

### 4. Factor Analysis

- **Purpose**: To identify underlying factors that explain the patterns of correlations within a set of observed variables (like different stock attributes).
- **Python Tools**: `factor_analyzer` package.

### 5. Regression Analysis

- **Purpose**: To model the relationship between potential predictors.
- **Method**: Linear regression, multiple regression.
- **Python Tools**: `statsmodels` or `scikit-learn`.

### 6. ANOVA (Analysis of Variance)

- **Purpose**: To compare the means of different groups.
- **Method**: One-way or two-way ANOVA.
- **Python Tools**: `scipy.stats.f_oneway` for one-way ANOVA.

### 7. Building a Simple Neural Network

- **Purpose**: Primarily to create models that can extend beyond data-sets I am using.
- **Method**: A basic feedforward neural network or LSTM (Long Short-Term Memory) networks for sequences.
- **Python Tools**: `keras` and `tensorflow`.

