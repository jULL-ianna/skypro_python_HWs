class Smartphone:

    def __init__(self, brand, model, number):
        self.p_brand = brand
        self.p_model = model
        self.subscriber_number = number

    def phone(self):
        print (self.p_brand, self.p_model, self.subscriber_number)

    def addPhone(self, catalog):
        self.ncatalog = catalog

    def getPhone(self):
        return self.phone()
    
    