#!/bin/bash

plink -pw '[password]' [username]@$1 "echo "[password]"| sudo -S shutdown -r now"