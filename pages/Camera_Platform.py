# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Platform",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Helium-Ion Microscope Camera Adjustment Platform")
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
   This project aimed to streamline the process of adjusting the camera inside a 
   vacuum chamber of a Helium-Ion microscope. Typically, this adjustment process 
   required pressurizing and opening the chamber, a task that could take hours. 
   By designing and implementing a remotely operated platform, I significantly 
   reduced the adjustment time to just a few seconds, eliminating disruptions to 
   the microscope and improving overall efficiency.
    """
)

# Add GitHub button here
st.markdown(
    """
    <a href="https://gitlab.com/NORDvv/him-moving-platform" target="_blank">
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
    - **Python + QtPy:** The logic for PC GUI.
    - **SOLIDWORKS + 3D Printing:** Prototyping the platform.
    - **Arduino:** Electric motor control.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **3D-Printed Platform:** Designed a compact, custom platform using SOLIDWORKS to meet the stringent spatial constraints of the vacuum chamber.
    - **Motorized Movement:** Integrated an electric motor controlled by Arduino to enable precise, remote camera adjustments.
    - **User-Friendly Control Software:** Developed a PC-based control interface using QtPy, allowing seamless remote operation of the platform.
    - **Minimal Wiring:** Engineered the system to function with just a few wires, simplifying installation and reducing potential interference.
    
    """
)

# Add an image in the Key Features section
# st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Space Constraints:** The vacuum chamber's limited space required meticulous design and iterative prototyping to ensure the platform fit perfectly while supporting the camera securely.
    - **Motor Vibration:** Addressed vibration issues by fine-tuning the Arduino code to ensure smooth motor operation, preserving the microscope's precision.
    - **Learning New Tools:** As this was my first experience with QtPy, I had to quickly learn and apply the framework to create a functional GUI. This experience laid the groundwork for future GUI development projects.
    
    """
)
# - **Efficient Fitness Evaluation:** With 1,000 nodes, evaluating fitness scores (total travel distance) quickly became computationally intensive. I optimized the evaluation process to maintain performance without bottlenecks.    
# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    This project provided invaluable experience in end-to-end product development, 
    from design and prototyping to implementation and testing. The resulting 
    platform transformed a time-intensive and laborious task into a quick and 
    seamless operation, showcasing my ability to solve practical problems with 
    innovative solutions.
    """
)
