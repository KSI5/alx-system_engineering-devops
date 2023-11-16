# 0x1B-web_stack_debugging_4


## Task 0: [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp)
- 📝 **Description**: This Puppet manifest 🏗️ addresses a web stack debugging issue. It is responsible for modifying the system's limits to ensure that the web server (Nginx, in this case) can handle more simultaneous connections by increasing the file descriptor limit. The task involves modifying the `/etc/default/nginx` configuration file to change the `ULIMIT` value from its default to a higher value. Once the file is modified, the Nginx service is restarted to apply the new configuration.

## Task 1: [1-user_limit.pp](./1-user_limit.pp)
- 📝 **Description**: This Puppet manifest 🏗️ is part of a web stack debugging task and focuses on adjusting user-specific limits. It increases the user-level open file descriptor limit to improve the web server's ability to handle connections effectively. The task involves modifying a specific user's resource limits, ensuring they have enough file descriptors available. In this case, the user's limit is increased to a specified value to optimize web server performance.

These tasks aim to enhance the web server's performance by addressing limits and resource constraints, which can be critical for handling a high volume of web traffic. The modifications help ensure that the web server can efficiently serve its purpose without running into issues related to file descriptor limits. 🚀👷‍♂️
