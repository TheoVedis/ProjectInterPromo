import pandas as pd
import numpy as np
import operator




def load_data(path, nom_fichier):
    df = pd.read_csv(path + str(nom_fichier))
    return df




def info_df(df):
    print("Nombre de colonnes/variables : %i \nNombre de lignes : %i" \
      %(df.shape[1], df.shape[0]))
    print('\n')

    #type données
    print("-------------------------Types des colonnes-------------------------")

    print(df.dtypes)
    print('\n')

    #Afficher distinct values
    print("-------------------------Valeurs distinctes-------------------------")

    for col in df:
        print(df[col].unique())
    print('\n')

    #Nombre des valeurs distinctes
    print("-------------------------Nombre valeurs distinctes-------------------------")

    for col in df:
        print(col, ':', len(pd.unique(df[col])))
    print('\n')

    #Données manquantes
    liste_nan = []
    for col in df:
        liste_nan.append([col,round(df[col].isnull().sum() / df.shape[0]*100,2)])

    print("------------------------- % des données manquantes-------------------------")

    sortedList = sorted(liste_nan,key=operator.itemgetter(1),reverse=True)
    for s in sortedList:
        print(s)



def drop_duplicates(df):
    df_without_duplicates = df.drop_duplicates()
    print("DataFrame with duplicates:")
    print(df.shape, "\n")

    print("DataFrame without duplicates:")
    print(df_without_duplicates.shape, "\n")

    return df_without_duplicates




def echantillon(df_fraude, df_pas_fraude, pourcentage = 0.1):
    ech = df_fraude.sample(frac=pourcentage).append(df_pas_fraude.sample(frac=pourcentage))
    return ech

def train_split_ech(echantillon,var_a_expliquer):
    X = echantillon.drop(str(var_a_expliquer), axis=1)
    y = echantillon[str(var_a_expliquer)]
    x_train ,x_test,y_train,y_test=train_test_split(X,y,test_size=0.5)
    return x_train, x_test, y_train, y_test
