This README file will describe what each script in this project is doing.
0-hello_world: The script echo "Hello, World" will print “Hello, World”, followed by a new line to the standard output.
1-confused_smiley: The command echo "\"(Ôo)'" will display a confused smiley.
2-hellofile: The command cat /etc/passwd will display the content of the /etc/passwd file.
3-twofiles: The command cat /etc/passwd /etc/hosts will display both the content of /etc/passwd and /etc/hosts
4-lastlines: The command tail -n 10 /etc/passwd will display the last 10 lines of /etc/passwd.
5-firstlines: The command head -n 10 /etc/passwd will display the first 10 lines of /etc/passwd.
6-third_line: The commamnd head -n 3 iacta | tail -n 1 will displays the third line of the file iacta.
7-file: The command echo "Best School" > '*\\\'"Best School"\'\\\\*\$\\?\*\*\*\*\*:)' will creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
8-cwd_state: The command ls -la > ls_cwd_content will write into the file ls_cwd_content the result of the command ls -la.
9-duplicate_last_line: This command tail -n 1 iacta >> iacta will duplicates the last line of the file iacta.
10-no_more_js: This command find . -type f -name "*.js" -delete will delete all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
11-directories: This command  find . -type d -not -name '.' | wc - l will count the directories and sub-directories in the current directory.
12-newest_files: This command ls -t1 | head -n 10 will display the 10 newest files in the current directory. 
13-unique: This command sort | uniq -c creates a script that takes a list of words as input and prints only words that appear exactly once. 
14-findthatword: This command grep "root" /etc/passwd will display lines containing the pattern “root” from the file /etc/passwd.
15-countthatword: The command grep -c "bin" /etc/passwd displays the number of lines that contain the pattern “bin” in the file /etc/passwd
16-whatsnext: This command grep -A 3 "root" /etc/passwd displays lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
17-hidethisword: The command grep -v "bin" /etc/passwd displays all the lines in the file /etc/passwd that do not contain the pattern “bin”. 
18-letteronly: The command grep -i '^[a-z]' /etc/ssh/sshd_config displays all lines of the file /etc/ssh/sshd_config starting with a letter. Capital letters inclusive.
19-AZ: The command tr 'Ac' 'Ze' will replace all characters A and c from input to Z and e respectively.
20-hiago: The command tr -d 'cC' create a script that removes all letters c and C from input. 
21-reverse: The command rev reverses its input.
22-users_and_homes: The command cut -d ':' -f 1,6 /etc/passwd | sort wiil write a script that displays all users and their home directories, sorted by users.
100-empty_casks: This command find . -empty | rev | cut -d '/' -f 1 | rev will write a command that finds all empty files and directories in the current directory and all sub-directories.
101-gifs: This command find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' 2- | rev | LC_ALL=C sort -f writes a script that lists all the files with a .gif extension in the current directory and all its sub-directories.  
102-acrostic: The command cut -c 1 | paste -s -d '' will create a script that decodes acrostics that use the first letter of each line.
103-the_biggest_fan: The command tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev will write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.


