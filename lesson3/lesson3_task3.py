from Address import Address
from Mailing import Mailing

to_address = Address('1231214', "СПб", "Речная улица", "10", "7" )
from_address = Address ('321654', "МСК", "Вечнозеленый бульвар", "7", "10")
Mailing = Mailing(to_address, from_address, 2000, 'trcnum1213141516171819')
print(f"Отправление {Mailing.track} из {Mailing.from_address.index}, {Mailing.from_address.city}",
      f"{Mailing.from_address.street}, {Mailing.from_address.house} - {Mailing.from_address.appart}"
      f" в {Mailing.to_address.index}, {Mailing.to_address.city}, {Mailing.to_address.street},"
      f"{Mailing.to_address.house} - {Mailing.to_address.appart}. Стоимость {Mailing.cost} рублей.")