import tkinter as tk
from tkinter import *
from lyrics_extractor import SongLyrics

window = Tk()  # creating window
window.geometry('600x600')  # giving size
window.title('PythonGeeks')  # giving title
head = Label(window, text="Enter the song you want Lyrics for",
             font=('Calibri 15'))  # a label
head.pack(pady=20)
result = tk.StringVar()  # ensuring result is string type
song = tk.StringVar()  # ensuring song is string type


def get_lyrics():
    song_name = song.get()  # using get method getting value of song
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    # going to the website for which we have got the engine id
    extract_lyrics = SongLyrics(api_key, engine_id)
    song_lyrics = extract_lyrics.get_lyrics(song_name)  # getting the lyrics
    result.set(song_lyrics)  # setting the result


Entry(window, textvariable=song).pack()  # enter a song name
Message(window, textvariable=result, bg="light grey").pack(
    side=TOP, anchor=W, fill=BOTH, expand=1)  # displaying the lyrics
# create a button
Button(window, text="GO", command=get_lyrics).pack()

window.mainloop()  # start the GUI event loop
# This code creates a simple GUI application that allows users to enter a song name and retrieve its
# lyrics using the Lyrics Extractor API. The user inputs the song name, clicks the "GO" button,
