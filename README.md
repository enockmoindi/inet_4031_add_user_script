# inet_4031_adduser_script

# Automating User Creation with Python

## Description
This script automates the creation of multiple user accounts on an Ubuntu system. It reads from an input file that contains user information and configures user accounts accordingly.

## Features
- Automates the creation of user accounts.
- Assigns users to groups specified in the input file.
- Sets user passwords securely.
- Skips commented or incorrectly formatted lines in the input file.

## Prerequisites
- Python 3.x installed on your system.
- Ubuntu system with `adduser` and `passwd` commands available.
- Elevated permissions (`sudo`) to run the script.

## Installation
Clone the GitHub repository:
```bash
git clone https://github.com/yourusername/inet_4031_adduser_script.git
cd inet_4031_adduser_script
