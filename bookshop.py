class Bookshop:
    def __int__(self, orders):
        self.orders = orders

    def method1(self):
        print("method1")
        # returns same list but the tuple w/ 2 items only
        # items r ( order num, quantity * price )
        # also price increases by 10 dollars if order is less than $100

    def method2(self):
        print("method2")
        # filter out minimum price of product, 4 tuples
        # has order num, then which order has the least amnt total
        # so get the quantity * price and return the lowest one

    def method3(self):
        print("method3")
        # filters out the maximum price ? so same thing as before
        # so order num, then order w the highest total amnt

    def method4(self):
        print("method4")
        # returns tuples w bookshop order number and then price * quantity?
        # so ( bookshop order number, total price of order )
        # so add all total amnt together and return it

    def method5(self):
        print("method5")
        # returns list w two items, book order num and total amount of product in all order
        # returns order num that has max total amount of product in all order (??)
        # returns order num, which pops up multiple times, w the most amnt and the total
        # it comes out to

    def method6(self):
        print("method6")
        # same as before but total quantity? so amount of books in order
        # so which order gets ordered the most w highest quantity added together

    def method7(self):
        print("method7")
        # returns an ordered list
        # based on bookshop order num, per maximum total quantity?
        # [(max bookshop order number, total quantity)....(min bookshop order num, total quantity)]
        # from greatest to least ig
        # so returns total amnt of quantity from high to low

    def method8(self):
        print("method8")
        # returns a total quantity of all books ordered
        # just a value no list or anything

    def method9(self):
        print("method9")
        # returns a list w two items
        # most ordered book, book order num, and the least ordered ( book order num)
        # count the occurrence of book order number in all orders

    def method10(self):
        print("method10")
        # returns a list w/ 4 items
        # each item represents length of sublist from index - to index 3
