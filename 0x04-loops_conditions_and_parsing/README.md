This README file contains descriptions for the 0x04-loops_conditions_and_parsing tasks

The Bash script files in this category demonstrate the use of loops, conditions, and parsing in shell scripting. The scripts cover a variety of settings and conditions to demonstrate various control structures and parsing strategies.

#Tasks


To provide descriptions of all the files in the 0x04-loops_conditions_and_parsing task, we need to list each file and briefly explain its purpose. Below is a description of each file that should be included in the README.md file:

0x04-loops_conditions_and_parsing
This directory contains Bash script files that demonstrate the usage of loops, conditions, and parsing in shell scripting. The scripts cover various scenarios and conditions to showcase different control structures and parsing techniques.

Files:
0-RSA_public_key.pub

Description: This file contains the RSA public key generated for SSH access to remote servers. It should be added to the user's intranet profile for server access.
1-for_best_school

Description: This script uses a for loop to display the text "Best School" ten times on separate lines.
2-while_best_school

Description: This script uses a while loop to display the text "Best School" ten times on separate lines.
4-if_9_say_hi

Description: This script uses an if statement to display "Best School" ten times and adds "Hi" on a new line for the 9th iteration.
5-4_bad_luck_8_is_your_chance

Description: This script uses if, elif, and else statements to display different messages for the 4th, 8th, and other loop iterations.
school_info.sh

Description: This script checks the existence and properties of a file named "school" and provides relevant information, adhering to the specified requirements.
print_file_names.sh

Description: This script lists the content of the current directory in a list format, displaying only the part of the name after the first dash for each file.
time_display.sh

Description: This script displays the time for 12 hours and 59 minutes using a while loop to print hours from 0 to 12 and minutes from 1 to 59.


# Advanced Tasks

#100-read_and_cut
File: 100-read_and_cut

Description: This Bash script reads and displays the content of the file /etc/passwd using the while loop and cut command. It extracts and displays the following information for each user entry:

username
user id
Home directory path for the user
The script processes the lines in the /etc/passwd file, extracts the required fields using the cut command, and presents the information in the format "username:user id:Home directory path for the user".

#101-tell_the_story_of_passwd
File: 101-tell_the_story_of_passwd

Description: This Bash script reads and displays the content of the file /etc/passwd using the while loop and IFS (Internal Field Separator). It interprets the information from the file and creates a descriptive story for each user entry in the /etc/passwd file.

#102-lets_parse_apache_logs
File: 102-lets_parse_apache_logs

Description: This Bash script performs a simple parsing of Apache log access files to gather data about website traffic. It extracts the visitor's IP address and the corresponding HTTP status code from the Apache log file. The output is displayed in a list format, showing the IP address followed by the HTTP status code, with each entry on a separate line.

#103-dig_the-data
File: 103-dig_the-data

Description: This Bash script parses the Apache log file to group visitors by IP and HTTP status code, and then displays this data in a sorted format. The script uses awk to process the log file and extract the required information.
