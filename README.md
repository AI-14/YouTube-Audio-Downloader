# YouTube Audio Downloader
  
## Description
  YouTube Audio Downloader is an application that downloads a list of YouTube links in the best audio bitrate format available and stores it in the destination folder chosen by the user. It is designed primarily for downloading songs/OSTs from YouTube. 

## Screenshots Of The Application
![](screenshots/1.png)
![](screenshots/2.png)

## How To Create A .exe File?
Download this repository and create a virtual environment folder in the **cmd** using the command ````python -m venv venv````. Activate this venv using the command ````venv\Scripts\activate.bat```` and then install the following modules/packages:
````
pip install PyQt5
pip install pytube3
pip install typing-extensions
pip install cx-Freeze
````
>**Note:** ***venv** should be created in this repo.*

*Now follow these steps*

Step 1: Run the scripts to check if they are working properly.

Step 2: Create a new module **setup.py** and copy paste the following code (and save it in **src**):

````
import sys
from cx_Freeze import setup, Executable

setup(name='YouTube Audio Downloader',
      version='1.0',
      description='An application that downloads YouTube video in the best bitrate audio format available',
      executables=[Executable('mainUi_logic.py', base='Win32GUI')])
````

Step 3: Go to **venv->Lib->sit-packages** and copy paste all the packages in the **src** folder. This is because cx-Freeze module sometimes gives error if you do not do this step. 

Step 4: Go to **src** and open **cmd**. Type the following command:
````
python setup.py build
````
After this you will be able to see **build** folder in **src**. 

Step 5: Now in the **src** folder, go to **build->exe.win32-3.6** and you will be able to see **mainUi_logic.exe**.
Now you can click on this .exe file or create a shortcut and give it 
any name you want.

Final step: Enjoy the app! Now you can download songs from YouTube without going to online websites with soo many ads and popups. One click and you get all the songs.

>**Note:** *If you get any errors, then try looking at YouTube videos on how to use **cx_Freeze** module.*
