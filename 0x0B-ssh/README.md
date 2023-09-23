# System Engineering & DevOps - 0x0B-ssh

This repository contains my solutions to the System Engineering & DevOps tasks for the Bash scripting project.

## Table of Contents ✏️

| Task                                 | Description                                                    |
| ------------------------------------ | -------------------------------------------------------------- |
| [0. Use a private key](#0-use-a-private-key) | Write a Bash script to connect to a server using an SSH private key. |
| [1. Create an SSH key pair](#1-create-an-ssh-key-pair) | Write a Bash script to create an RSA key pair with a passphrase. |
| [2. Client configuration file](#2-client-configuration-file) | Configure SSH client to use a private key and refuse password authentication. |
| [3. Client configuration file (w/ Puppet)] (#100-puppet_ssh_config.pp) | Configure SSH client settings on the target system. |

## Tasks 📖

### 0. Use a private key

Write a Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

### 1. Create an SSH key pair

Write a Bash script that creates an RSA key pair. The name of the created private key must be `school`, and the key must be protected by the passphrase `betty`.

### 2. Client configuration file

Configure your SSH client to use the private key `~/.ssh/school` and refuse password authentication.

## Advanced Task 💪

## 100-puppet_ssh_config.pp

This Puppet manifest file (`100-puppet_ssh_config.pp`) is part of the System Engineering & DevOps project for configuring SSH client settings.

### Description

The purpose of this Puppet manifest is to configure SSH client settings on the target system. It ensures that the SSH client is properly configured to use the private key `~/.ssh/school` and refuse password authentication.

### Usage

To apply this Puppet manifest and configure the SSH client on your system, you can use the `puppet apply` command:


## Author

* [Kriss Igebu](https://github.com/KSI5)


