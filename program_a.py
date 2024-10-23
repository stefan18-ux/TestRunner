import sys
import random

def main():
    while True:
        command = sys.stdin.readline().strip()
        if command == "Hi":
            print("Hi")
            sys.stdout.flush()
        elif command == "GetRandom":
            print(random.randint(1, 1000000))  # Generating a random integer
            sys.stdout.flush()
        elif command == "Shutdown":
            break
        # Unknown commands are ignored

if __name__ == "__main__":
    main()
