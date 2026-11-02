@echo off
setlocal
cd /d "%~dp0"

REM Query LeetCode's official GraphQL API before staging changes.
set "statusFile=%TEMP%\leetcode-push-status-%RANDOM%-%RANDOM%.txt"
python scripts\push_status.py > "%statusFile%"
if errorlevel 1 (
    del "%statusFile%"
    exit /b 1
)
set /p commitStatus=<"%statusFile%"
del "%statusFile%"
if not defined commitStatus exit /b 1

git add .
if errorlevel 1 exit /b 1
git diff --cached --quiet
if errorlevel 2 exit /b 1
if errorlevel 1 (
    git commit -m "status: %commitStatus%"
    if errorlevel 1 exit /b 1
)
git push
if errorlevel 1 exit /b 1
copy .vimrc "%USERPROFILE%\.vimrc"
