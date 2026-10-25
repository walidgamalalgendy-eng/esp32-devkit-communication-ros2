This project establishes a communication bridge between an **ESP32 DevKit** (running Arduino firmware) and a **ROS 2 Python node** to perform remote calculations (adding two numbers) over the network.

## Project Structure
- `esp_calc.py`: The ROS 2 Python node located inside a ROS 2 package, responsible for taking two numbers from the terminal and sending them.
- `sketch_oct24a.ino`: The ESP32 Arduino firmware responsible for network configuration and handling the calculation logic.

## How It Works & Setup Instructions

1. **ESP32 Network Configuration (`sketch_oct24a.ino`)**:
   - Flash the Arduino code to your ESP32 using the Arduino IDE.
   - Configure your Wi-Fi credentials (SSID and Password) inside the firmware.
   - Open the **Arduino IDE Serial Monitor** to check and copy the assigned **ESP32 IP address**.

2. **ROS 2 Integration (`esp_calc.py`)**:
   - Place the Python script inside your ROS 2 package workspace.
   - Update the **ESP32 IP** variable in the ROS 2 Python code with the IP address you obtained from the Arduino Serial Monitor.

3. **Execution**:
   - Run the ROS 2 node from your terminal:
     ```bash
     ros2 run <your_package_name> esp_calc
     ```
   - Input two numbers directly from the terminal, and the system will send them to the ESP32 to compute the addition.
