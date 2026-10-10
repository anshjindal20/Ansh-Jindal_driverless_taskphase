import rclpy
from rclpy.node import Node
from driverless_msgs.msg import RT2String
from driverless_msgs.srv import PalindromeCheck

class Node2(Node):
    def __init__(self):
        super().__init__('node_2')
        # Subscribes to Node 1
        self.subscription = self.create_subscription(
            RT2String, '/user_string', self.string_callback, 10)
        # Client to call Node 3
        self.cli = self.create_client(PalindromeCheck, '/verify_status')

    def string_callback(self, msg):
        text = msg.data
        # Check if string reads the same forwards and backwards
        is_palindrome = (text == text[::-1])
        status_val = 1 if is_palindrome else 0
        
        self.get_logger().info(f'Received "{text}". Sending {status_val} to Node 3...')
        
        # Wait for Node 3 to be online
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for Node 3 service...')
            
        # Call Node 3 asynchronously
        req = PalindromeCheck.Request()
        req.input_status = status_val
        future = self.cli.call_async(req)
        future.add_done_callback(self.service_response_callback)

    def service_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Node 3 conveyed: {response.response}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
