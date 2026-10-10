import rclpy
from rclpy.node import Node
from driverless_msgs.srv import PalindromeCheck

class Node3(Node):
    def __init__(self):
        super().__init__('node_3')
        self.srv = self.create_service(PalindromeCheck, '/verify_status', self.status_callback)
        self.get_logger().info('Node 3 Service Server is Ready.')

    def status_callback(self, request, response):
        if request.input_status == 1:
            response.response = "Yes"
        elif request.input_status == 0:
            response.response = "No"
        else:
            response.response = "Invalid"
            
        self.get_logger().info(f'Received status {request.input_status}, replying with "{response.response}"')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = Node3()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
