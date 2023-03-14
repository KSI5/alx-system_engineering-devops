This README file will describe what each script in this project is doing.


0-alias: The command alias ls='rm *' creates an alias for ls giving it a value of 'rm 
*'.
1-hello_you: The command echo echo "hello $USER" will print hello user, where user is the current Linux user.
2-path: The command export PATH=$PATH:/action will add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
3-paths: The command echo $PATH | tr ":" "\n" | wc -l creates a script that counts the number of directories in the PATH.
4-global_variables: The command printenv creates a script that lists environment variables.
5-local_variables: The set command creates a script that lists all local variables and environment variables, and functions.
6-create_local_variable: The command BEST="School" creates a script that creates a new local variable.
7-create_global_variable: The command export BEST="School" creates a script that creates a new global variable.
8-true_knowledge: The command echo $(( $TRUEKNOWLEDGE + 128 )) will write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
9-divide_and_rule: The command echo $(($POWER / $DIVIDE)) will write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
10-love_exponent_breath: The command echo $(($BREATH**$LOVE)) will write a script that displays the result of BREATH to the power LOVE.
11-binary_to_decimal: This command echo $((2#$BINARY)) will write a script that converts a number from base 2 to base 10.
12-combinations: The command eval echo {a..z}{a..z} | tr ' ' '\n' | grep -v "oo" will create a script that prints all possible combinations of two letters, except oo.
13-print_float: The command printf "%.2f\n" "$NUM" will write a script that prints a number with two decimal places, followed by a new line and the number will be stored in the environment variable NUM.
100-decimal_to_hexadecimal: The command printf "%x\n" "$DECIMAL" will write a script that converts a number from base 10 to base 16.
101-rot13: The command tr 'A-Za-z' 'N-ZA-Mn-za-m' will write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.
102-odd: The command paste - - | cut -d$'\t' -f1 will write a script that prints every other line from the input, starting with the first line.
103-water_and_stir: The command printf "%o\n" $(( $((5#$(echo $WATER | tr water 01234))) + $((5#$(echo $STIR | tr stir. 01234))) )) | tr 01234567 bestchol will write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
