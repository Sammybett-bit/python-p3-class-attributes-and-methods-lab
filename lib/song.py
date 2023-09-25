# class Song:
#     pass
class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.count += 1
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    @classmethod
    def add_to_artists(self, artist):
        if artist not in self.artists:
            self.artists.append(artist)

    @classmethod
    def add_to_genre_count(self, genre):
        if genre in self.genre_count:
            self.genre_count[genre] += 1
        else:
            self.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(self, artist):
        if artist in self.artist_count:
            self.artist_count[artist] += 1
        else:
            self.artist_count[artist] = 1