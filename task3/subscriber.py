import rclpy
from rclpy.node import Node
from driverless_msgs.msg import TaskOne

class SpeedCalculator(Node):
    def __init__(self):
        super().__init__('q1_subscriber')
        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        speed = msg.angvel * msg.radius
        self.get_logger().info(f'Calculated Longitudinal Speed: {speed:.2f} m/s')

def main(args=None):
    rclpy.init(args=args)
    node = SpeedCalculator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '_main_':
    main()
