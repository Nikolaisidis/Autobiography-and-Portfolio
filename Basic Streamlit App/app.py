import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# Set page configuration
st.set_page_config(page_title="Autobiography & Portfolio", layout="wide")

# Sidebar for additional options
st.sidebar.title("Select Visualization")
show_map = st.sidebar.checkbox("Show the map", value=True)
chart_type = st.sidebar.selectbox(
    "Choose a Chart Type", ["Line Chart", "Bar Chart"])

# Title and Introduction
st.title("Autobiography & Portfolio")
st.write("Hello! I am Alestair Cyril Coyoca, a college student pursuing a Bachelor of Science in Information Technology. Welcome to my autobiography and portfolio, where you can learn more about my journey, experiences, and work.")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Top Navigation Tabs
tabs = st.tabs(["Home", "Autobiography", "Portfolio", "Contact"])

# Home Tab
with tabs[0]:
    st.header("My Personal Space")
    st.write("""
    This application is divided into multiple sections:
    - **Autobiography:** Learn about my personal and professional journey.
    - **Portfolio:** Explore my projects, achievements, and skills.
    Use the navigation tabs above to explore.
    """)
    st.image("profile.jpg",
             caption="I don't take pictures, this was from my SHS photo", width=300)

    st.subheader("My Hobbies")
    interests = st.multiselect(
        "List of hobbies and interests:",
        ["🎶 Listening Old Songs", "🐱 Cat",
            "🎥 Watching Movies", "🎮 Playing Online Games", "🛌 Sleeping"]
    )
    st.write(f"Selected hobbies and interests: {', '.join(interests)}")

# Autobiography Tab
with tabs[1]:
    st.header("Autobiography")

    # Columns for biography details
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Early Life")
        st.write("""
        I was born and raised in Cebu City, Philippines. My childhood was filled with curiosity and a love for learning.
        I was passionate about technology and computers from a young age, which later shaped my career choice.
        """)

    with col2:
        st.subheader("Education")
        education_data = {
            'Degree': ['Elementary', 'Junior High School', 'Senior High School', 'College'],
            'School': ['Basak Community School', 'Cebu City Don Carlos A. Gothong MNHS', 'University of Cebu SHS Department', 'Cebu Institute of Technology University (CIT-U)'],
            'Year': ['2009-2015', '2015-2019', '2019-2021', '2021-Present']
        }
        education_df = pd.DataFrame(education_data)
        st.table(education_df)

    st.subheader("Career Beginnings")
    st.write("""
    I am currently a College Student specializing in Information Technology. 
    My academic journey includes being an academic scholar and achieving high honors throughout my high school and college education.
    """)

    st.subheader("Achievements")
    st.write("""
    - Special Science Class Program (Elementary and High School)
    - Best in ICT (2018 - 2019)
    - Consistent Honor Student since High School
    - Top 8 overall BSIT 2nd year level
    - Parangal Awardee, CIT - U (2021-2022)
    - Course Passer (HCIE - Storage Course, Huawei Talent)
    - Course Passer (HCIP - Storage Course, Huawei Talent)
    - Course Passer (HCIA - Storage Course, Huawei Talent)
    - Course Passer (IRDO- Storage Course, Huawei Talent)
    """)

    st.subheader("Skills")
    st.write("**Technical Skills:** Python, SQL, Data Analysis, Web Development")
    st.write("**Soft Skills:** Leadership, Communication, Teamwork, Proper Time Management, Effective Communication Skills")
    st.write("**Languages:** Bisaya, Tagalog, English")

# Portfolio Tab
with tabs[2]:
    st.header("Portfolio")

    st.subheader("Professional Experience")
    st.write("""
    As a student, my portfolio is focused on academic projects and personal growth. I have a strong foundation in programming and have completed various projects in web development and data science.
    """)

    # Line Chart for skills progression
    st.subheader("Skills Progression Over Time")
    skills_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Python', 'SQL', 'Web Development']
    )
    if chart_type == "Line Chart":
        st.line_chart(skills_data)
    else:
        st.bar_chart(skills_data)

    # Slider to show engagement in projects
    st.subheader("Engagement in Projects")
    hours = st.slider(
        "Select the number of hours worked per week on projects", 0, 60, 40)
    st.write(f"You have selected {hours} hours per week.")

    # Map to display project locations
    if show_map:
        st.subheader("One of these dots is the place where I live 😂")
        df_map = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] +
            [10.31, 123.89],  # Cebu City coordinates
            columns=['lat', 'lon']
        )
        st.map(df_map)

# Contact Tab

with tabs[3]:
    st.header("Contact Me")

    st.write(
        "Feel free to reach out to me for collaboration, inquiries, or just a friendly chat!")

    contact_info = {
        "Phone": "123-456-7890",
        "Mobile Number": "123-456-7890",
        "Email": "alestaircyril12@gmail.com",
        "Address": "Cebu City, Philippines"
    }

    for key, value in contact_info.items():
        st.write(f"**{key}:** {value}")

    contact_form = """
    <style>
        form {
            display: flex;
            flex-direction: column;
            width: 300px;
            margin: 0;
        }
        input, textarea, button {
            margin-bottom: 10px;
            padding: 10px;
            font-size: 16px;
        }
        textarea {
            resize: vertical; /* Allow vertical resizing */
            height: 100px; /* Set a default height */
        }
    </style>
    <form action="https://formsubmit.co/alestaircyril12@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
# Footer
st.write("---")
st.write("© 2024 by Alestair Cyril Coyoca")
