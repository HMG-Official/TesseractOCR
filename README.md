README: Tesseract OCR Image to Text GUI

This project is a simple Python Tkinter-based Graphical User Interface (GUI) application that allows you to select an image file and then uses Tesseract OCR to extract text from that image, displaying the results in a text box.
Features

    Image Browse: Easily select image files (PNG, JPG, JPEG, GIF, BMP, TIFF) from your system.
    Image Display: The chosen image is displayed within the application window.
    Text Extraction: Utilizes Tesseract OCR to convert the image content into editable text.
    Scrollable Output: Displays extracted text in a scrollable text area for easy viewing.
    Error Handling: Provides user-friendly messages for missing Tesseract installation or other OCR-related issues.

Prerequisites

Before running this application, you need to have the following installed:

    Python 3.x:
    If you don't have Python installed, download it from python.org.

    Tesseract OCR Engine:
    This is the core OCR engine. You must install it separately and ensure its executable is accessible.
        Windows: Download the installer from the Tesseract-OCR GitHub Wiki. During installation, note the installation path (e.g., C:\Program Files\Tesseract-OCR) as you might need to set it in the Python script. It's recommended to add Tesseract to your system's PATH environment variable.
        macOS: Open your terminal and run:
        Bash

brew install tesseract

Linux (Debian/Ubuntu): Open your terminal and run:
Bash

        sudo apt-get install tesseract-ocr

Installation

    Clone or Download the Repository:
    (If this were in a Git repository, you'd clone it here.)
    Otherwise, simply save the provided Python code into a file named ocr_app.py (or any name you prefer).

    Install Python Libraries:
    Open your terminal or command prompt and run the following command:
    Bash

    pip install pytesseract Pillow

        pytesseract: A Python wrapper for Tesseract-OCR.
        Pillow: The Python Imaging Library fork, required for image handling.

Configuration (Important for Windows Users)

If you are on Windows and Tesseract is not found automatically, you might need to specify the full path to the tesseract.exe executable in the Python script.

Open ocr_app.py and locate this line:
Python

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Change the path (e.g., 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe') to match the actual installation path of tesseract.exe on your system. If Tesseract is correctly added to your system's PATH, you might not need to explicitly set this.
How to Run

    Open your terminal or command prompt.
    Navigate to the directory where you saved ocr_app.py.
    Run the script using Python:
    Bash

    python ocr_app.py

Usage

    The GUI window will appear.
    Click the "Browse Image" button.
    Select an image file from your computer.
    The selected image will be displayed, and the extracted text will automatically appear in the "Extracted Text" box below.

Known Issues / Troubleshooting

    TesseractNotFoundError: This error means pytesseract cannot find the Tesseract executable.
        Ensure Tesseract OCR is installed on your system.
        Verify that the tesseract.exe path in the Python script (as described in the "Configuration" section) is correct, or that Tesseract is added to your system's PATH.
    Image Loading Errors: Ensure your image file is not corrupted and is in a supported format.

