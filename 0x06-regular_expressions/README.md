This file contains descriptions for the 0x06-regular_expressions tasks


#Descriptions for 0x06-regular_expressions directory


## 0-simply_match_school.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match the word "School". The script should output any occurrences of the word "School" in the input string.

Tsk: To match the word "School" in an input string, we can use the regular expression /School/. This will find any occurrence of the exact word "School" in the input

## 1-repetition_token_0.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match the given test cases. The regular expression should match any string that contains "h", followed by zero or one occurrences of "b", followed by "tn".

Task: To match strings that contain "h", followed by zero or one occurrences of "b", and ending with "tn", we can use the regular expression /hb?tn/. The ? denotes that the preceding character "b" is optional.

## 2-repetition_token_1.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match the given test cases. The regular expression should match any string that contains "h", followed by one or more occurrences of "b", followed by "tn".

Task: To match strings that contain "h", followed by one or more occurrences of "b", and ending with "tn", we can use the regular expression /hb+tn/. The + denotes that the preceding character "b" must occur at least once.

## 3-repetition_token_2.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match the given test cases. The regular expression should match any string that contains "h", followed by zero or more occurrences of "b", followed by "tn".

Task: To match strings that contain "h", followed by zero or more occurrences of "b", and ending with "tn", we can use the regular expression /hb*tn/. The * denotes that the preceding character "b" can occur any number of times, including zero.


## 4-repetition_token_3.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match the given test cases. The regular expression should match any string that contains "h", followed by one or more occurrences of "b", followed by "t" and "n" (in any order).

Task: To match strings that contain "h", followed by one or more occurrences of "b", followed by either "t" or "n" (in any order), we can use the regular expression /hb+t|n+t/. The | denotes an "or" condition.

## 5-beginning_and_end.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match the given test cases. The regular expression should match any string that starts with "h" and ends with "n", with any single character in between.

Task: To match strings that start with "h" and end with "n", with any single character in between, we can use the regular expression /h.n/. The . matches any single character.

## 6-phone_number.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match a 10-digit phone number. The script should output the phone number if it matches the pattern, otherwise, it should not output anything.

Task:
To match a 10-digit phone number, we can use the regular expression /^\d{10}$/. The ^ matches the start of the string, \d matches any digit, {10} specifies exactly 10 occurrences of the preceding character, and $ matches the end of the string.

## 7-OMG_WHY_ARE_YOU_SHOUTING.rb
Description:
Write a Ruby script that accepts one argument and uses a regular expression to match words that contain only capital letters. The script should output any matched words without duplicates.

Task: To match words that contain only capital letters, we can use the regular expression /[A-Z]+/. The [A-Z] matches any capital letter, and + denotes that the preceding character must occur at least once. To eliminate duplicates, we can use the uniq method in Ruby.

## 100-textme.rb
Description:
Write a Ruby script that accepts one argument (the path to a log file) and uses regular expressions to extract statistics from the log data. The script should output the sender, receiver, and flags for each transaction in the format: `[SENDER],[RECEIVER],[FLAGS]`.

To extract statistics from a log file, we can use regular expressions to match the required patterns. We can use capture groups to extract the sender, receiver, and flags. The regular expression may vary based on the log format, and the matched data can be output in the format [SENDER],[RECEIVER],[FLAGS].

