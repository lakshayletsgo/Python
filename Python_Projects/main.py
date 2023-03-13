import phonenumbers
number = "+15197814276"
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number)
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number)
print(carrier.name_for_number(service_number, "en"))

from phonenumbers import timezone
state_timezone = phonenumbers.parse(number)
print(timezone.time_zones_for_number(state_timezone))

validity = phonenumbers.parse(number)
print("Valid Mobile Number:" , phonenumbers.is_valid_number(validity))

