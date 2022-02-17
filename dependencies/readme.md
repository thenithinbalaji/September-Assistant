# Dependencies
+ [requirements.txt](../requirements.txt) contains all the python modules required by the program.
+ All the assets used by the program are present in [assets folder](../assets). The application won't function as intended without these assets.
+ Built in Python 3.10.1. Use python 3.0 or greater versions for better experience. 
+ Requires active internet connection. 
+ Make sure that your antivirus doesn't block the program from uploading or dowloading audio stream data. (Disable antivirus :D)
+ Additionally, the `Pyaudio` module must be installed by following the below instructions. 

### Install Pyaudio
+ Find your Python version using `python --version`
+ Find the appropriate `.whl` (wheel) file from [Pythonlibs](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and download it.
+ Go to the folder where it is downloaded and install the `.whl` file using pip, 
For example `pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl`
+ The wheel file for Python 3.10 64-bit is present in [dependencies/PyAudio-0.2.11-cp310-cp310-win_amd64.whl](PyAudio-0.2.11-cp310-cp310-win_amd64.whl)
+ [Visit for more information](https://stackoverflow.com/a/55630212)