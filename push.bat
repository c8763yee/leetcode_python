@echo off
REM Add all changes to git
git add .

REM Get total solved problems from the API
for /f %%i in ('curl https://leetcode-stats-api.herokuapp.com/c8763yee ^| jq ".totalSolved"') do set totalSolved=%%i

REM Count number of .py files and commit
for /f %%i in ('dir /s /b *.py ^| find /c /v ""') do set pyCount=%%i
git commit -m "status: %pyCount%/%totalSolved%"

REM Push changes to the repository
git push

REM Copy .vimrc file to home directory
copy .vimrc %HOMEPATH%\.vimrc
