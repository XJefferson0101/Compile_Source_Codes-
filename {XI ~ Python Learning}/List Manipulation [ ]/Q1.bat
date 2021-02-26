:x 
@echo off  
set /a col=(%RANDOM%*10/32768)+0 
color %col%
echo. 
echo. 
py Q1~.py 
echo. 
echo. 
pause 
cls  
goto x  