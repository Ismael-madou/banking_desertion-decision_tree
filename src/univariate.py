import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Remplace 'chemin/vers/ton_fichier.csv' par le chemin réel
data = pd.read_csv('C:/Users/MGI/Desktop/banking_desertion-decision_tree/data/BankChurners.csv')

#suppression des deux dernières colonnes
data.drop(columns=data.columns[-2:], inplace=True)

data.head()
data.describe()
data.info()


# Trouver les variables de type 'object' (catégorielles)
variables_categorielles = data.select_dtypes(include='object').columns

# Afficher la distribution de chaque variable catégorielle
print("\nSTATISTIQUES DES VARIABLES CATÉGORIELLES :\n")
for colonne in variables_categorielles:
    print(f"--- {colonne} ---")
    print(data[colonne].value_counts())
    print("\n")

# Diagrammes en barres pour les variables catégorielles
for col in variables_categorielles:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=col, data=data)
    plt.title(f"Distribution de {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



# Histogrammes des variables numériques
variables_numeriques = data.select_dtypes(include=['int64', 'float64']).hist(bins=20, figsize=(14, 10))

# Afficher la distribution de chaque variable numerique
plt.suptitle("Histogrammes des variables numériques", fontsize=16)
plt.tight_layout()
plt.show()





