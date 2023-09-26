# Web Server Configuration Project :open_book:

This project focuses on configuring an Nginx web server on an Ubuntu machine. Below are the tasks and objectives to be completed:

| Task                                | Description                                     |
| ----------------------------------- | ----------------------------------------------- |
| Task 0: Transfer a File to the Server | Transfer a file from client to server using SCP |
| Task 1: Install Nginx Web Server    | Install and configure Nginx web server          |
| Task 2: Setup a Domain Name         | Configure a domain name for the server          |
| Task 3: Redirection                 | Implement a 301 redirection from /redirect_me   |
| Task 4: Not Found Page (404)        | Configure a custom 404 page                     |
| Task 5: Install Nginx Web Server with Puppet | Install Nginx using Puppet                   |

## Task 0: Transfer a File to the Server

**Objective:** Create a Bash script that transfers a file from the client to the server using SCP (Secure Copy Protocol).

**Requirements:**
- Accept four parameters: path to the file, server IP, username, and SSH private key.
- Display usage instructions if parameters are missing.
- Use SCP to transfer the file to the user's home directory on the server.
- Disable strict host key checking.

## Task 1: Install Nginx Web Server

**Objective:** Install and configure the Nginx web server on the server machine.

**Requirements:**
- Install Nginx on the server.
- Configure Nginx to listen on port 80.
- Ensure that a GET request to the root ("/") returns a page containing the string "Hello World!"
- Implement this configuration via a Bash script.

## Task 2: Setup a Domain Name

**Objective:** Configure a domain name for the web server.

**Requirements:**
- Provide the domain name (e.g., example.tech) without subdomains.
- Configure DNS records with an A entry to point the root domain to the server's IP address.
- Update the project website URL in your profile.

## Task 3: Redirection

**Objective:** Implement a 301 redirection from "/redirect_me" to another web page.

**Requirements:**
- Perform a "301 Moved Permanently" redirection.
- Implement this configuration via a Bash script.
- The Bash script should also install Nginx and configure it to meet the requirements.

## Task 4: Not Found Page (404)

**Objective:** Configure a custom 404 page that displays the message "Ceci n'est pas une page."

**Requirements:**
- Return an HTTP 404 error code.
- The custom 404 page should contain the string "Ceci n'est pas une page."
- Implement this configuration via a Bash script.

## Task 5: Install Nginx Web Server with Puppet

**Objective:** Install and configure the Nginx web server using Puppet.

**Requirements:**
- Install Nginx on port 80.
- Ensure a GET request to the root ("/") returns a page with the string "Hello World!"
- Implement a 301 redirection for "/redirect_me" using Puppet resources.

---

Each task has specific requirements and objectives to be met. Ensure that your configurations adhere to these requirements, and you can automate the setup using the provided scripts.

