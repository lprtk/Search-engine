"""
  * This file is part of project Creation-of-a-search-engine. 
    It's copyrighted by the contributors
  * Copyright (c) 2021 lprtk
"""

"""
Modul which contains all the codes for the graphical interface.
"""

########################################################################################
                             ## Librairies loading ##
########################################################################################


import function_imdb as im
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as ScrolledText
from tkinter.messagebox import *

########################################################################################
                               ## Modul function ##
########################################################################################

def interface(path,df_names,df_movies,df_ratings,df_title_principals):
    
    root = tk.Tk() # Creates a tkinter object
    label = tk.Label(root, text="Welcome on Akinator'movies version",
                     font=("Helvetica", 20), bg='grey', fg='white')
    root.config(background='grey')
    root.title("IMDb application")
    label.pack()
     

    def action_1():
        text_area.config(state="normal")
        text_area.delete(1.0,tk.END)
        text_area.insert(tk.INSERT,im.get_movie_info(df_movies,df_ratings,arg_1.get()))
        text_area.configure(state='disabled')
    
        
    def action_2():
        text_area.config(state="normal")
        text_area.delete(1.0,tk.END) #delete scrolledtext content
        text_area.insert(tk.INSERT,im.get_commun_actors(df_movies,arg_2.get(),int(arg_3.get()),arg_4.get(),int(arg_5.get())))
        text_area.configure(state='disabled')
    
    def action_3():
        text_area.config(state="normal")
        text_area.delete(1.0,tk.END)
        text_area.insert(tk.INSERT,im.get_actor_info(df_names,df_movies,df_title_principals,arg_6.get()))
        text_area.configure(state='disabled')
    
    def action_4():
        text_area.config(state="normal")
        text_area.delete(1.0,tk.END)
        text_area.insert(tk.INSERT,im.get_best_movie(df_movies,int(arg_7.get()),arg_8.get()))
        text_area.configure(state='disabled')
        
    def action_5():
        text_area.config(state="normal")
        text_area.delete(1.0,tk.END)
        text_area.insert(tk.INSERT,im.get_movie_advice(df_movies,arg_9.get(),int(arg_10.get()),int(arg_11.get()),float(arg_12.get())))
        text_area.configure(state='disabled')
        
    def action_6():
        text_area.config(state="normal")
        text_area.delete(1.0,tk.END)
        text_area.insert(tk.INSERT,im.get_commun_films(df_movies,arg_13.get(),arg_14.get()))
        text_area.configure(state='disabled')
    
    def destroy():
        if askyesno('Quit IMDd application', 'Are you sure you want to do this?'):
            showwarning('Quit IMDd application', 'Thank you, see you soon!')
            root.destroy()
        
        
    ### Frame 1  : menu des actions possibles  
    ### Scrollable frame
    frame1 = tk.Frame(root)
    canvas = tk.Canvas(frame1, width=200, height=600)
    scrollbar = tk.Scrollbar(frame1, orient="vertical", command=canvas.yview)
    scrollFrame = tk.Frame(canvas,borderwidth=0, relief=tk.GROOVE)
    
    scrollFrame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollFrame, anchor="nw")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    frame1.pack(side=tk.LEFT, padx=10, pady=10)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    ### fonction get_movie_info
    framef1 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
    framef1.pack(side=tk.TOP, padx=1, pady=1)   
    
    label = tk.Label(framef1, text="Movie information", font=("Helvetica", 12))
    label.pack()
    label = tk.Label(framef1, text="Nom du film", font=("Helvetica", 10))
    label.pack()
    arg_1 = tk.Entry(framef1, width=30, font=("Helvetica", 10)) # argument de la fonction
    arg_1.pack()
    bouton_f1 = tk.Button(framef1, text="Search", font=("Helvetica", 10), bg='red', fg='white', command=action_1)
    bouton_f1.pack()
    
    
    ### fonction get_commun_actors
    framef2 = tk.Frame(scrollFrame, borderwidth=2,highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
    framef2.pack(side=tk.TOP, padx=1, pady=1)     
    
    label = tk.Label(framef2, text="Common actors", font=("Helvetica", 12))
    label.pack()
    label = tk.Label(framef2, text="First movie's name", font=("Helvetica", 10))
    label.pack()
    arg_2 = tk.Entry(framef2, width=30, font=("Helvetica", 10))
    arg_2.pack()
    label = tk.Label(framef2, text="Year of movies 1", font=("Helvetica", 10))
    label.pack()
    arg_3 = tk.Entry(framef2, width=30, font=("Helvetica", 10))
    arg_3.pack()
    label = tk.Label(framef2, text="Second movie's name", font=("Helvetica", 10))
    label.pack()
    arg_4 = tk.Entry(framef2, width=30, font=("Helvetica", 10))
    arg_4.pack()
    label = tk.Label(framef2, text="Year of movie 2", font=("Helvetica", 10))
    label.pack()
    arg_5 = tk.Entry(framef2, width=30, font=("Helvetica", 10))
    arg_5.pack()
    bouton_f2 = tk.Button(framef2, text="Search", font=("Helvetica", 10), bg='red', fg='white', command=action_2)
    bouton_f2.pack()
    
    
    ### fonction get_actor_info
    framef3 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="red",relief=tk.GROOVE)
    framef3.pack(side=tk.TOP, padx=1, pady=1)     
    
    label = tk.Label(framef3, text="Actor information", font=("Helvetica", 12))
    label.pack()
    label = tk.Label(framef3, text="Actor's name", font=("Helvetica", 10))
    label.pack()
    arg_6 = tk.Entry(framef3, width=30, font=("Helvetica", 10))
    arg_6.pack()
    bouton_f3 = tk.Button(framef3, text="Search", font=("Helvetica", 10), bg='red', fg='white', command=action_3)
    bouton_f3.pack()
    
    
    ### fonction get_best_movie
    framef4 = tk.Frame(scrollFrame, borderwidth=2,highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
    framef4.pack(side=tk.TOP, padx=1, pady=1)     
    
    label = tk.Label(framef4, text="Best movie", font=("Helvetica", 12))
    label.pack()
    label = tk.Label(framef4, text="Year", font=("Helvetica", 10))
    label.pack()
    arg_7 = tk.Entry(framef4, width=30, font=("Helvetica", 10))
    arg_7.pack()
    label = tk.Label(framef4, text="Genre(s)", font=("Helvetica", 10))
    label.pack()
    arg_8 = tk.Entry(framef4, width=30, font=("Helvetica", 10))
    arg_8.pack()
    bouton_f4 = tk.Button(framef4, text="Search", font=("Helvetica", 10), bg='red', fg='white', command=action_4)
    bouton_f4.pack()
    
    
    ### fonction get_commun_actors
    framef5 = tk.Frame(scrollFrame, borderwidth=2,highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
    framef5.pack(side=tk.TOP, padx=1, pady=1)     
    
    label = tk.Label(framef5, text="Movie advice", font=("Helvetica", 12))
    label.pack()
    label = tk.Label(framef5, text="Genre", font=("Helvetica", 10))
    label.pack()
    arg_9 = tk.Entry(framef5, width=30, font=("Helvetica", 10))
    arg_9.pack()
    label = tk.Label(framef5, text="Year", font=("Helvetica", 10))
    label.pack()
    arg_10 = tk.Entry(framef5, width=30, font=("Helvetica", 10))
    arg_10.pack()
    label = tk.Label(framef5, text="Minimum duration", font=("Helvetica", 10))
    label.pack()
    arg_11 = tk.Entry(framef5, width=30, font=("Helvetica", 10))
    arg_11.pack()
    label = tk.Label(framef5, text="Minimum avg note", font=("Helvetica", 10))
    label.pack()
    arg_12 = tk.Entry(framef5, width=30, font=("Helvetica", 10))
    arg_12.pack()
    bouton_f5 = tk.Button(framef5, text="Search", font=("Helvetica", 10), bg='red', fg='white', command=action_5)
    bouton_f5.pack()
    
    
    ### fonction get_commun_film
    framef6 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
    framef6.pack(side=tk.TOP, padx=1, pady=1)     
    
    label = tk.Label(framef6, text="Common movies", font=("Helvetica", 12))
    label.pack()
    label = tk.Label(framef6, text="First actor's name", font=("Helvetica", 10))
    label.pack()
    arg_13 = tk.Entry(framef6, width=30, font=("Helvetica", 10))
    arg_13.pack()
    label = tk.Label(framef6, text="Second actor's name", font=("Helvetica", 10))
    label.pack()
    arg_14 = tk.Entry(framef6, width=30, font=("Helvetica", 10))
    arg_14.pack()
    bouton_f6 = tk.Button(framef6, text="Search", font=("Helvetica", 10), bg='red', fg='white', command=action_6)
    bouton_f6.pack()
    
    
    ### fonction get_commun_film
    framef7 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
    framef7.pack(side=tk.TOP, padx=1, pady=1) 
    
    bouton_f7 = tk.Button(framef7, text="Quit", font=("Helvetica", 10), bg='white', fg='red', command=destroy)
    bouton_f7.pack()
    
    
    ### Frame 2 : affichage du résultat
    
    frame2 = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
    frame2.pack(side=tk.TOP, padx=10, pady=10)
    text_area = ScrolledText(frame2, width = 850,  height = 1000) 
    text_area.config(state="normal")
    text_default = """All the results which are asked will be printed here !\n
                \n
                \nThe fonctionalities of moteur search are described below: 
                \n-> Movie informations give a lot of informations about a movie or a word of the title.
                \n-> Commun actors give the actors who have played in the two movies.
                \n-> Actor information give some personal informations about an actor .
                \n-> Best movie provides for one year as well as one or more given genres the top 3 films according to their scores. 
                \n-> Movie advice gives one or more movies that you should watch according to your tastes.
                \n-> Common movies provides the list of films common to 2 actors."""
    text_area.insert(tk.INSERT,text_default)
    text_area.configure(state='disabled')
    text_area.pack()
    root.mainloop()


