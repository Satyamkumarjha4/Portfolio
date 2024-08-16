import streamlit as st
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database setup
def init_db():
    with sqlite3.connect('feedback.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()

def submit_feedback(name, email, message):
    with sqlite3.connect('feedback.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO feedback (name, email, message)
            VALUES (?, ?, ?)
        ''', (name, email, message))
        conn.commit()

def send_email(name, email, message):
    sender_email = "your-email@example.com"  # Replace with your email
    sender_password = "your-email-password"  # Replace with your email password
    receiver_email = "satyamjha4@gmail.com"  # Replace with the recipient's email

    subject = "New Feedback Received"
    body = f"""
    Name: {name}
    Email: {email}
    Message: {message}
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server details
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print('Email sent successfully.')
    except Exception as e:
        print(f'Error: {e}')

# Streamlit app
def main():
    st.set_page_config(page_title="Satyam's Portfolio", page_icon=":guardsman:", layout="wide")

    # HTML content
    html_code = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: Arial, sans-serif; font-size: 16px; line-height: 1.5; color: #333; background-color: #f9f9f9; }
        h1, h2, h3, h4, h5, h6 { font-weight: bold; color: #333; }
        a { text-decoration: none; color: #337ab7; }
        a:hover { color: #23527c; }
        p { color: #000; } /* Change text color to black */
        ul {color: #000; } /* Change text color to black */
        header { background-color: #337ab7; padding: 20px; text-align: center; }
        header nav ul { list-style: none; margin: 0; padding: 0; display: flex; justify-content: space-between; }
        header nav ul li { margin-right: 20px; }
        header nav a { color: #fff; transition: color 0.2s ease; }
        header nav a:hover { color: #ccc; }
        section { padding: 40px; margin-bottom: 20px; background-color: #fff; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }
        section h2 { margin-top: 0; }
        button { background-color: #337ab7; color: #fff; border: none; padding: 10px 20px; font-size: 16px; cursor: pointer; transition: background-color 0.2s ease; }
        button:hover { background-color: #23527c; }
        button:active { background-color: #337ab7; transform: translateY(2px); }
        .feedback-form { padding: 20px; background-color: #fff; border: 1px solid #ddd; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }
        .feedback-form label { display: block; margin-bottom: 10px; }
        .feedback-form input, .feedback-form textarea { width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; }
        .feedback-form input[type="submit"] { background-color: #337ab7; color: #fff; padding: 10px 20px; border: none; cursor: pointer; transition: background-color 0.2s ease; }
        .feedback-form input[type="submit"]:hover { background-color: #23527c; }
        @media (max-width: 768px) { header nav ul { flex-direction: column; } header nav ul li { margin-right: 0; } section { padding: 20px; } }
        @media (max-width: 480px) { header nav ul { flex-direction: column; } header nav ul li { margin-right: 0; } section { padding: 10px; } }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About Me</a></li>
                    <li><a href="#skills">Skills</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#experience">Experience</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <section id="home">
                <h1>Welcome to my portfolio!</h1>
                <p>I'm Satyam, a passionate programmer and developer with a strong foundation in programming languages, frameworks, and technologies. I'm excited to showcase my skills and projects in this portfolio.</p>
            </section>
            <section id="about">
                <h2>About Me</h2>
                <p>I'm Satyam, a [Your Age]-year-old programmer and developer with a strong passion for building innovative solutions. I'm proficient in a range of programming languages, including Python, C++, and Java, and have experience with various frameworks and technologies. I'm always looking to learn and improve my skills, and I'm excited to share my projects and experiences with you.</p>
            </section>
            <section id="skills">
                <h2>Skills</h2>
                <h3>Programming Languages</h3>
                <ul>
                    <li>Python: Proficient in Python programming, with experience in developing various projects, including a Comprehensive Book Management System, Password Generator, Calculator, Rock-Paper-Scissors game, and To-Do List using GUI. Strong understanding of Python's syntax, libraries, and object-oriented principles.</li>
                    <li>C++: Experience in writing, debugging, and running C++ code using Visual Studio Code and the terminal. Familiar with basic to intermediate concepts in C++ programming.</li>
                    <li>Java: Capable of developing Java programs, particularly in creating pattern-based programs like right-angle triangles with incrementing numbers. Good grasp of Java's syntax and object-oriented concepts.</li>
                    <li>SQL: Proficient in writing SQL queries and managing databases, particularly using SQLite. Experience in creating and manipulating database tables for various projects, such as the Comprehensive Book Management System.</li>
                </ul>
                <h3>Frameworks & Libraries</h3>
                <ul>
                    <li>PyQt5: Skilled in using PyQt5 for developing graphical user interfaces (GUIs) in Python. Applied PyQt5 in creating the Contact Manager application, leveraging features like PyQt Designer for efficient UI development.</li>
                    <li>Streamlit: Experience in using Streamlit for deploying Python applications with a modern web-based interface. Utilized Streamlit in the deployment of your Contact Manager application and updating the frontend of your Comprehensive Book Management System.</li>
                    <li>SQLite: Adept at using SQLite for database management in Python projects. Experience in designing and implementing databases, performing CRUD operations, and integrating SQLite with Python applications.</li>
                </ul>
                <h3>Tools & Technologies</h3>
                <ul>
                    <li>Visual Studio Code: Comfortable using Visual Studio Code as the primary integrated development environment (IDE) for coding in Python, C++, and other languages. Skilled in using extensions and terminal features for an efficient development workflow.</li>
                    <li>GitHub: Proficient in using GitHub for version control, code collaboration, and project management. Experience in pushing projects to GitHub repositories and managing project versions throughout the development lifecycle.</li>
                    <li>PyQt Designer: Familiar with PyQt Designer for designing and customizing graphical user interfaces in PyQt5. Used PyQt Designer to create intuitive and user-friendly interfaces for applications.</li>
                    <li>HTML/CSS: Basic understanding of HTML and CSS for creating and styling web pages. Experience in integrating HTML content with Python applications and streamlining the user interface design process.</li>
                </ul>
            </section>
            <section id="projects">
                <h2>Projects</h2>
                <h3>Comprehensive Book Management System</h3>
                <p>Developed a comprehensive book management system using Python, PyQt5, and SQLite. Integrated Streamlit to update the frontend, allowing for enhanced user interaction and functionality.</p>
                <h3>Password Generator</h3>
                <p>Created a password generator tool using Python to generate secure passwords with various complexity requirements. The project involved implementing algorithms for password generation and user input validation.</p>
                <h3>Calculator</h3>
                <p>Developed a simple calculator application using Python, capable of performing basic arithmetic operations. The project focused on implementing core mathematical functions and creating a user-friendly interface.</p>
                <h3>Rock-Paper-Scissors Game</h3>
                <p>Built a Rock-Paper-Scissors game using Python with a graphical user interface. The project demonstrated the ability to create interactive applications and handle user input for game logic.</p>
                <h3>To-Do List</h3>
                <p>Designed and implemented a To-Do List application with a graphical user interface using Python. The project aimed to provide a simple and effective task management solution for users.</p>
            </section>
            <section id="experience">
                <h2>Experience</h2>
                <h3>Internship at CodSoft</h3>
                <p>Completed a 4-week internship at CodSoft as a Python Programmer. Worked on various projects, including a Password Generator, Calculator, Rock-Paper-Scissors game, To-Do List, and Contact Manager application. Gained experience in using PyQt5, SQLite, and Streamlit, and improved coding proficiency through hands-on tasks.</p>
            </section>
        </main>
    </body>
    </html>
    '''

    st.markdown(html_code, unsafe_allow_html=True)

    st.subheader("Feedback Form")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Submit"):
        if name and email and message:
            submit_feedback(name, email, message)
            send_email(name, email, message)
            st.success("Feedback submitted successfully!")
        else:
            st.error("Please fill out all fields.")

    if st.button("Clear"):
        st.text_input("Name", value="", key="clear_name")
        st.text_input("Email", value="", key="clear_email")
        st.text_area("Message", value="", key="clear_message")

if __name__ == "__main__":
    init_db()
    main()
