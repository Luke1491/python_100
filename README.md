# python_100

100 simple projects for 100 days

# Python Docker Runner Script

Run the script from root folder level.
This script facilitates running Python scripts within a Docker container. It takes a folder name as an argument, where the Python script to be executed resides. The script assumes there is only one Python file (`*.py`) within the specified folder.

## Prerequisites

- Docker installed on your system.

## Usage

1. Clone this repository or download the `run.sh` script.

2. Make sure the script is executable:

   ```bash
   chmod +x run.sh
   ```

3. Run the script with the folder name containing your Python script:

   ```bash
   ./run.sh foldername
   ```

   Replace `foldername` with the name of the folder containing your Python script.

4. The script will search for a Python file (`*.py`) within the specified folder and run it using Docker.

## Example

Suppose you have a folder named `my_python_scripts` containing a Python script named `hello_world.py`. To run this script using the provided script:

```bash
./run.sh my_python_scripts

```

example to run project from day 1:

```bash
./run.sh 1
```
