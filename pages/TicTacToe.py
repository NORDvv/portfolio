# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Tic-Tac-Toe AI Game",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Tic-Tac-Toe AI Game")
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
    This project is a simple AI-driven Tic-Tac-Toe game developed as part of 
    my university curriculum. Designed with a straightforward command-line 
    interface, the game allows players to challenge an AI opponent that uses 
    a Monte-Carlo search algorithm to determine its moves. While the AI isn't 
    unbeatable, it's challenging enough to make each game engaging and strategic.
    """
)

# Add GitHub button here
st.markdown(
    """
    <a href="https://gitlab.com/NORDvv/tic-tac-toe" target="_blank">
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
    - **Monte-Carlo Search Algorithm:** Searching the best moves for the agent.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **AI-Driven Gameplay:** The AI uses a Monte-Carlo search algorithm to evaluate potential moves, aiming to maximize its chances of victory while minimizing the risk of loss.
    - **User Options:** Players can choose to play first (as crosses) or second (as zeros), providing flexibility in gameplay experience.
    - **Simple Command-Line Interface:** A clean and intuitive interface ensures that the game is easy to play and understand.
    - **Dynamic Decision-Making:** The AI adapts its strategy based on game progress, providing a balanced challenge for the player.    
    """
)

# Add an image in the Key Features section
# st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Configuring the Monte-Carlo Search Algorithm:** The key challenge was assigning appropriate weights to potential game outcomes—victory, draw, or loss—within the Monte-Carlo framework. Through iterative testing and fine-tuning, I optimized the scoring system to produce competitive AI performance.
    - **Balancing Challenge and Playability:** Ensuring the AI was neither too weak nor too overpowering required testing against multiple strategies and refining its decision-making parameters.    
    """
)

# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    This project served as my introduction to artificial intelligence and 
    decision-making algorithms. It provided valuable insights into the 
    implementation of game-playing AI and the practical application of 
    Monte-Carlo methods. The experience laid the foundation for future 
    projects in AI, combining problem-solving skills with 
    algorithmic thinking.
    """
)
