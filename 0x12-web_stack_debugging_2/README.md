0x12. Web stack debugging #2
Overview
This project focuses on enhancing security practices related to user permissions and configuring Nginx within a container. It includes a Bash script that accepts a username as an argument and runs the whoami command under the specified user. Additionally, there's a script to configure a container so that Nginx runs as the nginx user, listening on all active IPs on port 8080.

Table of Contents
Root User Script
Nginx Configuration Script
Debugging Information
Repository Information
Root User Script
Script Name: check_user.sh
Usage
./check_user.sh <username>
This Bash script takes a username as an argument and runs the whoami command under the specified user.
Example usage:
./check_user.sh www-data
Nginx Configuration Script
Script Name: 1-run_nginx_as_nginx
Requirements
Nginx must be running as the nginx user.
Nginx must be listening on all active IPs on port 8080.
Avoid using apt-get remove.
Usage
./1-run_nginx_as_nginx
This Bash script configures the container to meet the specified Nginx requirements.
Debugging Information
After running the Nginx Configuration Script, check the following:
# Check Nginx processes
ps auxff | grep ngin[x]

# Verify Nginx port 8080 is listening
nc -z 0 8080 ; echo $?
Repository Information
GitHub Repository: alx-system_engineering-devops
Directory: 0x12-web_stack_debugging_2
File: 1-run_nginx_as_nginx
Feel free to explore and contribute to the project! If you encounter any issues or have suggestions for improvement, please open an issue in the repository.
