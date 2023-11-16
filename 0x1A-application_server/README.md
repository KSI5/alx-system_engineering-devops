# 0x1A-application_server

### Table of Contents
1. [Task 0: Set up development with Python](#task-0-set-up-development-with-python)
2. [Task 1: Set up production with Gunicorn](#task-1-set-up-production-with-gunicorn)
3. [Task 2: Serve a page with Nginx](#task-2-serve-a-page-with-nginx)
4. [Task 3: Add a route with query parameters](#task-3-add-a-route-with-query-parameters)
5. [Task 4: Let's do this for your API](#task-4-lets-do-this-for-your-api)
6. [Task 5: Serve your AirBnB clone](#task-5-serve-your-airbnb-clone)
7. [Task 6: Deploy it!](#task-6-deploy-it)
8. [Task 7: No service interruption](#task-7-no-service-interruption)

---

### Task 0: Set up development with Python
📄 **File:** README.md  
📝 **Description:** Set up the development environment for the application server with Python. This involves installing Python 3 and creating a virtual environment to manage dependencies.

---

### Task 1: Set up production with Gunicorn
📄 **File:** 0x1A-application_server  
📝 **Description:** Configure the production environment for the application server using Gunicorn. Install Gunicorn and set up the necessary configurations to run the Flask app in a production-ready manner.

---

### Task 2: Serve a page with Nginx
📄 **File:** 2-app_server-nginx_config  
📝 **Description:** Configure Nginx to serve a page by setting up the necessary Nginx configuration files. Ensure that Nginx is properly set up to handle HTTP requests.

---

### Task 3: Add a route with query parameters
📄 **File:** 3-app_server-nginx_config  
📝 **Description:** Enhance the Nginx configuration to handle routes with query parameters. Modify the Nginx configuration files to include support for query parameters in the URLs.

---

### Task 4: Let's do this for your API
📄 **File:** 4-app_server-nginx_config  
📝 **Description:** Extend the Nginx configuration to support routing for an API. Ensure that Nginx is configured to handle API requests and route them to the appropriate backend.

---

### Task 5: Serve your AirBnB clone
📄 **File:** 5-app_server-nginx_config  
📝 **Description:** Serve the AirBnB clone application using the configured application server. Verify that the Flask application is accessible over HTTP and that requests are correctly handled by Gunicorn through the Nginx reverse proxy.

---

### Task 6: Deploy it!
📄 **File:** gunicorn.service  
📝 **Description:** Deploy the application server using Gunicorn as a systemd service. Create a systemd script to start Gunicorn with specified configurations, allowing the server to run automatically upon system boot.

---

### Task 7: No service interruption
📄 **File:** 4-reload_gunicorn_no_downtime  
📝 **Description:** Implement a Bash script to reload Gunicorn gracefully, ensuring there is no downtime during updates. The script should restart Gunicorn workers without interrupting the service.

