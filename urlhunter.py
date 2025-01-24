import argparse
import os
import requests
import threading
from queue import Queue

# Number of threads to use
NUM_THREADS = 10

# Queue to hold the directories to be scanned
queue = Queue()

def ascii_header():
    """
    Prints the ASCII art header for URLHunter.
    """
    print("""
▗▖ ▗▖▗▄▄▖ ▗▖   ▗▖ ▗▖▗▖ ▗▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌  █  ▐▌   ▐▌ ▐▌
▐▌ ▐▌▐▛▀▚▖▐▌   ▐▛▀▜▌▐▌ ▐▌▐▌ ▝▜▌  █  ▐▛▀▀▘▐▛▀▚▖
▝▚▄▞▘▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌▝▚▄▞▘▐▌  ▐▌  █  ▐▙▄▄▖▐▌ ▐▌

""")
    print("URLHunter - Web Directory Scanner v1.0")
    print("======================================")

def validate_url(base_url):
    """
    Ensures the URL includes a valid scheme (http/https).
    
    Args:
        base_url (str): The base URL to validate.
    
    Returns:
        str: Properly formatted URL with scheme.
    """
    if not base_url.startswith(('http://', 'https://')):
        base_url = f"https://{base_url}"
    return base_url.rstrip('/')

def resolve_path(path):
    """
    Resolves the given path to an absolute path.
    
    Args:
        path (str): Relative or absolute path to resolve.
    
    Returns:
        str: Absolute path of the given path.
    """
    return os.path.abspath(path)

def read_wordlist(wordlist_path):
    """
    Reads a wordlist file and returns a list of directories.
    
    Args:
        wordlist_path (str): Path to the wordlist file.
    
    Returns:
        list: List of directories from the wordlist.
    """
    with open(wordlist_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def scan_directory(session, base_url, directory):
    """
    Scans a single directory by making an HTTP request to the given URL.
    
    Args:
        session (requests.Session): The session object to make requests.
        base_url (str): The base URL to scan.
        directory (str): The directory to append to the base URL.
    """
    url = f"{base_url}/{directory}"
    try:
        response = session.get(url, timeout=5)  # Timeout of 5 seconds
        if response.status_code in [200, 204, 301, 302, 307, 401]:
            print(f"[{response.status_code}] {url}")
    except requests.RequestException as e:
        print(f"[-] Error: {e}")

def worker(base_url):
    """
    Worker function to process items in the queue.
    
    Args:
        base_url (str): The base URL to scan.
    """
    with requests.Session() as session:
        while not queue.empty():
            directory = queue.get()
            scan_directory(session, base_url, directory)
            queue.task_done()

def main():
    """
    Main function to parse arguments, read the wordlist, and start threads.
    """
    ascii_header()
    
    parser = argparse.ArgumentParser(description='Web Directory Brute Forcer/Scanner')
    parser.add_argument('-u', '--url', required=True, help='Base URL to scan')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist file (absolute or relative)')

    args = parser.parse_args()
    base_url = validate_url(args.url)  # Validate and format the base URL
    wordlist_path = resolve_path(args.wordlist)  # Resolve the wordlist path to an absolute path

    if not os.path.isfile(wordlist_path):
        print(f"Wordlist file '{wordlist_path}' does not exist.")
        return

    # Read the wordlist
    wordlist = read_wordlist(wordlist_path)

    # Add directories to the queue
    for directory in wordlist:
        queue.put(directory)

    # Create and start threads
    threads = []
    try:
        for _ in range(NUM_THREADS):
            thread = threading.Thread(target=worker, args=(base_url,))
            thread.start()
            threads.append(thread)

        # Wait for all tasks in the queue to be processed
        queue.join()

        # Ensure all threads have finished
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n[!] Scanning interrupted by user. Exiting...")
        os._exit(1)

    print("\n[+] Scanning complete.")

if __name__ == "__main__":
    main()
