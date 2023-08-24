# Simple Web Stack

![Image of a simple web stack](0-simple_web_stack.jpg)


## Description

This is a basic web server hosting a website that can be accessed by typing "www.foobar.com" into the address bar. The network of the server is not secured by firewalls or SSL certificates. The resources (CPU, RAM, and SSD) offered by the server (database, application server) must be shared by all components.

## Specifics About This Infrastructure

+ What a server is.<br/> A server is a powerful computer or system that delivers services, resources, or data to other computers known as clients across a network. Servers are meant to manage and process client requests, as well as to deliver the desired content or services.



+ The role of the domain name.<br/>
A domain name is a human-readable address that points to a certain IP address. It is used to find and access online resources such as websites. When opposed to IP addresses, domain names make it easier for people to remember and access websites. For example, the domain name `www.google.com` is easier to recognize and remember than `172.217.15.110`

+ The type of DNS record `www` is in `www.foobar.com`.<br/>The most common type of DNS record used for the "www" subdomain is a "CNAME" record, which stands for Canonical Name. In the context of "www.foobar.com," a CNAME record for the "www" subdomain would typically point to the main domain, "foobar.com."


+ The role of the web server.<br/>
A domain name is a human-readable address that refers to an IP address. It's used to find and access internet resources like websites. It accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.

+ The role of the application server.<br/>
The web application's business logic is executed by the application server. It handles dynamic requests, communicates with databases, and creates dynamic content based on user input. It exchanges data with the web server in order to fulfill user requests.

+ The role of the database.<br/>The database stores and maintains structured data for the application. It is used to save user data, content, configurations, and other information. The application server communicates with the database to read and write data, allowing the application to access and update information.


+ What is the server using to communicate with the computer of the user requesting the website.<br/>The TCP/IP protocol suite is used to communicate between the client and the server across the internet network.
When a user requests a website, the server communicates with the user's computer using the Hypertext Transfer Protocol (HTTP) or its secure version, HTTPS. HTTP and HTTPS are application-layer protocols that define how data is exchanged between a web server and a client (such as a web browser) over the internet.


## Issues With This Infrastructure

+ There are multiple SPOF (Single Point Of Failure) in this infrastructure.<br/>If any crucial part of the infrastructure as stated breaks, such as the sole web server, the entire application could go offline. Implementing redundancy techniques like load balancing and server clusters will help to reduce this.
For example, Consider a web application that sends user conversations, password resets, and vital notifications via email. The ability of the entire program to send important emails could be jeopardized if the email provider encounters a single point of failure, such as outage or technical problems.

+ Downtime when maintenance needed.<br/>The server must be shut down or any component shut down when we need to do maintenance checks on it. There is just one server, thus there would be a downtime on the website.

+ Cannot scale if there's too much incoming traffic.<br/>
A rapid flood of inbound traffic may strain the infrastructure. To distribute the load and ensure that the application can accommodate growing user demand, scaling methods such as adding more web servers and database replication must be introduced.

