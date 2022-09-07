#!/bin/bash

sshpass -p $2 ssh  $3@$1 "echo "$2"|sudo -S shutdown -r now"