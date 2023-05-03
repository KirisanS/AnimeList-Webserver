import os;
import sqlite3;


class Database():

    def __init__(self, reset=False):
        if (reset == True):
            if(os.path.isfile('Animes.db')):
                os.remove('Animes.db')
        self.data = sqlite3.connect('Animes.db')

    def create_tables(self):
      self.data.execute("""CREATE TABLE IF NOT EXISTS Animes     
                  ( ANIME_ID    INTEGER     PRIMARY KEY     AUTOINCREMENT   NOT NULL,
                    ANIME_NAME  VARCHAR(64) NOT NULL,
                    GENRE       VARCHAR(64) NOT NULL,
                    AUTHOR_NAME VARCHAR(32) NOT NULL );""") 
      
      self.data.execute("""CREATE TABLE IF NOT EXISTS Mangas 
                  ( MANGA_ID    INTEGER     PRIMARY KEY     AUTOINCREMENT   NOT NULL,
                    MANGA_NAME  VARCHAR(64) NOT NULL, 
                    GENRE       VARCHAR(64) NOT NULL,
                    AUTHOR_NAME VARCHAR(32) NOT NULL );""")

      self.data.execute("""CREATE TABLE IF NOT EXISTS AnimeRatings 
                  ( ANIME_ID    INTEGER     NOT NULL,
                    EMOTIONAL   INTEGER     NOT NULL,
                    ACTION      INTEGER     NOT NULL,
                    ROMANCE     INTEGER     NOT NULL, 
                    FOREIGN KEY (ANIME_ID)  REFERENCES Animes);""")
      
      self.data.execute("""CREATE TABLE IF NOT EXISTS MangaRatings 
                  ( MANGA_ID    INTEGER     NOT NULL,
                    EMOTIONAL   INTEGER     NOT NULL,
                    ACTION      INTEGER     NOT NULL,
                    ROMANCE     INTEGER     NOT NULL, 
                    FOREIGN KEY (MANGA_ID)  REFERENCES Mangas);""")
      

    def __setitem__(self, table, values):
      tempString = "( " + "?, "*(len(values)-1) + "? " + ")"

      self.data.execute(f"""INSERT OR IGNORE
                            INTO    {table}
                            VALUES  {tempString} ;""", values)
      
    
    def add_anime(self, values, ratings):

      self.__setitem__('Animes', (None, values[0], values[1], values[2]))
      animeID = self.data.execute(f"""SELECT ANIME_ID FROM Animes
                                      ORDER BY ANIME_ID DESC LIMIT 1 """).fetchone()

      self.__setitem__('AnimeRatings', (animeID[0], ratings[0], ratings[1], ratings[2]))
      self.data.commit()

    def add_manga(self, values, ratings):
       
      self.__setitem__('Mangas', (None, values[0], values[1], values[2]))
      mangaID = self.data.execute(f"""SELECT MANGA_ID FROM Mangas
                                      ORDER BY MANGA_ID DESC LIMIT 1 """).fetchone()
      self.__setitem__('AnimeRatings', (mangaID[0], ratings[0], ratings[1], ratings[2]))
      self.data.commit()
      
       




if __name__ == "__main__":
    db = Database(reset=True)
    db.create_tables()

    db.add_anime(("Oshi No Ko", "Scary", "JpnDude"), (2, 7, 5))
    db.add_anime(("Kaguya", "RomCom", "SomeGuy"), (3, 4, 9))
    db.add_anime(("Magi", "Action", "WowieGuy"), (5, 2, 1))