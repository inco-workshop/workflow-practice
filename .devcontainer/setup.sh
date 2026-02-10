#!/usr/bin/env bash

# Customise the terminal command prompt
printf "export PS1='\\[\\e[3;36m\\]\${PWD#/workspaces/} ->\\[\\e[0m\\] '\n" >> $HOME/.bashrc
export PS1='\[\e[3;36m\]${PWD#/workspaces/} ->\[\e[0m\] '

# Install vim
apt-get update && apt-get install -y vim && apt-get clean && rm -rf /var/lib/apt/lists/*

# Update Nextflow
nextflow self-update
nextflow -version

cat /usr/local/etc/vscode-dev-containers/first-run-notice.txt
