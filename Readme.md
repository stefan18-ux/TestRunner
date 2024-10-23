# Pseudo-Random Number Generator and Controller

This project consists of two Python programs: 
1. **Program A**: A pseudo-random number generator.
2. **Program B**: A controller that interacts with Program A, retrieves random numbers, and performs some statistical analysis.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Running Program A](#running-program-a)
  - [Running Program B (Controller)](#running-program-b-controller)
- [Behind the scenes](#behind-the-scenes)

## Description

This project demonstrates interaction between two Python programs:
- **Program A** is a pseudo-random number generator that responds to commands from standard input. It can:
  - Reply with "Hi" when asked.
  - Generate a random integer when prompted.
  - Shut down gracefully upon receiving a shutdown command.

- **Program B (Controller)** is responsible for:
  - Launching Program A as a subprocess.
  - Interacting with Program A to retrieve 100 random numbers.
  - Calculating and displaying statistics (median and average) from the retrieved numbers.
  - Ensuring Program A is gracefully shut down after the process.

## Requirements

To run the programs, you need:
- **Python 3.x** installed on your system.
- No additional external libraries are required, as the necessary Python modules (`subprocess`, `statistics`, etc.) are part of the Python standard library.

## Usage

### Running Program A

Program A is the random number generator that listens for commands via stdin and responds with appropriate outputs. 

To run **Program A** directly, use the following command:

```bash
python3 program_a.py
```
Example of interaction with **Program A**:

```bash
$ python3 program_a.py
Hi
# Output: Hello! I am Program A.
GetRandom
# Output: 823
Shutdown
# Output: Program A is shutting down...
```

### Running Program B (Controller)
To run **Program B**, you need to specify the filename of **Program A** as an argument. The command to launch **Program B** is:

```bash
python3 controller.py program_a.py
```
This will:
- Start **Program A** as a subprocess.
- Send the `"Hi"` command to **Program A** and check its response.
- Send the `"GetRandom"` command 100 times to retrieve 100 random numbers.
- Sort the retrieved random numbers and calculate both the **median** and **average**.
- Shut down **Program A** gracefully by sending the `"Shutdown"` command.

### Behind the scenes

The script `program_B.py` starts a subprocess by running the script `program_A.py`. The two programs communicate via `stdin` and `stdout` in the following way:

- When the subprocess is created, the `stdin` and `stdout` of it are connected to the main process using **`subprocess.PIPE`**. This allows the main process to control the flow of data to the child process.
- Running a command like **`process.stdin.write(b'Hi\n')`** sends the byte string **`b'Hi\n'`** to the `stdin` of the subprocess.
- In the subprocess, a loop such as **`for line in sys.stdin:`** reads the last written line from its `stdin` and executes a command based on the value of the **`line`** string.
- If the executed command involves a **`print`**, that string is printed and saved in a buffer. The buffer is then flushed to `stdout` using **`sys.stdout.flush()`**.
- After flushing, the main process retrieves the output as a byte string, which can be converted into a normal string for further use.
- The subprocess terminates gracefully when no more input is provided to `stdin`, or when the `"Shutdown"` command is given. In either case, no more lines are read from **`sys.stdin`**, or the loop ends due to a `break` statement.
