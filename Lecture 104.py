class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to", self.name, self.lastName, "'s Cart")


custmer1 = Customer()
custmer1.name = "Oliver"
custmer1.lastName = "Davies"
custmer1.addCart()

custmer2 = Customer()
custmer2.name = "Joshua"
custmer2.lastName = "Burgess"
custmer2.addCart()

custmer3 = Customer()
custmer3.name = "Austin"
custmer3.lastName = "Coleman"
custmer3.addCart()
