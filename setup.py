import db
import os
def main():

    #create archive directory
    if not os.path.exists('archives'):
        os.makedirs('archives')
    # TODO: encase in try catch
    # create database file
    database_file = open("archive/Videos.db",'w')
    database_file.close()

    videos_database = db.database("archive/Videos.db")
    sql_string = ("CREATE TABLE Videos(" +
#                       "id PRIMARY KEY," +
                       "channel text," +
                       "url text," +
                       "title text," +
                       "description text," +
                       "likes int," +
                       "dislikes int," +
                       "tags_id int," +
                       "file_path text);")
                       
    videos_database.execute_sql(sql_string)

    # todo: other tables
    videos_database.close_db()


    
if __name__ == '__main__':
    main()
