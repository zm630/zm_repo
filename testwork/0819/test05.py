class Book():
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def __str__(self):
        return (f"编号：{self.id},书名：{self.name},价格：{self.price}")

book1=Book(1, "好", 99)
book2=Book(2, "一般", 52)
book3=Book(3, "不好", 7)
books=[book1,book2,book3]
exspensive=max(books,key=lambda book:book.price)
print(exspensive)


