# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MAPF",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Multi-Agent Pathfinding (MAPF)")
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
   This project tackled the Multi-Agent Pathfinding (MAPF) problem, focusing on 
   enabling multiple agents to navigate to their goal positions efficiently and 
   without collisions. Based on foundational research from Professor Hang Ma, 
   the project explored several advanced algorithms to solve MAPF, including 
   space-time A*, prioritized planning, conflict-based search (CBS), and CBS 
   with disjoint splitting. Completed as part of a university course, this project 
   expanded my algorithmic expertise and introduced me to complex multi-agent 
   systems.
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
    - **Python:** The logic.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **Algorithm Diversity:** Implemented and compared multiple MAPF algorithms, including:
        - *Space-Time A*:* Ensures collision-free paths by integrating time as a dimension.
        - *Prioritized Planning:* Assigns priorities to agents to resolve conflicts.
        - *Conflict-Based Search (CBS):* Resolves conflicts iteratively by splitting search spaces.
        - *CBS with Disjoint Splitting:* An enhanced CBS approach that ensures more efficient conflict resolution.
    - **Scalability:** Designed to handle varying numbers of agents and goals while maintaining collision-free navigation.
    - **Research-Driven Development:** Developed under the guidance of Professor Hang Ma, aligning closely with cutting-edge MAPF methodologies.
    
    """
)

# Add an image in the Key Features section
# st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Understanding Advanced Algorithms:** Initially, grasping the nuances of CBS and disjoint splitting was challenging. Under Professor Ma’s supervision, I iteratively refined my understanding through research, experimentation, and application.
    - **Collision Avoidance in Dynamic Environments:** Ensuring agents avoided collisions while optimizing path length required meticulous algorithm tuning. Each method was tested extensively to validate collision-free paths under various configurations.
    
    """
)
# - **Efficient Fitness Evaluation:** With 1,000 nodes, evaluating fitness scores (total travel distance) quickly became computationally intensive. I optimized the evaluation process to maintain performance without bottlenecks.    
# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    This project deepened my understanding of algorithmic design and multi-agent 
    systems, showcasing the complexities of pathfinding in dynamic environments. 
    While the initial implementation was challenging, it fostered a strong 
    foundation in MAPF that I plan to build upon by re-implementing the project 
    with refined techniques and insights.
    """
)
