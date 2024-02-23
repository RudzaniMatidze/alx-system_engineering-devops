# 0x05-processes_and_signals

## TASKS

| Filename | Requirement |
| -------- | ----------- |
| <ul><li>0-what-is-my-pid</li></ul> | <ul><li>Bash script that displays its own PID.</li></ul> |
| <ul><li>1-list_your_processes</li></ul> | <ul><li>Bash script that displays a list of currently running processes.</li></ul> |
| <ul><li>2-show_your_bash_pid</li></ul> | <ul><li>Bash script that displays the PID, along with the process name, of processes whose name contain the word bash</li></ul> |
| <ul><li>3-show_your_bash_pid_made_easy</li></ul> | <ul><li>Bash script that displays the PID, along with the process name, of processes whose name contain the word baSH.</li></ul> |
| <ul><li>4-to_infinity_and_beyond</li></ul> | <ul><li>Bash script that displays To infinity and beyond indefinitely.</li></ul> |
| <ul><li>5-dont_stop_me_now</li></ul> | <ul><li>Bash script that stops 4-to_infinity_and_beyond process.</li></ul> |
| <ul><li>6-stop_me_if_you_can</li></ul> | <ul><li>Bash script that stops 4-to_infinity_and_beyond process.</li></ul> |
| <ul><li>7-highlander</li></ul> | Write a Bash script that displays:<ul><li>To infinity and beyond indefinitely</li><li>With a sleep 2 in between each iteration</li><li>I am invincible!!! when receiving a SIGTERM signal</li></ul> |
| <ul><li>8-beheaded_process</li></ul> | <ul><li>Bash script that kills the process 7-highlander.</li></ul> |
| <ul><li>100-process_and_pid_file</li></ul> | Write a Bash script that:<ul><li>Creates the file /var/run/myscript.pid containing its PID</li><li>Displays To infinity and beyond indefinitely</li><li>Displays I hate the kill command when receiving a SIGTERM signa</li><li>Displays Y U no love me?! when receiving a SIGINT signal</li><li>Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal</li></ul> |
| <ul><li>101-manage_my_process</li><li>manage_my_process</li></ul> | Write a manage_my_process Bash script that:<ul><li>Indefinitely writes I am alive! to the file /tmp/my_process</li></li>In between every I am alive! message, the program should pause for 2 seconds</li></ul> |
| <ul><li>102-zombie.c</li></ul> | <ul><li>C program that creates 5 zombie processes.</li></ul> |
