# ROS2 Exercises – Week 1 & Week 2

This repo contains my ROS2 lab work for **Week 1** and **Week 2** done as part of my course.

---

## 🧩 [Week 1 – Temperature Sensor & Monitor](./week1_exercise)

In this exercise, I created:
- A **temperature sensor node** that publishes random temperature values.  
- A **monitor node** that subscribes to the sensor and prints the readings.  
- A **monitor counter node** that counts the received messages.  
All nodes were launched using a single launch file.  
The project was built and run using `colcon build` and `ros2 run`.

---

## 📚 [Week 2 – Book Lookup Service](./week2_exercise)

This exercise focused on **ROS2 services**:
- A **Book Server** node that provides book lookup info (title → location).  
- A **Book Client** node that requests data from the server.  
- An **Extended Server** version that allows partial or fuzzy matches.  
- Both were tested using ROS2 launch files and service calls.

---

## ⚙️ How to Run
```bash
# Source environment
source /opt/ros/jazzy/setup.bash
source install/setup.bash

# Example: run Week 2 server and client
ros2 run week2_exercise book_server.py
python3 src/week2_exercise/scripts/book_client.py
