import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import resample


# Remplace 'chemin/vers/ton_fichier.csv' par le chemin réel
data = pd.read_csv('C:/Users/MGI/Desktop/banking_desertion-decision_tree/data/BankChurners.csv')

#suppression des deux dernières colonnes
data.drop(columns=data.columns[-2:], inplace=True)

# Afficher le nombre de valeurs manquantes par colonne
valeurs_manquantes = data.isnull().sum()
print(valeurs_manquantes)

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


df_majority = df[df.Attrition_Flag == 0]
df_minority = df[df.Attrition_Flag == 1]

df_majority_downsampled = resample(df_majority,
                                   replace=False,
                                   n_samples=len(df_minority),
                                   random_state=42)

df_balanced = pd.concat([df_majority_downsampled, df_minority])

##############################---------------------Statistiques bivariées----------------------############################
# Matrice de corrélation
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matrice de corrélation')
plt.show()

#boxplot pour la variable 'Customer_Age' selon le statut d'attrition
sns.boxplot(x='Attrition_Flag', y='Customer_Age', data=data)
plt.title("Âge selon le statut d'attrition")
plt.show()

# Afficher les tableaux croisés deux à deux
for i in range(len(qualitatives)):
    for j in range(i + 1, len(qualitatives)):
        var1 = qualitatives[i]
        var2 = qualitatives[j]
        print(f"Tableau croisé : {var1} vs {var2}")
        print(pd.crosstab(data[var1], data[var2]))
        print("\n")


# Calcul de la matrice de corrélation
correlation_matrix = numeriques.corr()

# Affichage avec une heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Matrice de corrélation des variables numériques")
plt.tight_layout()
plt.show()







