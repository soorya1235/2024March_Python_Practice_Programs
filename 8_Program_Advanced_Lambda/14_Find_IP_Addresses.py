import re


def count_ip_addresses(input_string):
    """
    Count the number of IP addresses in the given input string.
    """
    # Regular expression pattern to match an IPv4 address
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    # Find all matches of IP addresses in the input string
    ip_addresses = ip_pattern.findall(input_string)

    return len(ip_addresses)


# Example usage
input_string = "This is a sample text with IP addresses 192.168.1.1 and 10.0.0.1"
num_ips = count_ip_addresses(input_string)
print("Number of IP addresses found:", num_ips)
