# 🏦 Predicting Bank Customer Churn Using Decision Tree

# 🎯 Project Objective
The goal of this project is to predict whether a bank customer is likely to churn based on socio-financial features. The methodology combines:

An exploratory data analysis (EDA) phase using dimensionality reduction techniques such as PCA, MCA, or FAMD depending on the data types.

A decision tree model to predict churn.

# 📂 Dataset
We use the dataset provided in BankChurners.csv, which includes detailed customer information:

Demographics (e.g., age, gender, marital status)

Behavioral data (e.g., credit usage, transactions, balances)

Target variable: Attrition_Flag (indicates whether the customer has churned)

# ⚙️ Methodology
## 1. Data Preprocessing
Removal of irrelevant or identifier columns (e.g., CLIENTNUM)

Encoding of categorical variables

Handling of missing values if present

## 2. Exploratory Data Analysis
PCA (Principal Component Analysis) if variables are mostly numerical

MCA (Multiple Correspondence Analysis) or FAMD (Factor Analysis of Mixed Data) if the dataset contains a mix of categorical and numerical variables

Visualization of variable distributions and customer groups

## 3. Modeling
Splitting the data into training and test sets

Training a decision tree classifier to predict Attrition_Flag

Evaluation using metrics such as Accuracy, Precision, Recall, F1-score, and Confusion Matrix

## 4. Interpretation
Feature importance ranking

Extraction of decision rules from the tree

# 📈 Expected Outcomes
Identification of the key factors driving customer churn

A model that is simple, interpretable, and actionable by business teams

Clear visualization of the decision-making process

# 🛠️ Technologies Used
Python (Pandas, NumPy, Scikit-learn, matplotlib, seaborn)

prince (or factor_analyzer) for PCA/MCA/FAMD

Jupyter Notebook

# 📊 Sample Visuals
PCA plot with grouping by Attrition_Flag

Decision tree diagram with rule paths

# 📌 Further Improvements
Comparison with other models (Random Forest, XGBoost, etc.)

Deploying an interactive dashboard using Streamlit or Dash

Class imbalance treatment using techniques like SMOTE

# 📁 Project Structure
css
Copier
Modifier
📦 bank-churn-prediction-decision-tree
 ┣ 📊 data/
 ┃ ┗ BankChurners.csv
 ┣ 📓 notebooks/
 ┃ ┗ 01_EDA_DimensionalityReduction.ipynb
 ┃ ┗ 02_Modeling_DecisionTree.ipynb
 ┣ 📁 src/
 ┃ ┗ preprocessing.py
 ┃ ┗ model.py
 ┣ README.md
 ┗ requirements.txt
✅ Authors
Madou Gagi Ismael

(https://www.linkedin.com/in/ismael-madou-gagi-grema/)
