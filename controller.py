import subprocess
import statistics
import sys

# The number of pseudo-numbers created.
LEN = 100

def main():
    # Check if a file argument was provided, otherwise default to 'program_a.py'
    if len(sys.argv) < 2:
        print("Error: No program name provided. Please specify the path to Program A.")
        sys.exit(1)  # Exit the script with a non-zero status to indicate an error

    file_name = sys.argv[1]  # First argument after the script name
    
    # Start Program A as a subprocess
    process = subprocess.Popen([sys.executable, file_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    # Send the "Hi" command and check the response
    process.stdin.write("Hi\n")
    process.stdin.flush()
    response = process.stdout.readline().strip()
    if response == "Hi":
        print("Program A responded with 'Hi'")

    # Send "GetRandom" command 100 times and collect random numbers
    random_numbers = []
    for _ in range(LEN):
        process.stdin.write("GetRandom\n")
        process.stdin.flush()
        number = int(process.stdout.readline().strip())
        random_numbers.append(number)

    # Send the "Shutdown" command to terminate Program A
    process.stdin.write("Shutdown\n")
    process.stdin.flush()
    process.wait()  # Wait for Program A to shut down

    # Sort the random numbers
    random_numbers.sort()

    # Print the sorted numbers
    print("Sorted random numbers:")
    print(random_numbers)

    # Calculate and print the median and average
    print(LEN // 2 - 1)
    median = random_numbers[LEN // 2 - 1]
    average = sum(random_numbers) / len(random_numbers)

    print(f"Median: {median}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()
