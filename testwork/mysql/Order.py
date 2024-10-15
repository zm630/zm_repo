class Order():
    id = None
    date = None
    money = None
    province = None
    def __init__(self,id,date,money,province):
        self.id=id
        self.date=date
        self.money=money
        self.province=province
    def __str__(self):
        return self.id+"--"+self.date+"--"+self.money+"--"+self.province