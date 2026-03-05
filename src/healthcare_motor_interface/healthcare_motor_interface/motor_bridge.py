import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MotorBridge(Node):

    def __init__(self):
        super().__init__('motor_bridge')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        self.get_logger().info("Motor bridge running (simulation mode)")


    def cmd_callback(self, msg):

        linear = msg.linear.x
        angular = msg.angular.z

        self.get_logger().info(f"CMD_VEL → {linear} , {angular}")


def main(args=None):

    rclpy.init(args=args)

    node = MotorBridge()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
