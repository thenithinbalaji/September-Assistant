+ Thank you for installing September.
+ This is an open-source voice assistant. You can view its source code here                   
[https://github.com/thenithinbalaji/September-Assistant](https://github.com/thenithinbalaji/September-Assistant)

# Read & Follow these before using September 

<p align = "center">
  <img alt = "september load page" src = "https://user-images.githubusercontent.com/73932121/154336929-d42a9d0e-e346-472c-8231-77a87c4fac59.png">
</p>

## ⚙️ Setting up the application (Must Read, Don't Skip these)

  + [The Basic Question Answering Ability will break if you skip this step](README.md#the-basic-question-answering-ability-will-break-if-you-skip-this-step)   
  + [September won't be able to open apps and browsers if you skip this step](README.md#september-wont-be-able-to-open-apps-and-browsers-if-you-skip-this-step)        
  + [Additional Debugging](README.md#additional-debugging)      

## 🖥️ Keybinds

| Key         | Functionality |    
| ----------- | -----------   |     
| Escape      | Stops the assistant from speaking the current dialogue|     
| Enter       | Reads the input from the command entry box. <br> (Works only when the command entry box is focussed)|
| Alt + F4    | Quits the application |


## 🎙️ Wake word 

+ You can make September respond to a custom wake word. 
+ By default, the wake word is `September`
+ You can change it in the settings. 
![settings](https://user-images.githubusercontent.com/73932121/154291061-500874be-1a2f-4d76-9e75-98239170ad1f.png)

## 💾 Recommended Configuration

+ Windows 10
+ 1080p resolution
+ RAM >1GB
+ **Note:** These are just recommended requirements. Your PC might still support September without these.

## 😎 Cool Things to Try
```
open notepad
```
```
search for stock market crash on google
```
```
play gangnam style 
```
```
flip a coin
```
```
repeat rage, rage against the dying of the light!
```
```
photosynthesis from wikipedia
```
```
what is the lifespan of a housefly
```

## 📝 License
MIT License

Copyright (c) 2022 Nithin Balaji

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

----------------------

## The Basic Question Answering Ability will break if you skip this step

+ This app depends on Wolfram Alpha - a computational knowledge engine and answer engine developed by Wolfram Research.
+ The app comes with a default sample API key which is required for the Wolfram Alpha engine to function. This will become **outdated** after some time. 
+ To keep September working, you are required to generate your API key and update it in the app settings.
+ Note: Features like opening apps, searching web, playing from youtube etc. doesn't require the usage of this API.

### Steps to create and enter the new API key

+ Create an account at [https://account.wolfram.com/login/create](https://account.wolfram.com/login/create)
![create account](https://user-images.githubusercontent.com/73932121/154290158-ae1c80b6-b7d9-4e04-9c99-ca80cad29352.png)
+ After creating the account, verify your mail-id. Check your inbox and spam folder. 
+ After verifying your mail id, go to https://developer.wolframalpha.com/portal/myapps. Click on the **Sign up to get your first AppID** button and fill it out. 
![developer portal](https://user-images.githubusercontent.com/73932121/154291516-7f78a34e-a925-4dca-8cc1-6d6ce012d305.png)

+ Click get a **New AppID** dialog after that. You will then be presented with an API key

<p align = "center">
  <img alt = "appid created" src = "https://user-images.githubusercontent.com/73932121/154291042-7668fd00-036c-4fc8-b611-f954091ff93e.png">
</p>

+ Copy that API key. The key in the above image is a sample API key. Do not use that value.   
+ Go to September app settings to update the WOLFAPI KEY value.
![settings](https://user-images.githubusercontent.com/73932121/154291061-500874be-1a2f-4d76-9e75-98239170ad1f.png)
+ Select **WOLFAPI KEY** in the settings dropdown menu and      
  enter your copied app id in the **ENTER NEW VALUE BOX** and click update.

<p align = "center">
  <img alt = "api key in settings" src = "https://user-images.githubusercontent.com/73932121/154312014-4e5cc2c9-2569-4b62-ab08-abf59545400a.png">
</p>

### When to change my API key again

+ You can track your API status at [https://developer.wolframalpha.com/portal/myapps](https://developer.wolframalpha.com/portal/myapps)
+ Once you cross 2K monthly requests, you need to create a new API key and update it in the settings.
+ You need not change your API key if your monthly usage is less than 2K requests.   
+ Note: Features like opening apps, searching web, playing from youtube etc. doesn't require the usage of this API.

<br>

## September won't be able to open apps and browsers if you skip this step

+ You can command September to open some default apps, chrome & edge browsers, and even search Google, Youtube, and Wikipedia.
+ For this to work properly, you need to go to settings and ensure that the app paths are correct. (The default app paths will work in most of the systems)  
+ You can change those paths by entering a new value and clicking update in settings.
![settings](https://user-images.githubusercontent.com/73932121/154291061-500874be-1a2f-4d76-9e75-98239170ad1f.png)

## Additional Debugging
+ Sometimes the antivirus software may hinder September from uploading & downloading audio stream data or listening to the microphone. Make sure you trust the application in your antivirus software settings if the voice detection doesn't work.
+ Requires active internet connection to function.   
+ Make sure that your mic and speaker are in proper working condition. 
