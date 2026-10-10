import rclpy
from rclpy.node import Node
from driverless_msgs.msg import TaskOne

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('q1_publisher')
    pub = node.create_publisher(TaskOne, '/taskone', 10)
    
    try:
        while rclpy.ok():
            msg = TaskOne()
            # Taking input from the terminal
            msg.angvel = float(input("Enter angular velocity (rad/s): "))
            msg.radius = float(input("Enter radius (m): "))
            
            pub.publish(msg)
            node.get_logger().info(f'Published: angVel={msg.angvel}, radius={msg.radius}')
    except KeyboardInterrupt:
        pass
    except ValueError:
        node.get_logger().error("Invalid input. Please enter numbers.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '_main_':
    main()
