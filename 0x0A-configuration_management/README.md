# 0x0A-configuration_management 📖



## Description

**Task 1: Create a File Using Puppet**

**Requirements:**
- Use Puppet to create a file in the `/tmp` directory.
- The file path should be `/tmp/school`.
- Set the file permission to `0744`.
- Assign the file owner as `www-data`.
- Set the file group to `www-data`.
- Ensure the file contains the text "I love Puppet."

**Example:**
```shell
# Create the Puppet manifest and apply it
puppet apply 0-create_a_file.pp

# Verify that the file has been created with the correct permissions and content
ls -l /tmp/school
cat /tmp/school
```

**Task 2: Install Flask Version 2.1.0 Using Puppet**

**Requirements:**
- Use Puppet to install Flask version 2.1.0 using the `pip` package manager.
- After applying the Puppet manifest, verify that Flask 2.1.0 is installed.

**Example:**
```shell
# Apply the Puppet manifest to install Flask
puppet apply 1-install_a_package.pp

# Verify Flask installation
flask --version
```

**Task 3: Kill a Process Named "killmenow" Using Puppet**

**Requirements:**
- Create a Puppet manifest to terminate a process named "killmenow."
- Utilize the `exec` Puppet resource.
- Employ the `pkill` command to terminate the process.
- Verify if the process is running before attempting to terminate it.
- Confirm that the process is terminated when the Puppet manifest is applied.

**Example:**
```shell
# Start the "killmenow" process in one terminal
./killmenow

# Apply the Puppet manifest to kill the "killmenow" process in another terminal
puppet apply 2-execute_a_command.pp

# Verify that the "killmenow" process has been terminated
./killmenow
