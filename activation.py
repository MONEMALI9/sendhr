def activate():
    import subprocess
    import os

    # Define the path to the directory containing your virtual environment
    venv_dir = 'sendhr'

    # Check if the virtual environment directory exists
    if not os.path.exists(venv_dir):
        print(f"Virtual environment directory '{venv_dir}' does not exist.")
        exit(1)

    # Construct the activation command based on the operating system
    if os.name == 'nt':  # For Windows
        activate_cmd = os.path.join(venv_dir, 'Scripts', 'activate')
    else:  # For Unix-based systems (Linux, macOS)
        activate_cmd = os.path.join(venv_dir, 'bin', 'activate')

    # Activate the virtual environment using subprocess
    try:
        subprocess.check_call(activate_cmd, shell=True)
        print(f"Activated virtual environment: {venv_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error activating virtual environment: {e}")
