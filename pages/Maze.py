# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Maze",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Multi-Dimensional Maze Navigation")
# st.write(
#     """
#     This project showcases the development of a ROS2-based mobile manipulator robot. The system integrates SLAM, 
#     motion planning, and simulation, demonstrating advanced robotic capabilities.
#     """
# )

# Section: Overview
st.header("Overview")
st.write(
    """
    The Multi-Dimensional Maze project is a C++ implementation 
    designed to explore algorithms for navigating mazes in 
    higher-dimensional spaces. The current implementation supports 
    a 5-dimensional grid, where pathfinding algorithms like 
    Breadth-First Search (BFS) have been successfully applied, and 
    A* is in progress. This project demonstrates the challenges and 
    solutions associated with representing and navigating 
    multi-dimensional spaces.
    """
)

# Add GitHub button here
st.markdown(
    """
    <a href="https://gitlab.com/NORDvv/mobile-manipulator" target="_blank">
        <button style="
            background-color:#4CAF50; 
            color:white; 
            padding:10px; 
            border:none; 
            cursor:pointer; 
            font-size:16px;">
            View Project on GitLab
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Add another image in the Overview section
# st.image("images/mm1.jpeg", caption="Simulated view of the mobile manipulator in Gazebo.", use_container_width=False)

# Section: Technologies
st.header("Technologies Used")
st.markdown(
    """
    - **C++:** The logic.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **Flexible Maze Representation:** Designed the maze as a series of 2D arrays, enabling navigation in grids of arbitrary dimensions by calculating rows and columns from multi-dimensional coordinates.
    - **Pathfinding Algorithms:** Implemented BFS for reliable pathfinding in a 5-dimensional maze. Ongoing work includes integrating A* to enhance search efficiency.
    - **Extensible Framework:** Designed the project to accommodate future additions like Reinforcement Learning (RL) and Multi-Agent Pathfinding (MAPF).
    
    """
)

# Add an image in the Key Features section
# st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Representing Multi-Dimensional Grids:** Representing higher-dimensional spaces in memory posed a significant challenge. I solved this by using a series of 2D arrays, which simplifies navigation by reducing the problem to well-understood row-column calculations.
    - **Algorithm Adaptation:** Adapting pathfinding algorithms like BFS to work seamlessly in higher dimensions required careful consideration of how neighbors are calculated.
    - **Scalability:** Ensuring that the framework remains extensible for future enhancements like RL or MAPF involved thoughtful planning of the data structures and modular design.
    
    """
)
# - **Efficient Fitness Evaluation:** With 1,000 nodes, evaluating fitness scores (total travel distance) quickly became computationally intensive. I optimized the evaluation process to maintain performance without bottlenecks.    
# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    The Multi-Dimensional Maze project highlights my ability to approach 
    abstract problems with practical solutions. It has been a rewarding 
    exercise in both algorithmic design and software architecture, with 
    exciting potential for future exploration in advanced pathfinding 
    techniques and multi-agent coordination.
    """
)
