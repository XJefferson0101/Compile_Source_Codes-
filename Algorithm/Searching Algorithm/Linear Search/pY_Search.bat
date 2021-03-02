:x 
@echo off
set /a col=(%RANDOM%*10/32768)+0
color %col%
echo. 
py pY_Search.py
color %col%  
echo.
echo                  { Python: Press Any Key To Run The Searching Algorithm }
echo.
pause >nul 
cls 
goto x 