# URLHunter

URLHunter is a fast and efficient web directory brute-forcer/scanner. It is designed to uncover hidden directories and files on web servers by using a wordlist to generate requests to specified URLs.

## Features

- Multi-threaded for faster scanning
- Supports HTTP and HTTPS
- Easy-to-use command-line interface
- Customizable wordlists

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/cwsecur1ty/URLHunter.git
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
```
## Example
```bash
python urlhunter.py -u https://example.com -w wordlists/common.txt
```
This will scan https://example.com using the wordlist common.txt.

## Options
- -u, --url: Base URL to scan (required)
- -w, --wordlist: Path to the wordlist file (required)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational purposes and ethical security testing only. It should only be used on websites you own or have explicit permission to test. Unauthorized use of this tool on websites without permission is illegal and unethical.

The authors and contributors of DirBuster are not responsible for any misuse or damage caused by this tool. Always obtain proper authorization before performing any security testing.

Using this tool, you agree to comply with all applicable laws and regulations and take full responsibility for your actions.

