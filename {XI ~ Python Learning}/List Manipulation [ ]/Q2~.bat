:x 
@echo off  
set /a col=(%RANDOM%*10/32768)+0 
color %col%
echo. 
echo. 
py Q2~.py 
echo. 
echo. 
pause 
cls  
goto x  