# streamlit_page_name: Mobile Manipulator Robot 5555

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TSP",
    page_icon=":robot:",
    layout="centered"
)

# Header with image
# st.image("images/mm.jpeg", use_container_width=False)  # Replace with your image file path
st.title("Traveling Salesman Problem Solver")
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
   This project addresses the Traveling Salesman Problem (TSP), a 
   classic optimization challenge involving finding the shortest possible 
   route through 1,000 cities. Due to the computational infeasibility of 
   evaluating all possible combinations, I implemented a Genetic Algorithm 
   to approximate the shortest path. This project served as a final exam 
   replacement in my university course, demonstrating my ability to solve 
   complex computational problems efficiently.
    """
)

# Add GitHub button here
st.markdown(
    """
    <a href="https://gitlab.com/NORDvv/genetic-algorithm" target="_blank">
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
    - **Genetic Algorithms:** Searching for a shorter path.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    """
    - **Efficient Optimization:** The algorithm reduced the total travel distance by approximately 70%, demonstrating the power of heuristic-based solutions for large-scale optimization problems.
    - **Genetic Algorithm Implementation:** The solution uses a robust Genetic Algorithm that evolves combinations through mutation, selection, and crossover operations, ensuring all cities are visited exactly once.
    - **Scalable Design:** Designed to handle a high number of nodes (1,000 cities) efficiently while maintaining flexibility to adapt to other problem scales.
    - **Iterative Refinement:** The system continually improves the route by evaluating and selecting the best solutions across multiple generations.
    """
)

# Add an image in the Key Features section
# st.image("images/mm2.jpeg", caption="SLAM mapping and motion planning visualized in Rviz.", use_container_width=False)

# Section: Challenges and Solutions
st.header("Challenges and Solutions")
st.write(
    """
    - **Avoiding Local Minima:** One of the major challenges was preventing the algorithm from converging prematurely to suboptimal solutions. I achieved this by diversifying mutation types and implementing a controlled randomness in crossover operations to maintain genetic variety.
    - **Balancing Speed and Accuracy:** Fine-tuning the mutation and selection parameters was critical to producing meaningful results in a reasonable timeframe without sacrificing accuracy. Iterative testing and adjustments were employed to find the optimal balance.
    """
)
# - **Efficient Fitness Evaluation:** With 1,000 nodes, evaluating fitness scores (total travel distance) quickly became computationally intensive. I optimized the evaluation process to maintain performance without bottlenecks.    
# Section: Conclusion
st.header("Conclusion")
st.write(
    """
    This project demonstrated the effectiveness of Genetic Algorithms in solving 
    large-scale optimization problems. It also deepened my understanding of 
    heuristic methods, fitness evaluation, and iterative refinement techniques. 
    The experience equipped me with the ability to approach complex, 
    computationally intensive challenges with creative problem-solving strategies.
    """
)
