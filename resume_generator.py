import argparse
from fpdf import FPDF

def add_section_header(pdf, title, x, y, w, h, background_color):
    pdf.set_fill_color(*background_color)
    header_background_color = (230, 230, 230)  # Fixed color for section headers
    pdf.set_fill_color(*header_background_color)
    pdf.rect(x, y, w, h, style='F')
    pdf.set_font('DejaVu', 'B', 10)
    pdf.set_xy(x + 5, y)
    pdf.cell(w, 10, title, align='L')

def add_bullet_list(pdf, items, font, size):
    bullet = u'\u2022'
    pdf.set_font(font, '', size)
    for item in items:
        pdf.cell(10, 10, f'{bullet} {item}', ln=1)

def add_education_section(pdf, font_size, font_color, background_color):
    add_section_header(pdf, 'EDUCATION', 10, 40, 190, 8, background_color)
    pdf.set_y(47)
    pdf.set_font("DejaVu", 'B', 10)
    pdf.set_text_color(font_color[0], font_color[1], font_color[2])
    pdf.cell(20, 8, "Bachelor of Technology in Computer Science Engineering            August 2023 - Present     CPI:9.09")
    pdf.set_y(52)
    pdf.set_font("DejaVu", '', 10)
    pdf.cell(20, 8, "Indian Institute of Technology Gandhinagar")
    pdf.set_y(57)
    pdf.set_font("DejaVu", 'B', 10)
    pdf.set_text_color(font_color[0], font_color[1], font_color[2])
    pdf.cell(20, 8, "Central Board of Secondary Education                                              2021 - 2023              Percent%:96")
    pdf.set_y(62)
    pdf.set_font("DejaVu", '', 10)
    pdf.cell(20, 8, "SR Prime School")
    pdf.set_y(67)
    pdf.set_font("DejaVu", 'B', 10)
    pdf.set_text_color(font_color[0], font_color[1], font_color[2])
    pdf.cell(20, 8, "State Board of Secondary Education                                               2021                        Percent%:100")
    pdf.set_y(72)
    pdf.set_font("DejaVu", '', 10)
    pdf.cell(20, 8, "National High School")

def add_skills_section(pdf, font_size, font_color, background_color):
    add_section_header(pdf, 'SKILLS', 10, 85, 190, 8, background_color)
    pdf.set_y(92)
    pdf.set_font("DejaVu", 'B', font_size)
    pdf.cell(20, 8, "Programming Languages")
    pdf.set_y(99)
    pdf.set_font('DejaVu', '', 10)
    pdf.set_text_color(font_color[0], font_color[1], font_color[2])
    bullet = u'\u2022'
    pdf.cell(10, 10, f'{bullet} Python, C, C++', ln=1)
    pdf.set_y(106)
    pdf.set_font("DejaVu", 'B', font_size)
    pdf.cell(20, 8, "Tools")
    pdf.set_y(113)
    pdf.set_font('DejaVu', '', 10)
    pdf.cell(10, 10, f'{bullet} MySQL, Flask, CSV', ln=1)
    pdf.set_y(120)
    pdf.set_font("DejaVu", 'B', font_size)
    pdf.cell(20, 8, "Libraries")
    pdf.set_y(127)
    pdf.set_font('DejaVu', '', 10)
    pdf.cell(10, 10, f'{bullet} Numpy, Pandas, Scikit-learn, Pytorch, OpenCV, Tensorflow, Matplotlib', ln=1)

def add_experience_section(pdf, font_size, font_color, background_color):
    add_section_header(pdf, 'EXPERIENCE', 10, 140, 190, 8, background_color)
    pdf.set_y(147)
    pdf.set_font("DejaVu", 'B', font_size)
    pdf.cell(20, 8, "Coursework on Machine Learning")
    pdf.set_y(154)
    pdf.set_font('DejaVu', '', 10)
    pdf.set_text_color(font_color[0], font_color[1], font_color[2])
    bullet = u'\u2022'
    pdf.cell(10, 5, f'{bullet} Successfully completed a comprehensive course on Machine Learning', ln=1)
    pdf.cell(10, 10, f'{bullet} Worked on four mini-projects as part of the coursework, demonstrating practical application of concepts', ln=1)

def add_projects_section(pdf, font_size, font_color, background_color):
    projects = [
        {
            "title": "Activity Recognition Using Machine Learning",
            "description": "Collected real-time accelerometer data to develop a model that detects activity like sitting ,walking etc.",
            "techniques": "Techniques Used: Data preprocessing, feature engineering, and supervised learning algorithms.",
            "tools": "Tools: Python, Scikit-learn, Matplotlib."
        },
        {
            "title": "Text Generation Using MLP",
            "description": "Implemented a next-word prediction model using a Multilayer Perceptron on the Shakespeare dataset.",
            "techniques": "Developed a Streamlit app for user interaction and visualized embeddings using t-SNE.",
            "tools": "Tools: Python, Streamlit, t-SNE, Matplotlib."
        },
        {
            "title": "Classification of Dolphins and Snakes",
            "description": "Designed and compared performance of various VGG models for binary image classification.",
            "techniques": "Explored transfer learning approaches with VGG16 and VGG19 to improve accuracy.",
            "tools": "Tools: Python, TensorFlow/Keras, OpenCV."
        }
    ]
    pdf.set_y(165)
    pdf.set_font("DejaVu", 'B', 11)
    pdf.cell(20, 8, "Key Projects")
    pdf.ln(8)
    bullet = u'\u2022'
    for project in projects:
        pdf.set_font('DejaVu', 'B', font_size)
        pdf.cell(0, 10, project["title"], ln=True)
        pdf.set_font('DejaVu', '', 10)
        pdf.set_text_color(font_color[0], font_color[1], font_color[2])
        pdf.cell(10)
        pdf.cell(0, 8, f"{bullet} {project['description']}", ln=True)
        pdf.cell(10)
        pdf.cell(0, 8, f"{bullet} {project['techniques']}", ln=True)
        pdf.cell(10)
        pdf.cell(0, 8, f"{bullet} {project['tools']}", ln=True)
        pdf.ln(2)

def generate_resume(font_size, font_color, background_color):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(10, 10, 15)
    pdf.add_page()

    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)

    pdf.set_fill_color(*background_color)
    pdf.rect(0, 0, 210, 297, 'F')  
    
    pdf.set_font("DejaVu", 'B', 25)
    pdf.set_y(5)
    pdf.cell(10, 5, "", border=0, ln=1, align="C")
    pdf.set_y(10)
    pdf.set_font("DejaVu", 'B', 22)
    pdf.cell(60, 16, "BURRA SAHARSH")
    pdf.set_y(20)
    pdf.set_font("DejaVu", 'B', 15)
    pdf.cell(20, 8, "Sophomore at IITGN")
    pdf.set_text_color(font_color[0], font_color[1], font_color[2])
    pdf.set_y(25)
    pdf.set_font("DejaVu", '', 10)
    pdf.cell(100, 10, "Hiqom, IITGN, Palaj, Gujarat     |      +91 7093080074 | ", ln=0)
    pdf.set_text_color(0, 100, 255)
    pdf.set_font("DejaVu", 'U', 10)
    pdf.cell(0, 10, "saharshburra@gmail.com", ln=0, link="mailto:saharshburra@gmail.com")
    pdf.set_font("DejaVu", 'B', 25)
    pdf.set_text_color(0,0,0)

    add_education_section(pdf, font_size, font_color, background_color)
    add_skills_section(pdf, font_size, font_color, background_color)
    add_experience_section(pdf, font_size, font_color, background_color)
    add_projects_section(pdf, font_size, font_color, background_color)

    pdf.output("Resume_customized.pdf")

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a resume PDF.')
    parser.add_argument('--font-size', type=int, default=12, help='Adjust font size.')
    parser.add_argument('--font-color', type=str, default="#000000", help='Adjust font color (e.g., hex code or color name).')
    parser.add_argument('--background-color', type=str, default="#FFFFFF", help='Adjust background color (e.g., hex code or color name).')

    args = parser.parse_args()

    font_size = args.font_size
    font_color_rgb = hex_to_rgb(args.font_color)
    background_color_rgb = hex_to_rgb(args.background_color)

    generate_resume(font_size, font_color_rgb, background_color_rgb)