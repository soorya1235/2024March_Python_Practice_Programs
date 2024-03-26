import re


def find_email_addresses(text):
    """
    Finds and returns all email addresses in the given text using regular expressions.

    Args:
        text (str): The text in which to search for email addresses.

    Returns:
        list: A list of email addresses found in the text.
    """
    # Regular expression pattern to match email addresses
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Find all email addresses in the text
    email_addresses = pattern.findall(text)

    return email_addresses


# Example usage
text = "Contact us at email@example.com or support@example.org for assistance."
found_emails = find_email_addresses(text)
print("Found email addresses:", found_emails)
