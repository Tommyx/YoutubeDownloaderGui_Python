rmdir /s /Q dist

cd\

cd C:\Users\Thomas\eclipse-workspace\Experiments\youtube_downloader

c:\python27\python.exe setup.py py2exe

copy *.ui dist\
copy *.png dist\

rmdir /s /Q build 
pause