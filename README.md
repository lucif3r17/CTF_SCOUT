# Chall_Scraper

Chall_Scraper is a Python tool designed to scrape challenges from the picoCTF platform. It automates the process of logging in, navigating through categories, and scraping challenge names. 

## Requirements

- Python 3.x
- Selenium
- Mozilla Firefox browser
- geckodriver

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Chall_Scraper.git
    ```

2. Install the required Python packages:

    ```bash
    pip install selenium
    ```

3. Download the geckodriver for your system from [here](https://github.com/mozilla/geckodriver/releases) and place it in your PATH or in the same directory as the script.

## Usage

1. Run the script:

    ```bash
    python chall_scraper.py
    ```

2. Enter your picoCTF username and password when prompted.

3. The script will then scrape the challenges from each category and create a directory structure to store them.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and do not violate the terms of service of the picoCTF platform.
