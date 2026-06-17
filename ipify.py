import requests

IPIFY_IPv4_URL = "https://api.ipify.org"
IPIFY_IPv6_URL = "https://api6.ipify.org"

def get_public_ip_addresses():
    """
    Fetches both public IPv4 and IPv6 addresses using the ipify API.
    Returns:
        dict: A dictionary containing both IPv4 and IPv6 keys.
    """
    ip_addresses = {"ipv4": "Not Available", "ipv6": "Not Available"}

    # Fetch IPv4:
    try:
        response = requests.get(IPIFY_IPv4_URL, timeout=5)

        if response.status_code == 200:
            ip_addresses["ipv4"] = response.text.strip()
    except requests.RequestException:
        pass

    # Fetch IPv6:
    try:
        response = requests.get(IPIFY_IPv6_URL, timeout=5)

        if response.status_code == 200:
            ip_addresses["ipv6"] = response.text.strip()
    except requests.RequestException:
        pass

    return ip_addresses

if __name__ == "__main__":
    my_ip_addresses = get_public_ip_addresses()

    print(f"IPv4: {my_ip_addresses['ipv4']}")
    print(f"IPv6: {my_ip_addresses['ipv6']}")
