print("Om Nimmalwar")
class Library:

    def __init__(self):
        self.acc_number = ""
        self.title = ""
        self.author = ""
        self.publisher = ""

   
    def read(self):
        self.acc_number = input("Enter Accession Number: ")
        self.title = input("Enter Title of Book: ")
        self.author = input("Enter Author Name: ")
        self.publisher = input("Enter Publisher Name: ")

    
    def compute(self):
        days = int(input("Enter number of days late: "))
        fine = days * 5       
        print("Fine Amount = Rs.", fine)


    def display(self):
        print("\n--- BOOK DETAILS ---")
        print("Accession Number :", self.acc_number)
        print("Title            :", self.title)
        print("Author           :", self.author)
        print("Publisher        :", self.publisher)


obj = Library()

obj.read()
obj.display()
obj.compute()
