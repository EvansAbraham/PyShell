# Simple Python Shell

A simple command-line shell written in Python that mimics some basic functionalities of a terminal, such as navigating directories with `cd` and executing system commands. This script provides an interactive shell where users can input commands, navigate directories, and execute system commands directly from the shell.

## Features

- **Change Directory (`cd`)**: Navigate to a different directory.
- **Exit Command**: Exit the shell session with the `exit` command.
- **System Command Execution**: Execute any system command available on your machine, such as `ls`, `echo`, etc.
- **Error Handling**: Handle errors for invalid commands and paths.

## Requirements

- Python 3.x

No external dependencies are required. This shell uses the built-in `os`, `sys`, and `subprocess` modules.

## How to Use

### Running the Shell

To run the shell, simply execute the script in your terminal:

```bash
python main.py
```

You will be presented with a prompt similar to:

```bash
PyShell/yourcurrentdirectory/>
```

At this point, you can enter commands:

- **Navigate Directories**: Use `cd <directory_path>` to change the current working directory.
  ```bash
  PyShell/yourcurrentdirectory/> cd /path/to/directory
  ```
  
- **Execute Commands**: Type any system command (like `ls`, `echo`, etc.) and it will be executed.
  ```bash
  PyShell/yourcurrentdirectory/> ls
  ```

- **Exit the Shell**: Use `exit` to terminate the shell session.
  ```bash
  PyShell/yourcurrentdirectory/> exit
  Exiting shell...
  ```

### Error Handling

- **Missing Argument in `cd`**: If you use `cd` without providing a directory path, the shell will inform you.
  ```bash
  cd: missing argument
  ```

- **Invalid Directory in `cd`**: If you attempt to `cd` to a non-existent directory, an error will be shown.
  ```bash
  cd: no such file or directory: /path/to/nonexistent/directory
  ```

- **Command Execution Failure**: If an external command fails, the error message will be shown.
  ```bash
  Error executing command: Command 'invalidcommand' returned non-zero exit status 127.
  ```

## Code Explanation

1. **execute_command(command)**:
   - This function processes the input command.
   - If the command starts with `cd`, it tries to change the directory. It handles errors for missing arguments and non-existent directories.
   - If the command is `exit`, it prints a message and exits the shell.
   - For any other command, it uses `subprocess.run` to execute the command and checks for errors.

2. **main()**:
   - The `main` function runs an infinite loop where it continuously asks the user for input, processes the command, and calls `execute_command` to handle it.

3. **Error Handling**:
   - The script includes error handling for missing command arguments and failed command execution. It ensures the shell doesn't crash unexpectedly.

## Contributing

Feel free to fork the repository, report issues, or make improvements through pull requests. Contributions are welcome!


