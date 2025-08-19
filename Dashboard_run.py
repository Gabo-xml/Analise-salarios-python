import sys, os, subprocess

APP_FILE = "App.py"

def main():
    cmd = [sys.executable, "-m", "streamlit", "run", APP_FILE, "--server.runOnSave=true"]

    if os.name == 'nt':  # Windows
        subprocess.run(cmd, check=True)
    else:  # macOS and Linux
        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()