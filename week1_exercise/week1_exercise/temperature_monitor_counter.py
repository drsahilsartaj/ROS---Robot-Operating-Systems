import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

THRESHOLD = 30.0
WINDOW = 20

class TemperatureMonitorCounter(Node):
    def __init__(self):
        super().__init__('temperature_monitor_counter')
        self.sub = self.create_subscription(Float64, '/temperature', self.cb, 10)
        self.readings = []

    def cb(self, msg: Float64):
        temp = msg.data
        self.readings.append(temp)
        if len(self.readings) > WINDOW:
            self.readings.pop(0)
        if temp > THRESHOLD:
            self.get_logger().warn(f'WARNING: temperature {temp:.2f} °C exceeds threshold {THRESHOLD} °C')
        else:
            self.get_logger().info(f'Temperature: {temp:.2f} °C')
        if len(self.readings) == WINDOW:
            violations = sum(1 for t in self.readings if t > THRESHOLD)
            percent = (violations / WINDOW) * 100.0
            self.get_logger().info(f'Last {WINDOW} readings: {violations}/{WINDOW} exceed threshold -> {percent:.1f}%')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitorCounter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
