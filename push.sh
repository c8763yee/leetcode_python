#!/bin/bash
git add .
totalSolved="$(curl https://leetcode-stats-api.herokuapp.com/c8763yee | jq '.totalSolved')"
git commit -m "status: $(ls -aRl | grep .py | wc -l)/$totalSolved"
git push
cp .vimrc  ~/.vimrc
