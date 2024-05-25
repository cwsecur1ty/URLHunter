import argparse
import os
import requests
import threading
from queue import Queue

# Number of threads to use
NUM_THREADS = 10

# Queue to hold the directories to be scanned
queue = Queue()

# Function to read wordlist file
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

# Function to scan a single URL
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
        response = session.get(url)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
    except requests.RequestException as e:
        print(f"[-] Error: {e}")

# Worker function for threading
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

# Main function
def main():
    """
    Main function to parse arguments, read the wordlist, and start threads.
    """
    parser = argparse.ArgumentParser(description='Web Directory Brute Forcer/Scanner')
    parser.add_argument('-u', '--url', required=True, help='Base URL to scan')
    parser.add_argument('-w', '--wordlist', required=True, help='Name of the wordlist file in the wordlists directory')

    args = parser.parse_args()
    base_url = args.url
    wordlist_filename = args.wordlist
    wordlist_path = os.path.join('wordlists', wordlist_filename)

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
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=worker, args=(base_url,))
        thread.start()
        threads.append(thread)

    # Wait for all tasks in the queue to be processed
    queue.join()

    # Ensure all threads have finished
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
