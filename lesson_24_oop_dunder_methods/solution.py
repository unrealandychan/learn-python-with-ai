
# Lesson 24: Solution

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self.songs)} songs."

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

my_playlist = Playlist("Rock Anthems", ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"])

print(my_playlist)
print("Number of songs:", len(my_playlist))
print("First song:", my_playlist[0])
