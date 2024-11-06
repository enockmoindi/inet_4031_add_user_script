# INET 4031 Add Users Script

## Program Description

This project provides a batch user creation script designed for automating the addition of multiple users on a Linux system. The script reads user information from an input file and performs the following tasks:

- Creates user accounts with specified usernames and user details.
- Assigns users to designated groups as outlined in the input file.
- Ensures proper handling of errors and logs relevant actions.

This tool is especially useful for system administrators needing to onboard multiple users efficiently, ensuring consistent user account creation across systems.

## Program Operation

1. **Input File Format**: 
   - The `create-users.input` file should contain user details in the following format:
     ```
     username:password:last_name:first_name:group1,group2
     ```
   - Each line represents one user, with groups separated by commas. To exclude group assignments, use `-` in the group field.

2. **Script Execution**:
   - Run the script using:
     ```
     sudo ./create-users.py < create-users.input
     ```
   - Alternatively, to run with an explicit Python interpreter:
     ```
     sudo python3 create-users.py < create-users.input
     ```
   - The script will process each line in the input file, creating user accounts and assigning them to groups.

3. **Output**:
   - For each user, the script outputs progress messages:
     ```
     ==> Creating account for username...
     ==> Assigning username to the group group_name...
     ```
   - Errors and additional command details are saved in `errors.log` for troubleshooting.

4. **Log and Error Handling**:
   - If a line in the input file is incorrectly formatted, the script will skip it and proceed with the next line.
   - Group assignment and user creation errors are logged in the `errors.log` file for review.

## Additional Notes
This script is designed to streamline user management on Linux systems. Make sure to review any changes made to `/etc/passwd` and `/etc/group` after running the script.

## Troubleshooting
- If you encounter permission issues, verify that you have `sudo` privileges.
- Ensure that the input file format matches the expected structure to avoid errors.

## Author
Developed by Enock as part of the INET 4031 course project.

## Contact
For questions or feedback, please contact me via my [GitHub profile](https://github.com/enockmoindi).
