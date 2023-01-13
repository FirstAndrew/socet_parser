from classes.good import Good

class Good_details(Good) :
    def __init__(self, Name, Price, Photo, Link, photos, description, characteristic):
        super().__init__(Name, Price, Photo, Link)        
        self.id = 0
        self.photos = photos
        self.description = description
        self.charact = characteristic
        