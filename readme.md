 Brut

Brut is a simple brute force program developed for educational and legal purposes. It currently supports SSH brute force attempts using a password list to crack login credentials. The program is designed to be extensible, allowing additional brute force options to be added in the future.

## Features

- **SSH Brute Force:** 
  - The program allows users to attempt SSH login using a password list.
  
- **Future Options:**
  - More brute force methods will be added in the future.

## Requirements

Before running the program, you need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

Dependencies:
- `colorama`: A library for colored terminal output.
- `paramiko`: A Python library used for SSH connections.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrsajadpp/brut.git
   ```

2. Navigate into the project directory:

   ```bash
   cd brut
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Program

To start the program, simply run:

```bash
python brut.py
```

Once the program is running, you will see the following options:

1. **SSH Brute Force**:
   - Select option `1` to begin the SSH brute force.
   - Input the target IP address, username, and the path to the password list file.
   - The program will attempt to login using each password in the list.

### Example

```
Choose which brute force you need:
-------------------------------------------------
1 : SSH
-------------------------------------------------
Enter your choice: 1
Enter IP Address: 192.168.1.1
Enter Username: root
Enter Password List: /path/to/passwords.txt
```

### Error Handling

- If the password list file is not found, you will receive an error message indicating that the file path is invalid.
- If an error occurs during the connection attempt, it will be displayed in red.

## Warnings

This program is developed **only** for **educational and legal purposes**. Unauthorized access to computer systems is illegal and unethical. Please use this program responsibly and only on systems where you have explicit permission.

## Contributing

Feel free to contribute to this project by creating pull requests or opening issues for any bugs or suggestions.

## License

This project is licensed under the **GNU General Public License, Version 2, June 1991**. See the [LICENSE](LICENSE) file for details.

## Contact

Program developed and maintained by [mrsajadpp](https://github.com/mrsajadpp).