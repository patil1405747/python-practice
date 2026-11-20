#shopping cart management
class shoppingcart():
    def details(self,customername,productname,price,quantity):
        self.customername=customername
        self.productname=productname
        self.price=price
        self.quantity=quantity
    def calculate_total(self):
        self.total=self.price*self.quantity
        def apply_discount(self):
            if self.total>5000:
                self.discount=self.total*0.10
            else:
                self.discount=0
                def display_bill(self):
                    final_bill=self.total=self-apply_discount
                    print("customer name:",self.customername)
                    print("productname:",self.productname)
                    print("price:",self.price)
                    print("quantity:",self.quantity)
s1=shoppingcart()
s1.details("gayatri", "mobile",20000, 1)
s1.display()      

#Libray book management
class libraybook():
    def details(self,bookname, author name,price,is available):
        self.bookname=bookname
        self.author=