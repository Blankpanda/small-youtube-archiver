import db
import os
import shutil
import helpers

from random import *

class archiveManager:
    "manage archives"
    _archives_list = []
    
    def __init__(self):
        self._load_archives()

    def _load_archives(self):
        archive_list = self._get_archive_folders()
        for i in range(0,len(archive_list)):
            tmparchive = archive("archives/" + archive_list[i] + "/" + archive_list[i] + ".db")
            self._archives_list.append(tmparchive)
    
    def list_archives(self):
        # TODO more information
        archive_list = self._get_archive_folders()
        print("\n".join(archive_list))
        

    def create_new_archive(self,name):
#        new_name = self._create_random_key() + "-" + name
        if not os.path.exists("archives"):
            os.makedirs("archives")
            
        if os.path.exists("archives" + "/" + name):
            print("archive already exists!")
            return None        
        os.makedirs("archives/" + name)        
               
        tmpdb = db.database("archives/" + name + "/" + name + ".db")
        create_string = ("CREATE TABLE Videos(" +
#                       "id PRIMARY KEY," +
                       "channel text," +
                       "url text," +
                       "title text," +  
                       "description text," +
                       "likes int," +
                       "dislikes int," +
                       "tags_id int," +
                       "file_path text);")
        tmpdb.execute_sql(create_string)
        tmpdb.close_db()
        
        print("Archive created! path=" + 'archives' + "/" + name)
        new_archive = archive("archives/" + name + "/" + namse + ".db")
        self._archives_list.append(new_archive)
        return new_archive

    def delete_archive(self,name):
        archive = self.find_archive_by_name(name)
        for i in range(0,len(self._archives_list)):
            if(archives[i] == name):
                shutil.rmtree("archives/"+name)
        self.archives_list.remove(archive)


    def find_archive_by_name(self,name):
        # do a good search algorithm?
        for i in range(0, len(self._archives_list)):
            if self._archives_list[i].get_archive_name() == name:
                return self._archives_list[i]

    def _create_random_key(self):
        rands =  []
        for i in range(0,4):
            rands.append(chr(randint(97,122)))
        return "".join(rands)

    def _get_archive_folders(self):
        return [name for name in os.listdir('archives/') if os.path.isdir(os.path.join("archives/",name))]
            
        

class archive:
    _db = None
    _archive_name = ""
    _db_name = ""
    _dir_path = ""    
    def __init__(self,database):
        self._archive_name = database.split("/")[1:2][0]
        self._dir_path = "/".join(database.split("/")[:2])    
        self._db_name = database
        self._db = db.database(database)


    def get_archive_name(self):
        return self._archive_name

    def get_db_name(self):
        return self._db_name
    
    def get_dir_path(self):
        return self._dir_path
                       
    def add_to_archive(self,url,video_item):
        #created file from youtube-dl, lets say
        f = open("archives/" + self._archive_name + "/" + video_item.items['title']+".mp4",'w')
        f.close()
        # insert it into the table as well
        # check by title to see if this video already exists, dont add it if nessecary.
        sql = "INSERT INTO Videos VALUES " + helpers.create_sql_list(video_item.items);
        print(sql)
        self._db.execute_sql(sql)
        
    
    def delete_from_archive(self,name):
        # assuming everything is a .mp4
        os.remove(name + ".mp4")
        sql = ""
        

    def list_archived(self):
        self._db.execute(sql)
    
