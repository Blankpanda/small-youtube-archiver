import db
import archiver
import models
def main():
    a = archiver.archiveManager()

    # a.create_new_archive("test")
    # a.create_new_archive("test2")
    # a.create_new_archive("test3")
    
   # b = a.find_archive_by_name("test")
    #print(b.get_archive_name())
    
    # a.delete_archive("test")
    # a.delete_archive("test2")
    # a.delete_archive("test3")

    a.create_new_archive("bucky_bois")
    b = a.find_archive_by_name("bucky_bois")
    video = models.videoItem("bucky_bois","https://test.com","where''s waldo warriors win big","haha",1,10,0,"archives/bucky_bois/wwwb.mp4")
    print(video.items)
    b.add_to_archive("htts://test.com",video)
    
    
if __name__ == '__main__':
    main()
