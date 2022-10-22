import sqlite3

class ScoreDatabase():

    def __init__(self):
        self.con = sqlite3.connect("scores.db")
        self.cur = self.con.cursor()
        try:
            self.cur.execute("CREATE TABLE scores(name, score)")
        except sqlite3.OperationalError as ex:
            if not "table scores already exists" in str(ex):
                raise ex


    def get_best_scores(self):
        res = self.cur.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 3")
        result = res.fetchall()
        return result


    def add_score(self, name, score):
        self.cur.execute(f"INSERT INTO scores VALUES ('{name}', {int(score)})")
        self.con.commit()

    def close_connection(self):
        self.con.close()


