#!/bin/bash
git add .
git commit -m "status: $(ls -aRl | grep .py | wc -l)/$1"
git push
cp .vimrc  ~/.vimrc
