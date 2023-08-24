# Distributed Web Infrastructure

![Image of a distributed web infrastructure](1-distributed_web_infrastructure.jpg)

## Description

This distributed web infrastructure dynamically splits incoming traffic between two servers—a primary server and a replica server—to maximize performance and dependability. To effectively distribute the workload among multiple servers and guarantee that the primary server is not overworked, a dedicated load balancer is used. This method offers a smooth user experience while improving the scalability and robustness of the infrastructure. 

##Specifics About This Infrastructure

**Distribution Algorithm of the Load Balancer and How It Works:**<br/>
The HAProxy load balancer employs the Round Robin distribution algorithm. This algorithm cycles through each server behind the load balancer in a sequential order based on their weights. Round Robin ensures an equitable distribution of processing load, and it remains one of the most impartial algorithms. It accommodates dynamic adjustments to server weights as needed.

**Setup Enabled by the Load-Balancer:**<br/>
The HAProxy load balancer facilitates an Active-Passive setup. In an Active-Passive configuration, not all nodes are concurrently active in receiving workloads. For instance, with two nodes, if the first is active, the second remains passive or on standby. The next passive node becomes active when the preceding node is inactive. This approach ensures failover capability and effective resource utilization.

**How a Database Primary-Replica (Master-Slave) Cluster Operates:**<br/>
A Primary-Replica setup designates one server as the Primary, responsible for both read and write requests. The other server acts as a Replica of the Primary. However, the Replica server is limited to handling read requests exclusively. Data synchronization between the Primary and Replica servers occurs whenever a write operation is executed on the Primary server.

**Difference Between the Primary Node and the Replica Node in Regards to the Application:**<br/>
The Primary node handles all write operations required by the website. It manages data updates and modifications. In contrast, the Replica node specializes in processing read operations. By delegating read requests to the Replica node, the Primary node's workload is lightened, which helps optimize the site's performance and responsiveness.
