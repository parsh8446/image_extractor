# Webpage Image Extractor

This Streamlit application allows you to extract and download all images from a specified webpage URL. The images are saved into a folder, and the progress of the extraction is displayed using a progress bar.

## Features

- Extract images from any valid webpage URL.
- Display progress of image extraction.
- Save images into a specified folder.
- Display extracted images within the app.

## Installation

To use this application, you need to have Python installed. You can download Python from [python.org](https://www.python.org/).

1. Clone this repository or download the code files.
2. Create a virtual environment (recommended) and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

 3)  Install the required packages:
    pip install -r requirements.txt

Usage
Save the main script (image_extractor.py) in your project directory.
Run the Streamlit app: streamlit run image_extractor.py

Enter the URL of the webpage from which you want to extract images.
The app will display the progress of the extraction and show the downloaded images.
Dependencies
streamlit
requests
beautifulsoup4
You can install these dependencies using the requirements.txt file. Make sure you have the following in your requirements.txt:
txt:
streamlit
requests
beautifulsoup4

Folder Structure
image_extractor.py: The main script for the Streamlit app.
extracted_images/: Folder where the extracted images will be saved.
Troubleshooting
If you encounter any issues, ensure that:

You have a stable internet connection.
The URL you entered is valid and accessible.
All required packages are installed.
For further assistance, please open an issue in this repository.

License
This project is licensed under the MIT License.



