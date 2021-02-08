"""
  * This file is part of project Creation-of-a-search-engine. 
    It's copyrighted by the contributors
  * Copyright (c) 2021 lprtk
"""

"""
Welcome to the main module. To start the project, you will just have to enter, 
in the console, the path to the folder where the csv's are located.
Then everything is done automatically.
"""

########################################################################################
                             ## Librairies loading ##
########################################################################################

import pandas as pd
import numpy as np
import interface_imdb

########################################################################################
                               ## Project Launch ##
########################################################################################

path = input("Entrer le chemin du fichier : ")


df_movies = pd.read_csv(path+"/IMDb_movies.csv", sep=",")
df_names = pd.read_csv(path+"/IMDb_names.csv", sep=",")
df_ratings = pd.read_csv(path+"/IMDb_ratings.csv", sep=",") 
df_title_principals = pd.read_csv(path+"/IMDb_title_principals.csv", sep=",")


df_movies['year'][df_movies['year'] == 'TV Movie 2019'] = '2019'

df_movies['avg_vote'].astype(np.float64)
df_movies['year'].astype(np.int64)


df_movies["title_low"]=df_movies["original_title"].str.lower()
df_movies["genre_low"]=df_movies["genre"].str.lower()
df_movies["actors_low"]=df_movies["actors"].str.lower()


interface_imdb.interface(path,df_names,df_movies,df_ratings,df_title_principals)


    
