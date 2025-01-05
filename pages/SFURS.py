# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SFURS",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Robotic Soccer Software Development")
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
    As the Lead Software Developer for our university’s robotics soccer team, 
    I spearheaded the design and development of a modular software system to 
    autonomously control robots during competitive matches. This collaborative 
    project involved creating an integrated GUI, implementing modular software 
    architecture, and developing AI-driven coordination for robotic movements 
    and strategies.
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
    - **C++:** Most of the logic.
    - **Qt6:** GUI creation and for module communication.
    - **Protobuf:** Message handling.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **Modular Software Architecture:** Designed a robust modular architecture with 
    four distinct components: AI, Communication, GUI, and Network. Each module was 
    designed for independent development, fostering encapsulation and seamless 
    integration.
    - **AI Submodules:**
        - *Team Coordination:* Responsible for developing team strategies like formations and transitions between attack and defense.
        - *Pair Coordination:* Facilitated actions like passing and intercepting while maintaining strategic pair interactions.
        - *Personal Coordination:* Focused on collision avoidance, boundary adherence, and individual robot behaviors.
    - **Communication Module:** Utilized Qt6 sockets to handle internal data exchange and logging, inspired by ROS2 DDS protocols.
    - **GUI:** Provided an intuitive interface for configuring robot behaviors and troubleshooting the system.
    - **Network Module:** Managed external communication with the simulator and game environment using Protobuf for protocol translation.

    - **Scalable Collaboration:** Enabled team members to work independently on modules with clear input-output interfaces, minimizing dependencies.
    - **Integrated Functionality:** Built a system capable of real-time robot coordination, GUI interaction, and basic gameplay formation control.    
    """
)

# Add an image in the Key Features section
# st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Complexity of Team and Pair Coordination:** Addressing dynamic gameplay 
    strategies with multiple variables was daunting. While Reinforcement 
    Learning (RL) was considered, we opted for rule-based heuristics due to 
    time constraints. This approach allowed us to implement basic team formations 
    and strategic movements effectively.

    - **Team Leadership and Conflict Resolution:** As the lead, I navigated differing 
    architectural visions with the team manager, ensuring alignment through 
    consistent communication and thorough documentation. I also focused on 
    onboarding and mentoring new team members to address frequent turnover.

    - **Resource Constraints:** Balancing student schedules and varying levels of 
    expertise required adaptive planning. Modular architecture proved invaluable, 
    enabling contributors to focus on isolated aspects without disrupting overall 
    progress.    
    """
)

# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    This project was a milestone in my career, offering invaluable lessons in 
    software architecture, collaborative development, and leadership. It deepened 
    my expertise in C++ and Qt6 while fostering problem-solving skills in dynamic 
    and resource-constrained environments. The final software system, capable of 
    robot coordination, GUI integration, and strategic gameplay, was successfully 
    documented and handed over for future development.
    """
)
