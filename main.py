import phonenumbers
import pyfiglet
from colorama import Fore
from phonenumbers import carrier , timezone , geocoder

ascii_banner = pyfiglet.figlet_format("PhoneDetailer")
print(f"{ascii_banner} \n")

value= input(Fore.GREEN + "[+] Enter the Target Number(Includes CountryCode): ")

#Getting the contry code ==============
pepnumber = phonenumbers.parse(value)
location = geocoder.description_for_number(pepnumber , "en")

#Getting the Service Provider ===========
service_pro = carrier.name_for_number(pepnumber , "en")
is_valid = phonenumbers.is_valid_number(pepnumber)
name_user = carrier.safe_display_name(pepnumber , "en")
timeZone = timezone.time_zones_for_number(pepnumber)
code = phonenumbers.can_be_internationally_dialled(pepnumber)

token = phonenumbers.country_mobile_token(location)

print(Fore.RED + f"[-] Location : {location}")
print(Fore.RED + f"[-] Service Pprovider : {service_pro}")
print(Fore.RED + f"[-] Valid : {is_valid}")
print(Fore.RED + f"[-] User Name : {name_user}")
print(Fore.RED + f"[-] TimeZone : {timeZone}")
print(Fore.RED + f"[-] Dialled Internationally : {code}")


