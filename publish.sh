#!/bin/bash
cd ~/Documents/fedgg.github.io
git pull
git add .
git commit -m "Updated notes - $(date)"
git push
