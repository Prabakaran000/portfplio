import streamlit as st
import base64

def main():
    st.set_page_config(page_title="Prabakaran A - Resume", layout="wide")

    with st.sidebar:
        st.image("me.jpg", caption="Prabakaran A")
        st.title("Navigation")
        sections = [
            "Profile Summary",
            "Technical Skills",
            "Professional Experience",
            "Projects",
            "Education",
            "Certifications",
            "Achievements & Awards",
            "Languages",
            "Hobbies",
            "Declaration"
        ]
        selected_section = st.radio("Go to", sections)

    st.title('Prabakaran A')
    st.markdown("""
    **Email:** prabakaranarunkumar99@gmail.com | **Phone:** 8525069184  
    **Address:** 51/1A Pilliyarpuram, SIDCO Post, Coimbatore - 641021
    """)

    if selected_section == "Profile Summary":
        st.header('Profile Summary')
        st.markdown("""
        - Proficient in full stack development using Python, Django, React.js, Next.js.
        - Experienced in API development with Python Flask RESTx.
        - Skilled in backend technologies including SQL and MongoDB.
        - Version control expertise with GitHub.
        - Familiar with task management tools like Jira and Azure DevOps.
        - Strong understanding of SDLC and agile methodologies.
        """)
    
    if selected_section == "Technical Skills":
        st.header('Technical Skills')
        st.markdown("""
        - **Languages:** Python, HTML, CSS
        - **Frameworks/Libraries:** Django, React.js, Next.js, Flask RESTx
        - **Databases:** SQL, MongoDB
        - **Tools:** GitHub, Jira, Azure DevOps
        """)

    if selected_section == "Professional Experience":
        st.header('Professional Experience')
        st.subheader('Freelance Full Stack Developer')
        st.write("""
        **MG Express** (February 2021 - February 2023)
        - Designed, developed, and maintained scalable CRM applications using the Django framework.
        - Collaborated with product managers and stakeholders to gather and translate requirements into technical specifications.
        - Implemented custom CRM features and functionalities to meet business needs.
        """)

        st.subheader('Field Engineer')
        st.write("""
        **Oasys Cybernetics Private Limited** (August 2019 - August 2020)
        - Analyzed and rectified client problems efficiently.
        """)

        st.subheader('Data Annotation Specialist')
        st.write("""
        **Apexon** (February 2021 - February 2023)
        - Annotated data accurately and efficiently to support machine learning and data science projects.
        """)

    if selected_section == "Projects":
        st.header('Projects')
        st.markdown("""
        - **Conti-ODC:** Developed a data annotation process for machine learning and data science projects. """)
        st.markdown("""- **Co-optex:** Tested billing software and provided detailed reports to developers. """)
        st.markdown("""- **MG Express Courier Billing and Administration Dashboard:** Freelance Project: MG Express Courier System
Project Title: MG Express Courier Billing and Administration Dashboard Technologies Used:
Django, MySQL Role: Full Stack Developer
Duration: Feb 2023 to Dec 2023
Responsibilities and Achievements: Developed
a comprehensive courier billing system to
streamline and automate invoice generation
and payment processing. Designed and
implemented an intuitive admin dashboard for
managing courier operations, tracking
shipments, and monitoring system
performance. Utilized Django to create a
robust backend infrastructure ensuring secure
and efficient data handling. Integrated MySQL
for reliable and scalable database
management, optimizing queries for
enhanced performance. Conducted thorough
testing and debugging to ensure the system's
reliability and accuracy. Collaborated closely
with stakeholders to gather requirements and
deliver customized solutions that met business
needs. """)
        

    if selected_section == "Education":
        st.header('Education')
        st.markdown("""
        - **BCA:** Rathinam College of Arts and Science (2016-2019)
        - **12th Grade:** Government Higher Secondary School, Othakalmandabam (2016)
        - **10th Grade:** V.S. Sengottaiah Memorial High School (2014)
        """)

    if selected_section == "Certifications":
        st.header('Certifications')
        st.write("Python Full Stack Development: Core Python, Advanced Python, Django, HTML, CSS, Bootstrap, JavaScript, Angular.js, Vue.js, React.js.")

    if selected_section == "Achievements & Awards":
        st.header('Achievements & Awards')
        st.markdown("""
        - Presented a paper on Indian IT Act 2008 at an international cyber security conference (2017).
        - Participated in a machine learning workshop conducted by Google (2018).
        - Participated in a digital marketing workshop (2017).
        """)

    if selected_section == "Languages":
        st.header('Languages')
        st.markdown("""
        - Tamil: Fluent (Read, Write, Speak)
        - English: Fluent (Read, Write, Speak)
        """)

    if selected_section == "Hobbies":
        st.header('Hobbies')
        st.markdown("""
        - Learning new programming languages
        - Reading books
        - Playing sports to enhance teamwork and communication skills
        """)

    if selected_section == "Declaration":
        st.header('Declaration')
        st.write("I hereby declare that all the details furnished above are true to the best of my knowledge and belief.")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resume - Prabakaran A</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                margin-top: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
            }}
            .text-center h1 {{
                margin-bottom: 10px;
            }}
            .section-title {{
                background-color: #007bff;
                color: #fff;
                padding: 10px;
                border-radius: 5px;
            }}
            .section-content {{
                margin-bottom: 20px;
            }}
            ul {{
                padding-left: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="text-center mb-4">
                <h1>Prabakaran A</h1>
                <p>Email: prabakaranarunkumar99@gmail.com | Phone: 8525069184</p>
                <p>Address: 51/1A Pilliyarpuram, SIDCO Post, Coimbatore - 641021</p>
            </div>
            <section class="section-content">
                <h2 class="section-title">Profile Summary</h2>
                <ul>
                    <li>Proficient in full stack development using Python, Django, React.js, Next.js.</li>
                    <li>Experienced in API development with Python Flask RESTx.</li>
                    <li>Skilled in backend technologies including SQL and MongoDB.</li>
                    <li>Version control expertise with GitHub.</li>
                    <li>Familiar with task management tools like Jira and Azure DevOps.</li>
                    <li>Strong understanding of SDLC and agile methodologies.</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Technical Skills</h2>
                <ul>
                    <li><strong>Languages:</strong> Python, HTML, CSS</li>
                    <li><strong>Frameworks/Libraries:</strong> Django, React.js, Next.js, Flask RESTx</li>
                    <li><strong>Databases:</strong> SQL, MongoDB</li>
                    <li><strong>Tools:</strong> GitHub, Jira, Azure DevOps</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Professional Experience</h2>
                <div>
                    <h3>Freelance Full Stack Developer</h3>
                    <p><em>MG Express</em> (February 2021 - February 2023)</p>
                    <ul>
                        <li>Designed, developed, and maintained scalable CRM applications using the Django framework.</li>
                        <li>Collaborated with product managers and stakeholders to gather and translate requirements into technical specifications.</li>
                        <li>Implemented custom CRM features and functionalities to meet business needs.</li>
                    </ul>
                </div>
                <div>
                    <h3>Field Engineer</h3>
                    <p><em>Oasys Cybernetics Private Limited</em> (August 2019 - August 2020)</p>
                    <ul>
                        <li>Analyzed and rectified client problems efficiently.</li>
                    </ul>
                </div>
                <div>
                    <h3>Data Annotation Specialist</h3>
                    <p><em>Apexon</em> (February 2021 - February 2023)</p>
                    <ul>
                        <li>Annotated data accurately and efficiently to support machine learning and data science projects.</li>
                    </ul>
                </div>
            </section>
            <section class="section-content">
                <h2 class="section-title">Projects</h2>
                <ul>
                    <li><strong>Conti-ODC:</strong> Developed a data annotation process for machine learning and data science projects.</li>
                    <li><strong>Co-optex:</strong> Tested billing software and provided detailed reports to developers.</li>
                    <li><strong>MG Express Courier Billing and Administration Dashboard:</strong> Developed a comprehensive courier billing system to streamline and automate invoice generation and payment processing. Designed and implemented an intuitive admin dashboard for managing courier operations, tracking shipments, and monitoring system performance. Utilized Django to create a robust backend infrastructure ensuring secure and efficient data handling. Integrated MySQL for reliable and scalable database management, optimizing queries for enhanced performance. Conducted thorough testing and debugging to ensure the system's reliability and accuracy. Collaborated closely with stakeholders to gather requirements and deliver customized solutions that met business needs.</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Education</h2>
                <ul>
                    <li><strong>BCA:</strong> Rathinam College of Arts and Science (2016-2019)</li>
                    <li><strong>12th Grade:</strong> Government Higher Secondary School, Othakalmandabam (2016)</li>
                    <li><strong>10th Grade:</strong> V.S. Sengottaiah Memorial High School (2014)</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Certifications</h2>
                <p>Python Full Stack Development: Core Python, Advanced Python, Django, HTML, CSS, Bootstrap, JavaScript, Angular.js, Vue.js, React.js.</p>
            </section>
            <section class="section-content">
                <h2 class="section-title">Achievements & Awards</h2>
                <ul>
                    <li>Presented a paper on Indian IT Act 2008 at an international cyber security conference (2017).</li>
                    <li>Participated in a machine learning workshop conducted by Google (2018).</li>
                    <li>Participated in a digital marketing workshop (2017).</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Languages</h2>
                <ul>
                    <li>Tamil: Fluent (Read, Write, Speak)</li>
                    <li>English: Fluent (Read, Write, Speak)</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Hobbies</h2>
                <ul>
                    <li>Learning new programming languages</li>
                    <li>Reading books</li>
                    <li>Playing sports to enhance teamwork and communication skills</li>
                </ul>
            </section>
            <section class="section-content">
                <h2 class="section-title">Declaration</h2>
                <p>I hereby declare that all the details furnished above are true to the best of my knowledge and belief.</p>
            </section>
        </div>
    </body>
    </html>
    """

    # Encode the HTML content to base64 correctly for download
    b64_html_content = base64.b64encode(html_content.encode()).decode('utf-8')

    # Create a download button
    st.download_button(
        label="Download Resume",
        data=html_content,
        file_name='Prabakaran_A_Resume.html',
        mime='text/html'
    )

if __name__ == "__main__":
    main()
