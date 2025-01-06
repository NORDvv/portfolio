#Tm commands to run this:
# source .venv/bin/activate
# streamlit run main_page.py

#To stop the environment:
# deactivate

import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Vlad's Portfolio",
    page_icon=":robot_face:",
    layout="centered"
)

# Portfolio Header
st.title("Welcome to My Portfolio!")
st.write(
    """
    I'm Vlad Nadtochii, a passionate software developer with a strong interest in robotics and embedded systems. 
    Below, you'll find a showcase of my projects, highlighting my skills and technologies I've worked with.
    Click on a project's title to learn more about it.
    """
)

# Define projects with links to their pages
projects = [
    {
        "title": "Robotic Soccer Control System",
        "description": "Developed multi-threaded software to control autonomous soccer robots.",
        "technologies": "C++, Qt, Protobuf",
        "link": "./SFURS",
    },
    {
        "title": "Mobile Manipulator Robot",
        "description": "A ROS2-based mobile manipulator robot integrating SLAM, motion planning, and simulation.",
        "technologies": "ROS2, Python, Gazebo, MoveIt",
        "link": "./Mobile_Robot",
    },
    {
        "title": "Multi-Dimensional Maze",
        "description": "A maze to explore various path search algorithms",
        "technologies": "C++",
        "link": "./Maze",
    },
    {
        "title": "Camera Platform",
        "description": "A system created for a Helium-Ion microscope",
        "technologies": "Python, Arduino, 3D printing, SOLIDWORKS",
        "link": "./Camera_Platform",
    },
    {
        "title": "Traveling Salesman Problem Optimazation",
        "description": "Solving TSP using genetic algorithms",
        "technologies": "Python",
        "link": "./TSP",
    },
    {
        "title": "Tic-Tac-Toe AI Game",
        "description": "Plaing Tic-Tac-Toe with Monte-Carlo Search",
        "technologies": "Python",
        "link": "./TicTacToe",
    },
    {
        "title": "Multi-Agent Path Search",
        "description": "Coordinating movements of multiple agents in a maze",
        "technologies": "Python",
        "link": "./MAPF",
    },
]

# Display projects with clickable titles
for project in projects:
    # Create a clickable title using Markdown
    st.markdown(f"### [{project['title']}]({project['link']})")
    st.write(project["description"])
    st.markdown(f"**Technologies:** {project['technologies']}")
    st.markdown("---")

# st.set_page_config(
#     page_title="Vlad's portfolio"
# )

# st.write("# Welcome to my portfolio!")

# st.markdown(
#     """
#     ### Summary:
#     Something about me.
    
#     ### My projects at a glance:
#     - Mobile manipulator
#     - Robotic Soccer
#     - RL
#     - Path finding
#     - STM32 project with RTOS
#     - Computer Vision
    
#     ### Grad level courses taken:
#     - Intelligent systems
#     - Computer Vision
#     - Math for machine learning
    
#     ### Online specializations and courses:
#     - Modern Roboitcs
#     - Reinforcement Learning
#     - ROS2
    
#     ### Other interesting achievements:
#     - Scuba diving
#     - Bread & pizza baking
# """
# )
