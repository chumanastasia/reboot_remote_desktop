#!/bin/bash

sshpass -p '[password]' ssh -q  [username]@$1 "echo "password"|sudo -S shutdown -r now"