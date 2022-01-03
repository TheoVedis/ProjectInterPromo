import pandas as pd
import numpy as np
import zipfile

def afficher_fichier_zip(path, nom_zip):
    myzipfile= zipfile.ZipFile(path + str(nom_zip))
    return myzipfile.namelist()

def import_data(path, fichier, nom_zip):
    zf = zipfile.ZipFile(path + str(nom_zip))
    df = pd.read_csv(zf.open(str(fichier)))
    return df

def readme(path, nom_zip, readme):
    zf = zipfile.ZipFile(path + str(nom_zip))
    file =  zf.open(str(readme))
    for line in file:
        print(line)
    file.close()
    