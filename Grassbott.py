
import subprocess
import time

def run_script():
    while True:
        # Start the subprocess
        print("Starting the script...")
        process = subprocess.Popen(['python', 'mainn.py', 'xx', '20'])

        # Let the script run for 120 minutes (7200 seconds)
        time.sleep(150)

        # Terminate the script after 120 minutes       print("Stopping the script...")
        process.terminate()

        # Wait for 2 minutes (120 seconds) before restarting
        print("Waiting for 2 minutes before restarting...")
        time.sleep(120)

# Start the loop
if __name__ == "__main__":
    run_script()
