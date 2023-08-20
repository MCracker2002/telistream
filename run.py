import subprocess

# Create a virtual environment
subprocess.run(['python3', '-m', 'venv', './venv'])

# Activate the virtual environment
subprocess.run(['./venv/bin/activate'], shell=True)

# Install the required packages from requirements.txt
subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

# Run the WebStreamer module
subprocess.run(['python3', '-m', 'WebStreamer'])
