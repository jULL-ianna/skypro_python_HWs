from smartphone import Smartphone

catalog = ['nokia', '2200', '+79334567890']
catalog2 = ['AA', '2300', '+79334568901']
catalog3 = ['BB', '25', '+79334569012']
           
phone = Smartphone(catalog, catalog2, catalog3)
phone.addPhone(phone)
phone.getPhone()

