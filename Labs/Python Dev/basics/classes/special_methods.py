# __init__()
# __str__()
# __len__()
# __del__()

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"{self.title} Created")
    def __str__(self):
        return f"title:{self.title}, author:{self.author}, pages:{self.pages},"
    def __len__(self):
        return self.pages
    def __del__(self):
        print(f"{self.title} has been deleted")
    
b1 = Book('Coading Brains', 'Awais', 150)
b2 = Book('Example Book', 'Example Author', 75)

print(b1)
print(len(b1))

print(b2)
print(len(b2))

del(b1)
del(b2)