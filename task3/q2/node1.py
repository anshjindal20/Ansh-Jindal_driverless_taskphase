import rclpy
from rclpy.node import Node
from driverless_msgs.msg import RT2String

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('node_1')
    pub = node.create_publisher(RT2String, '/user_string', 10)
    
    node.get_logger().info('Node 1 Started. Type strings in the terminal.')
    
    while rclpy.ok():
        try:
            user_input = input("Enter a string (e.g. AABAA): ")
            msg = RT2String()
            msg.data = user_input
            pub.publish(msg)
            node.get_logger().info(f'Published: "{user_input}"')
        except KeyboardInterrupt:
            break
            
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
