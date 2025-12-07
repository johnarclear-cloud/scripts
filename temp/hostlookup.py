import socket
import sys

def perform_host_lookup(filename):
    """
    Reads a list of websites from a file and performs a host lookup (DNS lookup)
    for each domain to find its IP address.

    Args:
        filename (str): The path to the file containing the list of websites,
                        with one domain per line.
    """
    print(f"[*] Reading websites from '{filename}'...\n")
    
    try:
        with open(filename, 'r') as file:
            # Read each line, strip whitespace, and filter out empty lines
            websites = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: The file '{filename}' was not found. Please create it.")
        return
    except Exception as e:
        print(f"[!] An unexpected error occurred while reading the file: {e}")
        return

    if not websites:
        print("[!] The website list is empty. Please add some domains to the file.")
        return

    # Print a formatted header for the output
    print(f"{'Website':<35} | {'IP Address'}")
    print(f"{'-'*35} | {'-'*15}")

    # Loop through each website in the list
    for website in websites:
        try:
            # socket.gethostbyname() translates a host name to IPv4 address format
            ip_address = socket.gethostbyname(website)
            print(f"{website:<35} | {ip_address}")
        except socket.gaierror:
            # This error occurs if the DNS lookup fails
            print(f"{website:<35} | {'Host could not be resolved'}")
        except Exception as e:
            # Catch any other potential errors during the lookup
            print(f"{website:<35} | An error occurred: {e}")

if __name__ == "__main__":
    # The script uses 'websites.txt' as the default file name.
    # You can also provide a different filename as a command-line argument.
    # Example: python host_lookup.py my_list_of_sites.txt
    if len(sys.argv) > 1:
        file_to_process = sys.argv[1]
    else:
        file_to_process = 'websites.txt'
    
    perform_host_lookup(file_to_process)