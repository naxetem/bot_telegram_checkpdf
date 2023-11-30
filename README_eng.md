# PDF Download and Telegram Send Automation

## Description
This project consists of a Python script that automatically performs the following tasks:
1. Reads URLs and folder names from a text file.
2. For each URL, downloads all the PDF files found on the page.
3. Saves each PDF in a specific folder on the server/local machine.
4. Sends the downloaded PDFs to a specific Telegram chat using a bot.

## How It Works
- **Data Loading**: The script reads a `webs.txt` file containing pairs of folder names and URLs, separated by commas.
- **PDF Download**: For each URL, the script searches for links to PDF files and downloads them to the corresponding folder.
- **Telegram Sending**: Each downloaded PDF file is automatically sent to a specific Telegram chat through a bot.

## Requirements
To run this script, you will need:
- Python 3.x
- Python Libraries: `requests`, `bs4` (BeautifulSoup), `os`, `urllib`, `telebot`, `dotenv`.
- A `.env` file with `TELEBOT_TOKEN` and `CHAT_ID` set for the Telegram bot.
- A `webs.txt` file with the folder names and URLs.

## Installation and Execution
1. **Dependency Installation**: Ensure you have all the necessary libraries installed.
2. **`.env` File Setup**: Create a `.env` file in the same directory as the script with the required variables.
3. **Preparing `webs.txt`**: Create and fill the `webs.txt` file with folder names and URLs.
4. **Script Execution**: Run the script in your Python environment.

## Additional Notes
- The script does not verify SSL certificates (`verify=False` in HTTP requests), which can be risky for non-secure URLs.
- Ensure you have the appropriate permissions to download and send the PDF files.
- The Telegram bot must be properly set up and have permission to send messages to the specified `CHAT_ID`.
