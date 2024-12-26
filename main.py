import os
import sys
import subprocess

def execute_command(command):
    if command.startswith("cd"):
        try:
            path = command.split(" ")[1]
            os.chdir(path)
        except IndexError:
            print("cd: missing argument")
        except FileNotFoundError:
            print(f"cd: no such file or directory: {path}")
    elif command == "exit":
        print("Exiting shell...")
        sys.exit(0)
    else:
        try:
            result = subprocess.run(command, shell=True, check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

def main():
    while True:
        current_dir = os.getcwd()
        command = input(f"PyShell/{current_dir}/> ")

        command = command.strip()

        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
