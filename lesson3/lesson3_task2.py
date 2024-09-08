from smartphone import Smartphone

catalog = []
p1 = Smartphone("Samsung", "A215G", "+79112345678")
p2 = Smartphone("Nokia", "2210", "+79223456789")
p3 = Smartphone("GU", '1120', "+79334567890")
p4 = Smartphone("Moto", "A55", "+79445678901")
p5 = Smartphone('Eric', 'wm', '+79556789012')

catalog.append(p1)
catalog.append(p2)
catalog.append(p3)
catalog.append(p4)
catalog.append(p5)

for ph in catalog:
    print(f"{ph.p_brand} - {ph.p_model}. {ph.subscriber_number}")

