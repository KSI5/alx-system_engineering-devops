# 0x10-https_ssl


❶ Task: 0-world_wide_web

🎯 **Objective:** Set up the World Wide Web with your web application.

📋 **Instructions:**

1. Install and configure a web server (e.g., Apache, Nginx) on your server.
2. Ensure it listens on port 80.
3. Place your web application files in the appropriate directory.
4. Test your web server by accessing it via your server's IP address or domain name.

🔗 **Related Files:** None

---
❸ Task: 1-haproxy_ssl_termination

🎯  **Objective:** Configure HAProxy to terminate SSL and serve encrypted traffic for your web application.

📋  **Requirements:**

1. HAProxy must be listening on port TCP 443.
2. HAProxy must be configured to accept SSL traffic.
3. HAProxy must serve encrypted traffic that will return the root page of your web server.
4. When querying the root of your domain name, the page returned must contain "Holberton School."
5. Share your HAProxy config as an answer file (`/etc/haproxy/haproxy.cfg`).
6. The file `1-haproxy_ssl_termination` must be your HAProxy configuration file.

🔗  **Steps:**

1. Install HAProxy 1.5 or higher on your server using your operating system's package manager (e.g., `apt-get`).
2. Install Certbot to obtain SSL certificates for your subdomain.
3. Use Certbot to obtain an SSL certificate for your subdomain.
4. Create or edit the HAProxy configuration file `/etc/haproxy/haproxy.cfg` with the provided configuration, replacing `your_domain.pem` with your actual SSL certificate file.
5. Restart HAProxy to apply the changes.
6. Ensure your web server serves content with "Holberton School" when accessing the root of your domain.

📂  **Files:** [1-haproxy_ssl_termination](path/to/your/1-haproxy_ssl_termination)

❷ Task: 100-redirect_http_to_https

🎯 **Objective:** Enforce HTTPS traffic by configuring HAProxy to automatically redirect HTTP traffic to HTTPS.

📋 **Requirements:**

1. This redirection should be transparent to the user.
2. HAProxy should return a 301 status code.
3. HAProxy should redirect HTTP traffic to HTTPS.
4. Share your HAProxy config as an answer file (`/etc/haproxy/haproxy.cfg`).
5. The file `100-redirect_http_to_https` must be your HAProxy configuration file.

🔗 **Steps:**

1. Modify your existing HAProxy configuration file to include HTTP to HTTPS redirection.
2. Save the updated configuration as "100-redirect_http_to_https" in the appropriate directory (/etc/haproxy/).
3. Restart HAProxy to apply the changes.
4. Test that HTTP requests are automatically redirected to HTTPS without user intervention.

📂 **Files:** [100-redirect_http_to_https](path/to/your/100-redirect_http_to_https)

---



