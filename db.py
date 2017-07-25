import sqlite3

class database:
    "manage database connections and transactions"
    _database_name = ""
    _db_object = None
    _db_cursor = None

    def get_db_name(self):
        return _database_name

    def get_db_object(self):
        return db_object
    
    def __init__(self,database_name):
        "Constructor"
        self._database_name = database_name
        self.connect_db(None)
        self._db_cursor = None
                            
    def connect_db(self,new_database):
        # just to be safe, were going to close the connection
        if(new_database is None):
            self._db_object = sqlite3.connect(self._database_name)
        else:
            self.close_db()
            self._db_object = sqlite3.connect(new_database)
            
    def execute_sql(self,sql):
        self._db_cursor = self._db_object.cursor()
        #todo, a ton of error checking
        data = self._db_cursor.execute(sql)
        self._save_changes()
        return data

    def _save_changes(self):
        self._db_object.commit()
    
    def close_db(self):
        self._db_object.close()

    
