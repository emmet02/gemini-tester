
import sys


def greet(name: str):
    return f"Hello, {name}!"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
        print(greet(user_name))
    else:
        print("Usage: python main.py <name>")
