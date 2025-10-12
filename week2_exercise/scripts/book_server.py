#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from week2_exercise.srv import BookLookup

class BookServer(Node):
    def __init__(self):
        super().__init__('book_server')
        self.srv = self.create_service(BookLookup, 'book_lookup', self.handle_book_lookup)
        self.catalog = {
            'The Great Gatsby': 'Shelf A3',
            '1984': 'Shelf B1',
            'To Kill a Mockingbird': 'Shelf C2',
            'Moby Dick': 'Shelf D4'
        }
        self.get_logger().info('Book server ready.')

    def handle_book_lookup(self, request, response):
        title = request.title
        self.get_logger().info(f'Received lookup request for: "{title}"')
        if title in self.catalog:
            response.available = True
            response.location = self.catalog[title]
        else:
            response.available = False
            response.location = 'N/A'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = BookServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
