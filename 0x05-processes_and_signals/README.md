This README file contains descriptions for the 0x05-processes_and_signals0x05-processes_and_signals tasks.

0-what-is-my-pid
Description:
A Bash script that displays its own PID.

1-list_your_processes
Description:
A Bash script that displays a list of currently running processes. It shows all processes for all users, including those which might not have a TTY, and displays the process hierarchy.

2-show_your_bash_pid
Description:
A Bash script that displays lines containing the word "bash" from the process list, allowing you to easily get the PID of your Bash process. It cannot use the pgrep command and includes a shellcheck disable comment for a specific error.

3-show_your_bash_pid_made_easy
Description:
A Bash script that displays the PID, along with the process name, of processes whose name contains the word "bash". It cannot use the ps command.

4-to_infinity_and_beyond
Description:
A Bash script that displays "To infinity and beyond" indefinitely with a 2-second sleep in between each iteration.

5-kill_me_now
Description:
A Bash script that kills the 4-to_infinity_and_beyond process.

6-stop_me_if_you_can
Description:
A Bash script that displays "To infinity and beyond" indefinitely with a 2-second sleep in between each iteration. When the script receives a SIGTERM signal (usually sent by pressing Ctrl+C), it will display "I am invincible!!!" before terminating.

7-highlander
Description:
A Bash script that displays "I am invincible!!!" indefinitely with a 2-second sleep in between each iteration. This script is designed to be used as a background process and can be terminated using the 67-stop_me_if_you_can script.

8-beheaded_process
Description:
A Bash script that kills the process named "7-highlander".

