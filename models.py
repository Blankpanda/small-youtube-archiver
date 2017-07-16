class videoItem:
    items = {}
    def __init__(self,channel,url,title,description,likes,dislikes,tags_id,file_path):
        self.items['channel'] = channel
        self.items['url'] = url
        self.items['title'] = title
        self.items['description'] = description
        self.items['likes'] = likes
        self.items['dislikes'] = dislikes
        self.items['tags_id'] = tags_id
        self.items['file_path'] = file_path
