# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        addresses = re.split(r'\s|,', self.email_addresses)  # Split on spaces or commas
        addresses = [address.strip() for address in addresses if address.strip()]  # Remove empty strings
        addresses = list(set(addresses))  # Remove duplicates
        addresses.sort()  # Sort alphabetically
        return addresses
