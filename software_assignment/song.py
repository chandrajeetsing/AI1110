import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import numpy as np

# Initialize the mixer
mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Player")
window.geometry("400x400")

# Create a playlist to store the songs
playlist = []
current_song_index = 0

def add_song():
    """Add songs to the playlist."""
    filetypes = (("MP3 Files", "*.mp3"), ("All files", "*.*"))
    songs = filedialog.askopenfilenames(filetypes=filetypes)
    for song in songs:
        playlist.append(song)
    update_playlist_listbox()

def remove_song():
    """Remove the selected song from the playlist."""
    selection = playlist_listbox.curselection()
    if selection:
        index = int(selection[0])
        playlist.pop(index)
        update_playlist_listbox()

def play_song(index):
    """Play a song from the playlist at the given index."""
    if index < len(playlist):
        mixer.music.stop()  # Stop the currently playing song (if any)
        song = playlist[index]
        mixer.music.load(song)
        mixer.music.play()


# ...

def play_random_song():
    """Play a random song from the playlist."""
    if playlist:
        mixer.music.stop()  # Stop the currently playing song (if any)
        random_index = np.random.randint(len(playlist))
        play_song(random_index)


# ...

def play_all_songs_randomly():
    """Play all songs in the playlist at once in random order."""
    if playlist:
        mixer.music.stop()  # Stop the currently playing song (if any)
        random_order = np.random.permutation(len(playlist))
        played_songs = set()  # Keep track of the played songs
        for index in random_order:
            song = playlist[index]
            if song not in played_songs:
                mixer.music.load(song)
                mixer.music.play()
                while mixer.music.get_busy():
                    continue
                played_songs.add(song)


def stop_song():
    """Stop the currently playing song."""
    mixer.music.stop()

def next_song():
    """Play the next song in the playlist."""
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_song()



def update_playlist_listbox():
    """Update the playlist listbox with the current playlist."""
    playlist_listbox.delete(0, tk.END)
    for song in playlist:
        playlist_listbox.insert(tk.END, os.path.basename(song))

# Create the GUI elements
add_button = tk.Button(window, text="Add Song", command=add_song)
add_button.pack(pady=10)

remove_button = tk.Button(window, text="Remove Song", command=remove_song)
remove_button.pack(pady=10)

playlist_listbox = tk.Listbox(window, width=40, height=10)
playlist_listbox.pack(pady=10)

play_button = tk.Button(window, text="Play Random Song", command=play_random_song, relief=tk.RAISED, borderwidth=5)
play_button.pack()

play_all_button = tk.Button(window, text="Play All Songs Randomly", command=play_all_songs_randomly, relief=tk.RAISED,
                            borderwidth=5)
play_all_button.pack()

stop = tk.Button(window, text="Stop current song", command=stop_song, relief=tk.RAISED, borderwidth=5)
stop.pack()

next_button = tk.Button(window, text="Next Song", command=next_song, relief=tk.RAISED, borderwidth=5)
next_button.pack()

status_label = tk.Label(window, text="Status: Stopped", anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Function to update the status label
def update_status_label():
    if mixer.music.get_busy():
        status_label.config(text=f"Status: Playing - {os.path.basename(playlist[current_song_index])}")
    else:
        status_label.config(text="Status: Stopped")

# Update the status label periodically
def update_status_periodically():
    update_status_label()
    window.after(1000, update_status_periodically)

update_status_periodically()

# Run the main event loop
window.mainloop()


