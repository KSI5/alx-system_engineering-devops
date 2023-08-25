##Description
This infrastructure comprises three servers, designed to ensure security, monitoring, and encrypted traffic for web services.

# Secured and Monitored Web Infrastructure

![Image of a secured and monitored infrastructure](2-secured_and_monitored_web_infrastructure.jpg)


**Firewalls (x3):**<br/>
 These were added to improve security by filtering and keeping track of incoming and outgoing traffic. wards off any dangers and unwanted entry.

Protects sensitive data from being intercepted or altered with an SSL certificate for HTTPS, ensuring safe and encrypted communication between users and the website.

Data gatherers for monitoring services like Sumo Logic are referred to as monitoring clients (x3). Keep an eye on the server's performance, resource usage, and any potential problems.

**What are firewalls for?**<br/>
Firewalls are used to safeguard and manage network traffic, block unauthorized entry, and defend against online dangers.

**Why is the traffic served over HTTPS?**<br/>
 Data integrity is maintained during transit thanks to HTTPS, which guarantees secured data transmission.

**What monitoring is used for:**<br/>
Monitoring is essential to check system health, spot performance hiccups, and resolve possible problems before they have an impact on consumers.

**How the monitoring tool is collecting data:**<br/>
Performance and log data are collected and sent to monitoring services via monitoring clients. For insights, this data is processed and analyzed by Sumo Logic or other services.

**Explain what to do if you want to monitor your web server QPS:**<br/>
Configure metrics collection for request counts and response timings to track web server queries per second (QPS). To determine server load and user experience, analyze these metrics.


## Issues with the Infrastructure:

+ Terminating SSL at Load Balancer Level: Terminating SSL at the load balancer can expose sensitive data between the load balancer and the application server. End-to-end encryption is preferable.

+ Single MySQL Server for Writes: Relying on a single MySQL server for writes creates a single point of failure. Redundancy and failover mechanisms should be in place.

+ Uniform Component Configuration: Using identical configurations for all servers might not be optimal for different roles. Tailor configurations for specific server functions to avoid resource wastage.
