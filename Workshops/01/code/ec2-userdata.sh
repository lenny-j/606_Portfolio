#!/bin/bash
# EC2 User Data Script - TechStart Web Server
# This script runs automatically when the EC2 instance first launches

# Update all installed packages to the latest versions
yum update -y

# Install Apache HTTP Server (httpd)
yum install -y httpd

# Start the Apache service
systemctl start httpd

# Enable Apache to start automatically on boot
systemctl enable httpd

# Create a simple HTML page with the instance hostname
echo "<h1>TechStart Inc. - Web Server</h1><p>Instance: $(hostname)</p>" > /var/www/html/index.html
