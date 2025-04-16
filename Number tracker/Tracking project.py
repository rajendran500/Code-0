import phonenumbers
from phonenumbers import geocoder, carrier, timezone
Input the number (with country code)
number = input("Enter mobile number with country code (e.g., +919876543210): ")

 Parse the number
parsed_number = phonenumbers.parse(number)

 Get location
location = geocoder.description_for_number(parsed_number, "en")
 Get carrier
service_provider = carrier.name_for_number(parsed_number, "en")
 Get time zone
time_zones = timezone.time_zones_for_number(parsed_number)

print("\n📍 Location:", location)
print("📞 Carrier:", service_provider)
print("⏰ Time Zone(s):", ', '.join(time_zones))
