class Course():

    def __init___(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = int(price)
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self. avg_rating = 0
    
    def __str__(self):
        return(f'Title: {self.title}\nInstructor: {self.instructor}\nAverage ratings: {self.avg_rating}\nUsers: {self.users}\n')
    
    def new_user_enrolled(self, new_user):
        self.users.append(new_user)
    
    def received_a_rating(self, new_rating):
        self.avg_rating = (self.avg_rating * self.ratings + new_rating) / (self.ratings + 1)
        self.ratings += 1 
    
    def show_details(self):
        print('Course Title: ', self.title)
        print('Intructor: ', self.instructor)
        print('Price: ', self.price)
        print('Number of Lectures: ', self.lectures)
        print('Users: ', self.users)
        print('Average rating: ', self.avg_rating)

    
class VideoCourse(Course):
    
    def __init__(self, title, instructor, lectures, price, length_video):
        super().__init__(title, instructor, lectures, price)
        self.length_video = length_video
 
    def show_details(self):
        super().show_details()
        print('Video Length : ', self.length_video)
        
        
class PdfCourse(Course):

    def __init__(self, title, instructor, lectures, price, pages):
        super().__init__(title, instructor, lectures, price)
        self.pages = pages
 
    def show_details(self):
        super().show_details()
        print('Number of pages : ', self.pages)
 
 
vc = VideoCourse('Learn C++', 'Jack', 30, 50, 10)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Max')
vc.new_user_enrolled('Tom')
vc.received_a_rating(3)
vc.received_a_rating(5)
vc.received_a_rating(4)
vc.show_details()
 
print()
 
pc = PdfCourse('Learn Java', 'Jim', 35, 50, 1000)
pc.new_user_enrolled('Allen')
pc.new_user_enrolled('Mary')
pc.new_user_enrolled('JIm')
pc.received_a_rating(5)
pc.received_a_rating(4)
pc.received_a_rating(4.5)
pc.show_details()