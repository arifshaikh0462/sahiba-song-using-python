import pygame
import time
import threading

SONG_FILE = "song.mpeg"
LYRICS_FILE = "lyrics.txt"

CHAR_DELAY = 0.05
LINE_DELAY = 1.2


def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load(SONG_FILE)
    pygame.mixer.music.play()

def show_lyrics():
    try:
        with open(LYRICS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            for char in line:
                print(char, end="", flush=True)
                time.sleep(CHAR_DELAY)
            time.sleep(LINE_DELAY)

    except FileNotFoundError:
        print("❌ lyrics.txt file not found!")

# Run song in background
song_thread = threading.Thread(target=play_song)
song_thread.start()

# Show lyrics
show_lyrics()

# Keep program alive until song ends
while pygame.mixer.music.get_busy():
    time.sleep(1)