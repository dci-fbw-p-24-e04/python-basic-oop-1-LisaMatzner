from stack import Stack


def reverse_string(my_string: str) -> str:
    rev_stack = Stack()

    for char in my_string:
        rev_stack.push(char)
    
    reversed_string = ""
    while not rev_stack.is_empty():
        reversed_string += rev_stack.pop()
    
    return reversed_string


if __name__ == "__main__":
    print(reverse_string("hello"))  # olleh
