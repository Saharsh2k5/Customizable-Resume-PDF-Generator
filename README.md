# Customizable-Resume-PDF-Generator

This Python script allows us to generate a customized resume in PDF format with options to adjust font size, font color, and background color

## Features
1. **Pre-generated Resume**: 
   - Contains sections like Name, Contact Information, Skills, Education, and Experience.
   - Designed with a modern and professional layout.
   
2. **Customization Options**: 
   - **Font Size**: Specify the font size for the resume text.
   - **Font Color**: Choose a font color using a hex code or color name.
   - **Background Color**: Set the background color using a hex code or color name.
   
3. **PDF Regeneration**:
   - Generate a new PDF based on your customization preferences.

## Tools and Frameworks
- `argparse`: For parsing command-line arguments.
- `FPDF`: For generating PDF files.

## Requirements
- Python 3.x
- FPDF library (`pip install fpdf`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/resume-generator.git
   cd resume-generator

## Install the dependencies
    
    pip install fpdf
## Usage
Run the script with the desired arguments:

    python resume_generator.py --font-size <size> --font-color <color> --background-color <color>
## Output
The script generates a PDF file with the customized options and saves it in the project directory.

## Sample Resume
A sample resume generated by the script is included in the repository as Resume_customized.pdf



  
