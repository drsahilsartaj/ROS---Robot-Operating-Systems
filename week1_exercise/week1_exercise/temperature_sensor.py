import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.pub = self.create_publisher(Float64, '/temperature', 10)
        self.create_timer(1.0, self.publish_temp)

    def publish_temp(self):
        val = random.uniform(15.0, 45.0)
        msg = Float64()
        msg.data = float(val)
        self.pub.publish(msg)
        self.get_logger().info(f'Published temperature: {msg.data:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
