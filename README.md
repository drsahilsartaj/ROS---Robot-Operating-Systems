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
# Run commands (short)

# 1. Build (once / after changes)
cd /home/vscode/ros2_ws
source /home/vscode/ros2_venv/bin/activate
source /opt/ros/jazzy/setup.bash
colcon build --packages-select week2_exercise --symlink-install

# 2. Source workspace
source /home/vscode/ros2_ws/install/week2_exercise/share/week2_exercise/local_setup.bash

# 3. Start server (Terminal 1)
ros2 run week2_exercise book_server.py

# 4. Run client (Terminal 2)
# from workspace src folder:
cd /home/vscode/ros2_ws/src/week2_exercise
source /home/vscode/ros2_venv/bin/activate
source /opt/ros/jazzy/setup.bash
source /home/vscode/ros2_ws/install/week2_exercise/share/week2_exercise/local_setup.bash
python3 -u scripts/book_client.py

# 5. Extended server (optional)
ros2 launch week2_exercise book_lookup_extended.launch.py

