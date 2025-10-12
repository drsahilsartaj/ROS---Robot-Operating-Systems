import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

THRESHOLD = 30.0

class TemperatureMonitor(Node):
    def __init__(self):
        super().__init__('temperature_monitor')
        self.sub = self.create_subscription(Float64, '/temperature', self.cb, 10)

    def cb(self, msg: Float64):
        temp = msg.data
        if temp > THRESHOLD:
            self.get_logger().warn(f'WARNING: temperature {temp:.2f} °C exceeds threshold {THRESHOLD} °C')
        else:
            self.get_logger().info(f'Temperature: {temp:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
