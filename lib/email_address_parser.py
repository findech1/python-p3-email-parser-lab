# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Use regex to find email addresses
        email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.addresses)
        
        # Remove duplicates and sort the list alphabetically
        unique_emails = sorted(set(email_list))
        return unique_emails

# Example usage:
email_string = "john@example.com, jane@example.com bob@example.com sarah@example.com, alex@example.com, john@example.com"
parser = EmailAddressParser(email_string)
parsed_emails = parser.parse()
print(parsed_emails)  # Output: ['alex@example.com', 'bob@example.com', 'jane@example.com', 'john@example.com', 'sarah@example.com']
