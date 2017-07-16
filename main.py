import db
import archiver
def main():
    a = archiver.archiveManager()

    # a.create_new_archive("test")
    # a.create_new_archive("test2")
    # a.create_new_archive("test3")
    
    b = a.find_archive_by_name("test")
    #print(b.get_archive_name())
    
    # a.delete_archive("test")
    # a.delete_archive("test2")
    # a.delete_archive("test3")
            
    
if __name__ == '__main__':
    main()
