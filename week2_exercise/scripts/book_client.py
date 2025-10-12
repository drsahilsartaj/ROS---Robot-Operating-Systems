#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from week2_exercise.srv import BookLookup

def main():
    rclpy.init()
    node = Node('book_client_min')
    client = node.create_client(BookLookup, 'book_lookup')
    if not client.wait_for_service(timeout_sec=5.0):
        print("ERROR: service /book_lookup not available")
        rclpy.shutdown()
        return
    req = BookLookup.Request()
    req.title = "The Great Gatsby"
    fut = client.call_async(req)
    rclpy.spin_until_future_complete(node, fut)
    res = fut.result()
    if res is None:
        print("ERROR: service call failed")
    else:
        print(f'Book: "{req.title}" -> available={res.available}, location="{res.location}"')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
