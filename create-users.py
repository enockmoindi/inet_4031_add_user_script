#!/usr/bin/python3


### Student Name: Enock Moindi
### Program Name: create-users.py script
### Program Creation Date: 2024-11-02
### Prgram Last Updated Date: 2024-11-06


# Import necessary libraries
import os
import re
import sys

def main():
    for line in sys.stdin:
        # This regular expression checks for lines starting with '#' (commented lines)
        match = re.match("^#", line)

        # Split the line into fields by ':'
        fields = line.strip().split(':')

        # Skip lines that are comments or do not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user details from fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Formatted comment field (gecos)
        groups = fields[4].split(',')  # Split group names by commas

        # Print message indicating account creation
        print("==> Creating account for %s..." % (username))

        # Construct the command to create the user (with 'sudo' to ensure elevated privileges)
        cmd = "sudo /usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Print the command for debugging
        print("Running command:", cmd)

        # Execute the command
        os.system(cmd)

        # Assign user to groups if applicable
        for group in groups:
            # Skip if group is '-'
            if group != '-':
                # Print message indicating group assignment
                print("==> Assigning %s to the %s group..." % (username, group))

                # Construct the command to add the user to the group (with 'sudo')
                cmd = "sudo /usr/sbin/adduser %s %s" % (username, group)

                # Print the command for debugging
                print("Running command:", cmd)

                # Execute the command to add user to group
                os.system(cmd)

if __name__ == '__main__':
    main()
