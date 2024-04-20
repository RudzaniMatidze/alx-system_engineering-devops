# 0x0B-ssh

## Tasks

| Task | Requirements |
| ---- | ------------ |
| 0-use_a_private_key | Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.<ul><li>Only use ssh single-character flags</li><li>You cannot use -l</li><li>You do not need to handle the case of a private key protected by a passphrase</li></ul> |
| 1-create_ssh_key_pair | Write a Bash script that creates an RSA key pair.<ul><li>Name of the created private key must be school</li><li>Number of bits in the created key to be created 4096</li><li>The created key must be protected by the passphrase betty</li></ul> |
| 2-ssh_config | Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.<ul><li>Your SSH client configuration must be configured to use the private key ~/.ssh/school</li><li>Your SSH client configuration must be configured to refuse to authenticate using a password</li></ul> |
| 0x0B-ssh | Now that you have successfully connected to your server, we would also like to join the party.<ul><li>Add the SSH public key below to your server so that we can connect using the ubuntu user.</li></ul> |
