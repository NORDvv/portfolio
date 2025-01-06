# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Mobile Manipulator Robot",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Mobile Manipulator Robot")
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
    The mobile manipulator combines the mobility of a wheeled base with the dexterity of a robotic arm. 
    This enables it to perform tasks like object manipulation, pick-and-place operations, and autonomous navigation 
    in dynamic environments. The project utilized Gazebo for simulation and ROS2 for control and coordination.
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
#st.image("images/mm1.jpeg", caption="Simulated view of the mobile manipulator in Gazebo.", use_container_width=False)

# Section: Technologies
st.header("Technologies Used")
st.markdown(
    """
    - **Robot Operating System (ROS2):** Integration and control of robot components.
    - **Gazebo:** Simulation environment for testing and fine-tuning the robot's behavior.
    - **MoveIt:** Motion planning and trajectory optimization.
    - **Python:** Development of robot behavior and control algorithms.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **SLAM (Simultaneous Localization and Mapping):** Enables the robot to create maps of its environment and 
      navigate autonomously.
    - **Motion Planning:** Ensures smooth and collision-free movements for both the base and the arm.
    - **End-Effector Control:** Allows the robot to manipulate objects with precision.
    """
)

# Add an image in the Key Features section
#st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Challenge:** Integrating SLAM with the manipulator's movement.
      - **Solution:** Fine-tuned the ROS2 node coordination to achieve seamless integration.
    - **Challenge:** Simulating realistic environments in Gazebo.
      - **Solution:** Used detailed models and physics parameters to replicate real-world conditions.
    """
)

# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    The mobile manipulator project demonstrates expertise in robotics software development, including SLAM, 
    motion planning, and simulation. It showcases my ability to design and implement complex robotic systems 
    while leveraging industry-standard tools and technologies.
    """
)
