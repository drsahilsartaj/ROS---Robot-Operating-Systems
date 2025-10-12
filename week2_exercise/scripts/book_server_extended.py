#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from week2_exercise.srv import BookLookup
import difflib

class BookServerExtended(Node):
    def __init__(self):
        super().__init__('book_server_extended')
        self.srv = self.create_service(BookLookup, 'book_lookup', self.handle_book_lookup)
        self.catalog = {
            'The Great Gatsby': 'Shelf A3',
            '1984': 'Shelf B1',
            'To Kill a Mockingbird': 'Shelf C2',
            'Moby Dick': 'Shelf D4'
        }
        self.get_logger().info('Extended book server ready.')

    def handle_book_lookup(self, request, response):
        title_req = request.title
        self.get_logger().info(f'Received lookup request for: \"{title_req}\"')
        # exact match
        if title_req in self.catalog:
            response.available = True
            response.location = self.catalog[title_req]
            return response
        # case-insensitive substring match
        titles = list(self.catalog.keys())
        lower_titles = [t.lower() for t in titles]
        req_l = title_req.lower()
        for i,t in enumerate(lower_titles):
            if req_l in t:
                response.available = True
                response.location = self.catalog[titles[i]]
                return response
        # fallback: close match using difflib
        close = difflib.get_close_matches(title_req, titles, n=1, cutoff=0.4)
        if close:
            match = close[0]
            response.available = True
            response.location = self.catalog[match]
            return response
        response.available = False
        response.location = 'N/A'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = BookServerExtended()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
