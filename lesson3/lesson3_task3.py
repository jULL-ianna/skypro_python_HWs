from Address import Address
from Mailing import Mailing

to_address = Address('1231214', "СПб", "Речная улица", "10", "7" )
from_address = Address ('321654', "МСК", "Вечнозеленый бульвар", "7", "10")
Mailing = Mailing(to_address, from_address, 2000, 'trcnum1213141516171819')
print(Mailing)