# Pager Tools

Pager Tools is a multi-tool web application built using Flask and Python. It provides a collection of useful tools, including Text to Speech, QR Code Generator, Password Generator, Unit Converter, Image Compressor, and PDF to Text extraction. The application is designed to be simple, modular, and easy to use.

## Features

1.Text to Speech: Convert text into speech using Google's Text-to-Speech API.

2.QR Code Generator: Generate QR codes from text or URLs.

3.Password Generator: Create strong, random passwords of customizable length.

4.Unit Converter: Convert units of length (e.g., meters to feet).

5.Image Compressor: Compress images while maintaining quality.

6.PDF to Text: Extract text from PDF files.

## Technologies Used

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Libraries:

    gTTS for Text to Speech

    qrcode for QR Code Generation

    pdfplumber for PDF to Text Extraction

    Pillow for Image Compression

Styling: Google Fonts (Roboto)

## Setup Instructions
### Prerequisites
 Python 3.11

pip (Python package manager)

Step 1: Clone the Repository

git clone https://github.com/kamleshjha/PagerTools.git

cd PagerTools

Step 2: Install Dependencies

Install the required Python libraries using pip:

pip install -r requirements.txt

Step 3: Run the Application

Start the Flask development server:

python app.py

Step 4: Access the Application

Open your browser and navigate to:

http://127.0.0.1:5000/

## Project Structure
pager-tools/
│
├── app.py                  # Main Flask application
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
├── templates/
│   └── index.html          # Frontend HTML file
└── tools/                  # Modularized tools
    ├── text_to_speech.py   # Text to Speech tool
    ├── qr_code.py          # QR Code Generator tool
    ├── password_generator.py # Password Generator tool
    ├── unit_converter.py   # Unit Converter tool
    ├── image_compressor.py # Image Compressor tool
    └── pdf_to_text.py      # PDF to Text tool

## Usage
1. Text to Speech
Enter text in the text area.

Click Convert to Speech to generate and download an audio file.

2. QR Code Generator
Enter text or a URL in the input field.

Click Generate QR Code to create and display a QR code.

3. Password Generator
Enter the desired password length (between 8 and 32).

Click Generate Password to create a random password.

4. Unit Converter
Enter the value to convert.

Select the source and target units.

Click Convert to see the result.

5. Image Compressor
Upload an image file.

Click Compress Image to download the compressed image.

6. PDF to Text
Upload a PDF file.

Click Extract Text to extract and display the text content.

Contributing
Contributions are welcome! If you'd like to contribute to Pager Tools, follow these steps:

## Fork the repository.

Create a new branch for your feature or bugfix:
git checkout -b feature-name
Commit your changes:
git commit -m "Add your message here"
Push to the branch:
git push origin feature-name
Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Flask: For providing a lightweight and flexible web framework.

Hugging Face Transformers: For inspiration on modular tool design.

Google Fonts: For the Roboto font used in the UI.

Contact
For questions or feedback, feel free to reach out:

Email: kjha8713@gmail.com

GitHub: kamleshjha

Recording of Working Application

[![Watch the video](https://img.youtube.com/vi/o3RwGcvxI/maxresdefault.jpg)](https://www.youtube.com/watch?v=o3RwGcvxI)


Enjoy using Pager Tools! 🚀
