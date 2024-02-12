# Web-01 Firewall Configuration

This repository contains a script to configure the firewall on the web-01 server using Uncomplicated Firewall (ufw). The script is designed to block all incoming traffic except for specified TCP ports (22 for SSH, 80 for HTTP, and 443 for HTTPS).

## Usage

cd web-01-firewall-config
./configure_firewall.sh

This script installs ufw if not already installed, resets ufw to default settings (optional), sets default incoming policy to deny, allows outgoing traffic, permits SSH, HTTP, and HTTPS, and finally, enables ufw. The script also displays the ufw status in verbose mode.

File Structure
configure_firewall.sh: The main script file for configuring the firewall.
README.md: This readme file providing instructions and information about the repository.
Requirements
The script is designed for the web-01 server, but it can be adapted for other servers if needed.
Make sure to run the script with elevated privileges using sudo.
Notes
Ensure that you have SSH access to the server before running the script.
Review the script to understand the firewall rules and adjust them based on your specific requirements.


