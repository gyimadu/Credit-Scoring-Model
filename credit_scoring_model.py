import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import GridSearchCV
import joblib

df = pd.read_excel('default of credit card clients.xls', skiprows=1)
print(df.head())

print(df.isnull().sum())
print(df.describe())
print(df.info())

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

sns.histplot(df['LIMIT_BAL'], kde=True)
plt.show()

df = pd.get_dummies(df, drop_first=True)
X = df.drop(columns=['ID', 'default payment next month'])
y = df['default payment next month']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression(C=1, solver='saga', max_iter=500)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(classification_report(y_test, y_pred))
print(f'ROC-AUC Score: {roc_auc_score(y_test, y_pred)}')

param_grid = {'C': [0.1, 1, 10, 100], 'solver': ['liblinear', 'saga']}
grid = GridSearchCV(LogisticRegression(), param_grid, refit=True, verbose=2, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_)

joblib.dump(model, 'credit_scoring_model.pkl')

joblib.dump(scaler, 'scaler.pkl')

