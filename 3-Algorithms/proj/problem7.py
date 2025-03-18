## The Router class will wrap the Trie and handle 
from re import split

class TrieNode(object):
    def __init__(self):
        self.handler = None
        self.children = {}

class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        self.root = TrieNode()
        self.root.handler = root_handler
        self.not_found_handler = not_found_handler
        
    def add_handler(self, route, handler):
        # Add a handler for a path
        # Split the path and pass the parts as a list to navigate the Trie
        path_parts = self.split_path(route)
        
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.children[part] = TrieNode()
            current_node = current_node.children[part]
        
        current_node.handler = handler
    
    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        path_parts = self.split_path(route)
        
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[part]
        
        if current_node.handler is None:
            return self.not_found_handler
        return current_node.handler
    
    def split_path(self, route):
        # Split the path into parts
        # Handle trailing slashes by removing empty strings
        if route == "/":
            return []
        
        parts = route.split("/")
        # Remove empty strings (occurs with leading/trailing slashes)
        return [part for part in parts if part]

## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'