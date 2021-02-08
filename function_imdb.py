"""
  * This file is part of project Creation-of-a-search-engine. 
    It's copyrighted by the contributors
  * Copyright (c) 2021 lprtk
"""

"""
This module includes the six functions of the motor search. 
You can reuse these functions for other databases because they are universal with 
parameters.
"""

########################################################################################
                             ## Librairies loading ##
########################################################################################

import tkinter as tk
import pandas as pd
import numpy as np

########################################################################################
                               ## Modul function ##
########################################################################################

def get_movie_info(df_movies,df_ratings,Title):
    """
    This is a function that allows the user to enter the title of a movie: release date, 
    duration of the film, genre, country, language, main actors, description, average user ratings, 
    ratings received by age group of users.
    
    The title variable will be entered by the user via the Tkinter interface using the `.get()` method.

    Parameters
    ----------
    df_movies : dataframe
        IMDb movie database
    df_ratings : dataframe
        IMDb movie database
    Title : string
        title of the movie entered by the user via the Tkinter interface
    
    Returns
    -------
    res : string
        result displayed in the graphical interface

    """
    
    Title=Title.lower()  
    
  # 1 - Extraction des informations concernant le titre du film saisi 
    df_title1 = df_movies[df_movies["title_low"].str.contains(Title)]
    
    # Trie par année du plus récent au plus anciens
    df_title1["year"] = df_title1["year"].astype(str).astype(int)
    df_title1=df_title1.sort_values(by='year', ascending=False)
    
    # Gestion des erreurs de saisie et des films qui ont un même titre
    a=df_title1.shape
    if a[0]==0 :
        res="\n Aucun résultat trouvé pour un film au nom de "+Title+"."+"\n"
        res=res+" Veuillez vérifier votre saisie."
        print(res)
    
    # Recupération de l'info
    else :
         df_title1 = df_title1[['imdb_title_id','original_title','date_published','duration','genre','country','language','actors','description','year']]
         df_title2 = df_ratings[['imdb_title_id','mean_vote','allgenders_0age_avg_vote','allgenders_18age_avg_vote','allgenders_30age_avg_vote','allgenders_45age_avg_vote']]
         df_title = pd.merge(df_title1, df_title2, on='imdb_title_id', how='inner')
    
  # 2-3 - Extraction de l'information, On stock toute l'information récupéré dans une variable char appelé result
    res=str(a[0])+" résultat(s) trouvé(s) pour le titre "+Title+".\n\n\n"
    i=0
    while i<a[0] :
        res = res+"Titre original du film : "+str(df_title["original_title"][i])+"\n"+"\n"
        res = res +"Date de sortie : "+str(df_title["date_published"][i])+"\n"+"\n"
        res = res +"Année du film : "+str(df_title["year"][i])+"\n"+"\n"
        res = res +"Durée : "+str(df_title["duration"][i])+"mins"+"\n"+"\n"
        res = res +"Genre : "+str(df_title["genre"][i])+"\n"+"\n"
        res = res +"Pays de production : "+str(df_title["country"][i])+"\n"+"\n"
        res = res +"Langue du film : "+str(df_title["language"][i])+"\n"+"\n"
        res = res +"Les acteurs principaux : "+str(df_title["actors"][i])+"\n"+"\n"
        res = res +"Description : "+str(df_title["description"][i])+"\n"+"\n"
        res = res +"Note moyenne : "+str(df_title["mean_vote"][i])+"\n"
        res = res +"Note moyenne reçue par les - de 18 ans : "+str(df_title["allgenders_0age_avg_vote"][i])+"\n"
        res = res +"Note moyenne reçue par les [18-29] ans : "+str(df_title["allgenders_18age_avg_vote"][i])+"\n"
        res = res +"Note moyenne reçue par les [30-44] ans : "+str(df_title["allgenders_30age_avg_vote"][i])+"\n"
        res = res +"Note moyenne reçue par les + de 45 ans : "+str(df_title["allgenders_45age_avg_vote"][i])+"\n\n"
        res = res +"---------------------------------------------------------------------------------------------"+"\n\n"
        i=i+1
    return res


def get_commun_actors(df_movies,Title1,Year1,Title2,Year2):
    """
    The user enters two movie titles: list of the actors who played in these two movies 
    (e.g. the actors common to these two films, if any).
    
    Parameters
    ----------
    df_movies : dataframe
        IMDb movie database
    Title1 : string
        title of the first movie entered by the user via the Tkinter interface
    Year1 : int
        year of the first movie entered by the user via the Tkinter interface
    Title2 : string
        title of the second movie entered by the user via the Tkinter interface
    Year2 : int
        year of the second movie entered by the user via the Tkinter interface

    Returns
    -------
    resultat : string
        result displayed in the graphical interface

    """

    # 1-Constitution de la dataframe pertinente
    min_title1=Title1.lower()
    min_title2=Title2.lower()
    
    # On rajoute un champs années car il y a des films ayant le même titre
    actors1 = df_movies.loc[(df_movies['title_low'] == str(min_title1)) & (df_movies['year'] == int(Year1))]
    actors2 = df_movies.loc[(df_movies['title_low'] == str(min_title2)) & (df_movies['year'] == int(Year2))]
    
    a1=actors1.shape
    a2=actors2.shape
    
    if a1[0]==0 or a2[0]==0 :
        if a1[0]==0 and a2[0]==0 :
            resultat="Les informations renseignées pour le film 1 et 2 sont erronées.\nVérifiez les informations renseignées. PS : aidez vous des autres fonctionnalitées ;-)"
        elif a1[0]==0 :
            resultat="L'une des informations renseignées pour le film 1 est erronée.\nVérifiez les informations renseignées. PS : aidez vous des autres fonctionnalitées ;-)"
        elif a2[0]==0 :
            resultat="L'une des informations renseignées pour le film 2 est erronée.\nVérifiez les informations renseignées. PS : aidez vous des autres fonctionnalitées ;-)"
    
    else:
        # Saisi des set
        Actors_title1 = list(actors1['actors'])
        Actors_title1 = set(Actors_title1[0].split(","))
        
        Actors_title2 = list(actors2['actors'])
        Actors_title2 = set(Actors_title2[0].split(","))
    
        # Liste des acteurs communs aux deux films (s'il y en a)
        Common_Actors = list(Actors_title1.intersection(Actors_title2))
        
        if len(Common_Actors) != 0 :
            common_actors = ", ".join([str(_) for _ in Common_Actors])
            resultat="Titre 1 : {}  /  Année : {} \nTitre 2 : {}  /  Année : {} \n Common Actors : {}.".format(str(Title1), str(Year1), str(Title2), str(Year2),str(common_actors))
        else:
            resultat="Titre 1 : {}  /  Année : {} \nTitre 2 : {}  /  Année : {} \n Common Actors : ces films n'ont aucun acteurs en commun.".format(str(Title1), str(Year1), str(Title2), str(Year2))
    return resultat


def get_actor_info(df_names,df_movies,df_title_principals,Name):
    """
    The user enters the name of an actor: date of birth, biography, list of all movies in 
    who played this actor as well as all the co-stars of this actor, the average IMDb rating of the 
    films in which he has played, the maximum and minimum score (indicate for which films). 


    Parameters
    ----------
    df_names : dataframe
        IMDb movie database
    df_movies : dataframe
        IMDb movie database
    df_title_principals : dataframe
        IMDb movie database
    Name : string
        name of the actor entered by the user via the Tkinter interface

    Returns
    -------
    result : string
        result displayed in the graphical interface

    """
    
  # 1 - Extraction des informations sur l'acteur
    # Création d'un dataframe contenant des informmations sur l'acteur
    columns=['name','birth_details','place_of_birth','bio','date_of_death','reason_of_death','imdb_name_id']
    df_actor = df_names[columns]
    
    df_actor_info = df_actor.loc[df_actor['name'] == Name]
    
    # Gestion des erreurs de saisie 
    a=df_actor_info.shape
    if a[0]==0 :
        result="\n"+" Aucun résultat trouvé pour un acteur/une actrice au nom de "+Name+"."+"\n"
        result=result+" Veuillez respecter les majuscules et vérifier votre saisie. "
    
    # Recupération de l'info
    else: 
        id_name = df_actor_info.iloc[0,6]
    
        biography = list(df_actor_info['bio'])
        biography = ",".join([str(_) for _ in biography])
    
        birth_d = list(df_actor_info['birth_details'])
        birth_d = ",".join([str(_) for _ in birth_d])
        
        place_birth = list(df_actor_info['place_of_birth'])
        place_birth = ",".join([str(_) for _ in place_birth])
        
        date_death = list(df_actor_info['date_of_death'])
        date_death = ",".join([str(_) for _ in date_death])
        
        reasons_death = list(df_actor_info['reason_of_death'])
        reasons_death = ",".join([str(_) for _ in reasons_death])
         
   # 2 - Extraction des informmations contenues dans le dataframe Title principals
        
        # Filtrer le dataframe sur l'id name de l'acteur
        df_name_id = df_title_principals[(df_title_principals['imdb_name_id']== str(id_name))]
        
        # Récupérer l'ensemble des id title dans lequel l'acteur a joué
        df_movies_actor = df_name_id['imdb_title_id']
        
        df_title_id = pd.merge(df_movies_actor, df_movies, how='inner', on=['imdb_title_id'])
        
   # 3 - Finalisation des informations
        
        # Récupérer les titres et les co acteurs
        colonnes = ['title', 'actors']
        df_coactors = df_title_id[colonnes]
        
        # Créer une liste de tous les titres de films
        title_list = list(df_coactors['title'])
        
        # Transformer la liste des titres en chaîne de caractères
        title_list = ", ".join([str(_) for _ in title_list])
        
        # Créer une liste contenant les co acteurs et Séparation des élements de la liste
        coactors_list = list(df_coactors['actors'])
        
        coactors = []
        for element in coactors_list:
            coactors += element.split(",")
        
        # Suppression des doublons
        coactors = list(set(coactors))
        
        # Suppression de l'acteur étudié de la liste des co acteurs
        for i in coactors:
            if i == Name : 
                coactors.remove(i)
        
        # Transforme la liste des co acteurs en chaîne de caractère
        coactors = ",".join([str(_) for _ in coactors])
        nb_stars=len(coactors)
        
    # 4 - Filtre pour récupérer les notes
        moyenne=df_title_id['avg_vote'].mean(skipna=True)
        max_=df_title_id['avg_vote'].max(skipna=True)
        min_=df_title_id['avg_vote'].min(skipna=True)
        
        max_1=df_title_id[df_title_id['avg_vote']==df_title_id['avg_vote'].max()]
        min_1=df_title_id[df_title_id['avg_vote']==df_title_id['avg_vote'].min()]
        title_max=max_1['original_title'].to_string(index=False)
        title_min=min_1['original_title'].to_string(index=False)
        
    # 5 - On prépare l'affichage du résultat
        result=""
        result=result+"Nom de l'acteur: "+Name+"\n"+"\n"
        result=result+"Biographie :\n"+biography+"\n"+"\n"
        result=result+"Details sur la naissance de "+Name+": "+birth_d+"\n"+"\n"
        result=result+"Lieu de naissance: "+place_birth+"\n"+"\n"
        result=result+"Malheuresement, "+Name+" est mort le "+date_death+"\n"+"\n"
        result=result+"La (Les) cause(s) de sa mort est (sont): "+reasons_death+"\n"+"\n"
        result=result+"Listes des films dans lequel il/elle a joué: "+title_list+"\n"+"\n"
        result=result+"Note moyenne sur IMDb des films dans lequel il a joué: "+str(round(moyenne,1))+"\n"+"\n"
        result=result+"Note maximum sur IMDb des films dans lequel il a joué: "+str(max_)+", Titre : "+title_max+"\n"+"\n"
        result=result+"Note minimum sur IMDb des films dans lequel il a joué: "+str(min_)+", Titre : "+title_min+"\n"+"\n"
        result=result+"Cet(te) acteur(trice)"+" a joué aux côtés de "+str(nb_stars)+" acteurs dans sa carrière dont :\n"
        result=result+coactors
    return result


def get_best_movie(df_movies,Year,Genre):
    """
    The user enters a year and a gender and the function returns a file containing a top 3 
    the best movies (the sorting key is the movies with the best rating by the users)

    Parameters
    ----------
    df_movies : dataframe
        IMDb movie database
    Year : int
        year of the movie entered by the user via the Tkinter interface
    Genre : string
        genre of the movie entered by the user via the Tkinter interface

    Returns
    -------
    resulta : string
        result displayed in the graphical interface

    """
    
    Genre=Genre.lower() 
    
  # 1 - Filtrer le dataframe sur deux colonnes
    df_filtered = df_movies[(df_movies['genre_low']== str(Genre)) & (df_movies['year']== int(Year))]
    
  # 2 - Trier le dataframe par la colonne avg_vote par ordre décroissant
    df_filtered_sort = df_filtered.sort_values(by = 'avg_vote',ascending=False)
    df_BestMovies = df_filtered_sort.head(3)
    
  # 3 - Créer un nouveau dataframe
    columns = ['title','avg_vote','genre', 'year']
    df_m = df_BestMovies[columns]
    
    title_list4 = list(df_m['title'])
    avg_vote_list4 = list(df_m['avg_vote'])
    
  # 4 - Gestion des erreurs de saisie
    if len(df_m['title']) > 0:
        resulta=""
        n = len(title_list4)
        resulta="Top 3 des films ayant eu la meilleur note par les utilisateurs pour l'année "+str(Year)+" et le genre "+Genre+":"+"\n"+"\n"
        for i in range(0,n): 
            resulta=resulta+str(i+1)+"- "+str(title_list4[i])+", "+str(avg_vote_list4[i])+"/10"+"\n"+"\n"
     
    elif len(df_m['title']) == 0:
        resulta="\nAucun résultat pour les films répertoriés en "+str(Year)+" appartenant au genre "+Genre+".\n"
        resulta=resulta+"Veuillez revoir la saisie et réécrire les genres an anglais séparées de virgules."
    return resulta


def get_movie_advice(df_movies,Genre,Year,Duration,Avg_vote):
    """
    This is a function that uses the information entered by the user via the Tkinter interface.
    to offer him films that correspond to his expectations

    Parameters
    ----------
    df_movies : dataframe
        IMDb movie database
    Genre : string
        genre of the movie entered by the user via the Tkinter interface
    Year : int
        year of the movie entered by the user via the Tkinter interface
    Duration : float
        duration of the movie entered by the user via the Tkinter interface
    Avg_vote : float
        average vote of the movie entered by the user via the Tkinter interface

    Returns
    -------
    resulta : string
        result displayed in the graphical interface

    """
    
    Genre = Genre.lower()
    
  # 1 - Filtrer le dataframe 
    df_filtered = df_movies[(df_movies['genre_low']== str(Genre)) & 
                            (df_movies['year']== int(Year)) &
                            (df_movies['duration']>= int(Duration)) & 
                            (df_movies['avg_vote']>= float(Avg_vote))]
    df_filtered = df_filtered.sort_values(by = 'avg_vote',ascending=False)
    
  # 2 - Récupération des informations
    list_genre = list(df_filtered['genre'])
    list_year = list(df_filtered['year'])
    list_title = list(df_filtered['title'])
    list_duration = list(df_filtered['duration'])
    list_country = list(df_filtered['country'])
    list_language = list(df_filtered['language'])
    list_avg_vote = list(df_filtered['avg_vote'])
    
  # 3 - Gestion des erreurs de saisie
    if len(df_filtered['title']) != 0:
        resulta=""
        n = len(list_genre)
        resulta="Voici le(s) film(s) trouvé(s) qui correpond(ent) à vos critères : \n"
        for i in range(0,n): 
            resulta=resulta+str(i+1)+"- "+"Titre du film : "+str(list_title[i])+"\n"+"\n"
            resulta=resulta+"Genre : "+str(list_genre[i])+"\n"+"\n"
            resulta=resulta+"Année de sortie : "+str(list_year[i])+"\n"+"\n"
            resulta=resulta+"Durée : : "+str(list_duration[i])+" minutes \n"+"\n"
            resulta=resulta+"Pays du film : "+str(list_country[i])+"\n"+"\n"
            resulta=resulta+"Langues originelle : "+str(list_language[i])+"\n"+"\n"
            resulta=resulta+"Note moyenne : "+str(list_avg_vote[i])+"/10 \n"+"\n"
            resulta=resulta+"---------------------------------------------------------------------------------------------"+"\n"+"\n"
     
    elif len(df_filtered['title']) == 0:
        resulta="\nAucun résultat pour les films répertoriés en "+str(Year)+" appartenant au genre "+Genre+", pour les crières de "+str(Duration)+" minutes et pour une note moyenne de "+str(Avg_vote)+"/10."+"\n"
        resulta=resulta+"Veuillez revoir vos critères saisies et réécrire les genres an anglais séparées de virgules."
    return resulta


def get_commun_films(df_movies,Actor1,Actor2):
    """
    Function that gives the movies in which two actors have played

    Parameters
    ----------
    df_movies : dataframe
        IMDb movie database
    Actor1 : string
        name of the first actor entered by the user via the Tkinter interface
    Actor2 : string
        name of the second actor entered by the user via the Tkinter interface

    Returns
    -------
    result : string
        result displayed in the graphical interface

    """
    
    Actor1 = Actor1.lower() 
    Actor2 = Actor2.lower() 
    
 # 1 - Constitution du dataframe
    
    # Filtrage film avec le nom des acteurs
    df=df_movies[df_movies['actors_low'].str.contains(Actor1,na=False)]
    df=df_movies[df_movies['actors_low'].str.contains(Actor2,na=False)]

 # 2 - Extraction de l'information    
    list_film=list(df['original_title'])
    
    liste=""
    for element in list_film: 
        liste=liste+"- "+element+"\n"
    
 # 3- On stock toute l'information récupéré dans une variable char appelé result
    if liste=="" :
        result="Ces 2 acteurs n'ont pour l'instant joué dans aucun film ensemble."
    else:
        result="Ces 2 acteurs ont joué ensemble dans les films suivant :\n"+liste
    return result