# URLHunter

URLHunter is a fast and efficient web directory brute forcer/scanner. It is designed to uncover hidden directories and files on web servers by using a wordlist to generate requests to specified URLs.

## Features

- Multi-threaded for faster scanning
- Supports HTTP and HTTPS
- Easy-to-use command-line interface
- Customizable wordlists

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/URLHunter-Web-Directory-Scanner.git
    cd URLHunter-Web-Directory-Scanner
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use URLHunter, run the script with the following command:

```bash
python URLHunter.py -u URL -w WORDLIST
