# Wordlists for DirBuster

This directory contains wordlists used by URLHunter, a web directory brute forcer/scanner. These wordlists are used to uncover hidden directories and files on web servers by generating requests to specified URLs based on the entries in the wordlists.

## Available Wordlists

### common.txt
- **Description**: This wordlist contains a collection of common hidden directories and files frequently targeted during web security scans.
- **Usage**: Suitable for general-purpose scans to identify common administrative interfaces, backup directories, and other sensitive paths.

## How to Use

To use a wordlist with DirBuster, specify the name of the wordlist file using the `-w` or `--wordlist` option when running the script. The script will automatically look for the wordlist in this directory.
