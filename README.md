<h1 align = "center">September - Windows Assistant</h1>

September is an open-source Windows personal assistant built-in python. Read [SETUP.md](SETUP.md) for additional information on setting up the application. 

## 🔮 Features 

+ [x] Minimalistic UI
+ [x] Lightweight 
+ [x] Customizable Wake Word
+ [x] Type/Speak commands
+ [x] Search Wiki, Google and YouTube
+ [x] Open Windows Apps
+ [x] Mathematical Calculations 
+ [x] Human-like Conversations  

<p align = "center">
  <video src = "https://user-images.githubusercontent.com/73932121/154417750-2b43a0e7-2d89-44d6-8ad5-f0ebb3f32ad1.mp4">Sample Video</video>
</p>

## 📚 Overview

| September uses                                                       | For                      |
| -----------                                                          | -----------              |
| [Google Speech Recognition](https://cloud.google.com/speech-to-text) | Speech recognition       |
| [Pyttsx3](https://pypi.org/project/pyttsx3/)                         | Text to Speech           |
| [Tkinter](https://docs.python.org/3/library/tkinter.html)            | GUI                      |
| [Wikipedia API](https://pypi.org/project/wikipedia/)                 | Wiki related search      |
| [Wolfram Alpha](https://www.wolframalpha.com/)                       | Processing queries       |

## 💻 Code Walkthrough

+ [main.py](main.py) contains the functions for initializing Tkinter-based windows and converting speech to text.  
  + The listening process and tkinter frame refresh process run concurrently using threads.       
  + Each window is started as a separate thread for them to work parallelly.      
  + Start and Stop Listening sounds are played using the `playsound` module.
  + The input from the user is taken either as a text from the command entry box or as audio from mic button
  + The input is converted to text using `SpeechRecognition` module and passed to processtext function of [processtext.py](processtext.py)
  ![entry place](https://user-images.githubusercontent.com/73932121/154352815-6bc467bf-bc62-4409-bbac-210a00037a62.png)

+ [processtext.py](processtext.py) contains the function in which the command processing happens.       
  + The input obtained from the user in the main function is passed to the processtext function. It has an **if-else ladder** to search for specific **keywords** in the input. If the query does not match with the keywords found in the ladder, it is passed to [wolfresponse.py](wolfresponse.py)
  + Functions like opening apps, searching web happens here. 
    
+ [wikiresponse.py](wikiresponse.py) and [wolfresponse.py](wolfresponse.py) are the places where the respective APIs are accessed to process the output of the unmatched queries from [processtext.py](processtext.py)

+ [texttospeech.py](texttospeech.py) uses the `pyttsx3` module to convert speech to text. 
  + After processing the query, text to speech function is called.    
  + `Esc` Key is added as a keybind to stop text to speech for one iteration. 

+ [config_data.json](config_data.json) contains the values that are displayed in the September app settings in **JSON** format. It is used for storing windows application paths, wake word and the API key. 

+ [requirements.txt](requirements.txt) contains the list of all the modules used in this program. 

## 🌐 Dependencies

+ [requirements.txt](requirements.txt) contains all the python modules required by the program.
+ All the assets used by the program are present in [assets folder](assets). The application won't function as intended without these assets.
+ Built in Python 3.10.1. Use python 3.0 or greater versions for a better experience. 
+ Requires active internet connection. 
+ Make sure that your antivirus doesn't block the program from uploading or downloading audio stream data. (Disable antivirus :D)
+ Additionally, the `Pyaudio` module must be installed by following the below instructions. 

### Install Pyaudio

+ Find your Python version using in your terminal
```
python --version
```
+ Find the appropriate `.whl` (wheel) file at [Pythonlibs](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and download it.
+ Go to the folder where it is downloaded and install the `.whl` file using pip,        
For example, if you download the wheel file for Python 3.7 64-bit, your pip command would be,     
```
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```
+ The wheel file for Python 3.10 64-bit is present in [dependencies/PyAudio-0.2.11-cp310-cp310-win_amd64.whl](dependencies/PyAudio-0.2.11-cp310-cp310-win_amd64.whl)
+ [Visit for more information](https://stackoverflow.com/a/55630212)


## 📝 License
[MIT License Copyright (c) 2021 Nithin Balaji](LICENSE.md)


