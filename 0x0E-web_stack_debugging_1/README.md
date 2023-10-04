# Web Stack Debugging 1 :wrench:

This repository contains a set of tasks focused on debugging and configuring an Nginx web server running on an Ubuntu 20.04 LTS server. The tasks aim to help you develop debugging skills and resolve common issues that may arise when working with web servers.

## Tasks :clipboard:

### Task 0: Nginx Likes Port 80 :mag_right:

In this task, you will use your debugging skills to identify and fix an issue that prevents the Nginx web server from listening on port 80. The goal is to ensure that Nginx is running and properly configured to listen on port 80 of all the server's active IPv4 IPs.

### Task 1: Make It Sweet and Short :candy:

Building on Task 0, this task challenges you to create a more concise Bash script, limited to five lines or less. The script should still configure Nginx to listen on port 80 and restart the Nginx service. Additionally, it should correctly indicate that Nginx is not running.

## Requirements :memo:

- All Bash scripts must be executable.
- Bash scripts must pass Shellcheck without any errors.
- Bash scripts must run without error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining the script's purpose.
- You are not allowed to use `wget`.
