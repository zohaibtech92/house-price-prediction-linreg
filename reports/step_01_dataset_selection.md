# Step 1: Problem Framing & Dataset Selection

## Goal
Build a linear regression model that predicts house sale price, and use it to practice missing-value handling, feature scaling, and coefficient interpretation.

## Problem definition
- **Task type:** supervised regression (continuous target)
- **Target:** `SalePrice` (USD)
- **Unit of analysis:** one row = one residential property sale in Ames, Iowa (2006–2010)

## Dataset choice
**Chosen:** Ames Housing dataset (Dean De Cock), original version via a Hugging Face mirror.

**Why Ames:**
- Roughly 80 features (numeric and categorical), so there is real material for feature engineering and encoding
- Contains missing values, which makes it useful for practicing imputation
- Designed specifically as a modern teaching alternative to Boston Housing

**Why not Boston Housing:** it was removed from scikit-learn because one of its features encodes a racial demographic variable in a problematic way. It is also small (13 features) and dated.

**Why the original version instead of Kaggle's:** the original is a single combined file, so I create my own train/test split in code. Column names follow De Cock's original naming, which may differ slightly from Kaggle's version (e.g. spacing in names).

## Data loaded successfully
- Shape: [FILL IN: rows × columns from your sanity check]
- Target column confirmed: `SalePrice`
- Download is automated in `src/download_data.py`; data files are not committed because the dataset license is listed as unknown on the mirror.

## Success criteria
- Evaluate on a held-out test set (RMSE, MAE, R²)
- Coefficients should make domain sense (e.g. larger living area → higher price)
- Residual plots should be checked for patterns that violate linear regression assumptions

## Known limitations (to revisit)
- Sale prices are likely right-skewed; a log transform may be needed
- A purely linear model may not capture all real pricing behavior

## Next step
Step 2: Exploratory data analysis
