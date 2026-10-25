import sys
import socket
import rclpy
from rclpy.node import Node

class ESP32CalcNode(Node):
    def __init__(self):
        super().__init__('esp32_calc_node')
        
 
        self.esp_ip = 'ENTER YOUR ESP32 IP FROM SERIAL MONITOR ' 
        self.esp_port = 8888

   
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(3.0) #


        num1 = sys.argv[1] if len(sys.argv) > 2 else '10'
        num2 = sys.argv[2] if len(sys.argv) > 2 else '20'

        self.calculate_on_esp(num1, num2)

    def calculate_on_esp(self, a, b):
        msg = f"{a},{b}"
        self.get_logger().info(f"Sending numbers ({a}, {b}) to ESP32...")
        
        try:
     
            self.sock.sendto(msg.encode('utf-8'), (self.esp_ip, self.esp_port))
            
  
            data, _ = self.sock.recvfrom(1024)
            result = data.decode('utf-8')
            self.get_logger().info(f"Result from ESP32 = {result}")
            
        except socket.timeout:
            self.get_logger().error("ESP32 did not respond! Check IP and Wi-Fi.")

def main(args=None):
    rclpy.init(args=args)
    node = ESP32CalcNode()
    rclpy.shutdown()