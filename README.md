# House Price Prediction (Linear Regression)

Predicting house sale prices in Ames, Iowa using linear regression. The project focuses on three skills: **handling missing values**, **feature scaling**, and **interpreting model coefficients**. Each step is documented with its implementation.

## Dataset
- **Ames Housing dataset** by Dean De Cock (Truman State University): residential property sales in Ames, Iowa, 2006–2010.
- Source used: Hugging Face mirror of the original data (`cloderic/ames_iowa_housing`).
- Paper: De Cock, D. (2011). *Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project.* Journal of Statistics Education, 19(3).
- **Size:** 2930 rows × 82 columns
- **Target variable:** `sale_price`
- The Boston Housing dataset was deliberately not used (removed from scikit-learn over ethical concerns).

## Setup
```bash
git clone git@github.com:YOUR_GITHUB_USERNAME/house-price-prediction-linreg.git
cd house-price-prediction-linreg
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/download_data.py
```

## Project structure
```
data/raw/         original downloaded data (not committed)
data/processed/   cleaned data (not committed)
notebooks/        one notebook per step
src/              reusable scripts and functions
reports/          written documentation for each step
```

## Progress
- [x] Step 1: Problem framing & dataset selection → [report](reports/step_01_dataset_selection.md)
- [ ] Step 2: Exploratory data analysis
- [ ] Step 3: Handling missing values
- [ ] Step 4: Feature engineering & encoding
- [ ] Step 5: Feature scaling
- [ ] Step 6: Train/test split
- [ ] Step 7: Model training
- [ ] Step 8: Interpreting coefficients
- [ ] Step 9: Model evaluation
- [ ] Step 10: Residual analysis
- [ ] Step 11: Final write-up

## Status
Work in progress, updated as each step is completed.
