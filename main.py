################################################### modules
from msilib import text
from winsound import PlaySound
from texttospeech import *
from processtext import *
from threading import *
import speech_recognition as sr
from playsound import playsound
from tkinter import *
import sys

# for settings
from cgitb import text
from ctypes import windll
from tkinter import *
from tkinter import ttk
from soupsieve import select
from tkinter import messagebox
import json

################################################### modules
infi_listen_bool = True
##############################################################settings window
def settings_window():

    # loading config_data into data dict
    file = open("config_data.json", "r")
    data = json.loads(file.read())
    file.close()

    # initial value for option selected in drop down
    dropdownstring = None

    # filling drop down menu using data dict by returning a tuple
    def fill_drop_down():
        values = ()
        for i in data.keys():
            values = values + (i,)
        return values

    # fetching drop down menu's selected option and returning it to current value box
    def option_selected(event):
        nonlocal dropdownstring
        dropdownstring = s.get()
        enternewvaluebox.delete("1.0", "end")
        insert_current_value(dropdownstring)

    # displaying cuurent values of selected option in dropdown menu
    def insert_current_value(key):
        currentvaluebox.configure(state="normal")
        currentvaluebox.delete("1.0", "end")
        currentvaluebox.insert("end", data[key])
        currentvaluebox.configure(state="disabled")

    # when update button is pressed
    def update_pressed():
        nonlocal dropdownstring

        if dropdownstring != None:
            key = dropdownstring
            newval = enternewvaluebox.get("1.0", END).strip()

            if len(newval) > 0:
                # updating data dict
                data[key] = newval

                # dumping data dict to config_data.json
                newdata = json.dumps(data)
                file = open("config_data.json", "w")
                file.write(newdata)
                file.close()

                # showing success message, changing current value
                messagebox.showinfo(
                    "", f"{key} has been successfully updated to \n{newval}"
                )
                insert_current_value(key)
                enternewvaluebox.delete("1.0", "end")

            else:
                messagebox.showwarning("", f"{key} can't be empty")

    #

    ################ window and combobox string declaration, window styling
    window = Toplevel()
    s = StringVar()
    window.geometry("500x500")
    window.maxsize(500, 500)
    window.title("SETTINGS")
    window.configure(bg="white")
    window.option_add("*font", "Segoe_UI 10")
    window.iconbitmap("assets\settings_icon.ico")
    window.attributes("-topmost", True)
    ################ window and combobox string declaration, window styling

    #

    #####################################################name frame
    nameframe = Frame(window)
    Label(nameframe, text="NAME : ", bg="white", width=25).pack(side=LEFT)

    combobox = ttk.Combobox(nameframe, width=30, textvariable=s)
    combobox.pack(side=RIGHT)

    combobox["state"] = "readonly"
    combobox.current(None)

    # filling data dict values
    combobox["values"] = fill_drop_down()

    # when an option is selected
    combobox.bind("<<ComboboxSelected>>", option_selected)

    nameframe.pack(pady=(50, 0))
    #####################################################name frame

    #

    #####################################################current value frame
    currentvalueframe = Frame(window)
    currentvalueframe.configure(bg="white")

    Label(currentvalueframe, text="CURRENT VALUE : ", bg="white", width=25).pack(
        side=LEFT
    )

    currentvaluebox = Text(currentvalueframe, bg="white", width=33, height=5, wrap=WORD)
    currentvaluebox.pack(side=RIGHT)
    currentvaluebox.configure(state="disabled")

    currentvalueframe.pack(pady=(10, 0))
    #####################################################current value frame

    #

    #####################################################enter new value frame
    enternewvalueframe = Frame(window)
    enternewvalueframe.configure(bg="white")

    Label(enternewvalueframe, text="ENTER NEW VALUE : ", bg="white", width=25).pack(
        side=LEFT
    )

    enternewvaluebox = Text(
        enternewvalueframe, bg="white", width=33, height=5, wrap=WORD
    )
    enternewvaluebox.pack(side=RIGHT)

    enternewvalueframe.pack(pady=(10, 0))
    #####################################################enter new value frame

    #
    # update button
    Button(window, text="UPDATE", bg="black", fg="white", command=update_pressed).pack(
        pady=(20, 0)
    )
    #

    window.mainloop()


##############################################################settings window

################################ global threads
def program_thread_settings():
    thread2 = Thread(target=settings_window)
    thread2.start()


def program_thread_listen():
    thread1 = Thread(target=listen)
    thread1.start()


################################ global threads

# when enter key is pressed in entry box
def enter_key_pressed(event):
    program_thread_listen()


# speech to text
def speechtotext():
    r = sr.Recognizer()
    texttospeech_stop("event")
    with sr.Microphone() as source:

        # printing "STARTED Listening" in console
        print()
        print("Listening.. Ask me anything.. ")

        # playing start sound
        try:
            playsound("assets\start_sound.mp3")
        except:
            pass

        # storing listened text
        try:
            listened_text = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            pass

        # printing "FINISHED Listening" in console
        print("Finished Listening.. ")
        print()

        # playing end sound
        try:
            playsound("assets\end_sound.mp3")
        except:
            pass

        # result
        try:
            detection_result = r.recognize_google(listened_text)
        except:
            detection_result = "NO AUDIO DETECTED"

        return detection_result


def listen():
    global infi_listen_bool

    query_input = input_box.get()
    input_box.delete(0, END)

    query_input = query_input.lstrip()
    query_input = query_input.rstrip()

    if len(query_input) == 0:
        query_input = speechtotext()

    # priting mic detected text in console and output box
    print("Mic detected text: ", query_input)
    output_box.configure(state="normal")
    output_box.insert("end", "\n\nYOU: " + query_input)
    output_box.configure(state="disabled")

    # sending query to process function
    if query_input != "NO AUDIO DETECTED":
        query_success_code, query_output = processtext(query_input)
    else:
        query_success_code, query_output = (
            "Response <501>",
            "Sorry, I was not able to detect your voice",
        )

    # printing process result in console and output box
    print("Query Success Code: ", query_success_code)
    print("Final Answer: ", query_output)
    output_box.configure(state="normal")

    # loading config_data into data
    file = open("config_data.json", "r")
    data = json.loads(file.read())
    file.close()

    output_box.insert("end", f"\n{data['WAKE WORD'].upper()}: " + query_output.upper())
    output_box.configure(state="disabled")

    output_box.see(END)
    # speaking result
    texttospeech(query_output)

    # checking for bye code
    if query_success_code == "bye code":
        root.destroy()
        infi_listen_bool = False
        sys.exit(0)

    elif query_success_code == "settings code":
        program_thread_settings()


######################################### loading screen
def loading_screen():

    # creating and styling screen
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.minsize(screen_width, screen_height)
    root.state("zoomed")

    root.title("LAUNCHING")  # title
    root.option_add("*font", "Segoe 15")  # font
    root.configure(bg="white")  # bg color
    root.iconbitmap("assets\logo_icon.ico")  # icon

    logoimg1 = PhotoImage(file="assets\logo_image.png").subsample(5, 5)
    logoimg2 = PhotoImage(file="assets\logo_image2.png").subsample(5, 5)
    logoimg3 = PhotoImage(file="assets\logo_image3.png").subsample(5, 5)
    logoimg4 = PhotoImage(file="assets\logo_image4.png").subsample(5, 5)
    logoimg5 = PhotoImage(file="assets\logo_image5.png").subsample(5, 5)

    logo = Button(root, image=logoimg1, bg="white", highlightthickness=0, bd=0)
    logo.pack(pady=(300, 0))
    logo["state"] = "disabled"

    logotext = Label(text="Loading Scripts ...", bg="white", fg="grey", width=125)
    logotext.pack(pady=20)

    def image_change():

        counter = 0
        list_of_texts = [
            "Scripts Loaded",
            "Connecting to Server ...",
            "Loading Config Data ...",
            "Config Data Loaded",
            "Initialising UI ...",
            "Loading Assets ...",
            "Assets Loaded",
            "Starting September ...",
        ]

        for i in [
            logoimg2,
            logoimg3,
            logoimg4,
            logoimg5,
            logoimg2,
            logoimg3,
            logoimg4,
            logoimg5,
        ]:
            if counter < 4:
                logo.after(100, None)
            else:
                logo.after(250, None)
            logo.configure(image=i)
            logotext.configure(text=list_of_texts[counter])
            counter += 1

    subthread = Thread(target=image_change)
    subthread.start()

    logo.after(2000, root.destroy)
    root.mainloop()


######################################### loading screen

######################################### infinite listen
r = sr.Recognizer()


def infinite_listen():
    global infi_listen_bool
    while infi_listen_bool:
        with sr.Microphone() as source:

            print("Listening")
            # r.adjust_for_ambient_noise(source)

            try:
                listened_text = r.listen(source, timeout=5, phrase_time_limit=5)
            except:
                listened_text = ""

            try:
                detection_result = r.recognize_google(listened_text)
            except:
                detection_result = ""

            # print(detection_result, end = " ")

            # loading config_data into data
            file = open("config_data.json", "r")
            data = json.loads(file.read())
            file.close()

            if data["WAKE WORD"] in detection_result.lower():
                listen()
    sys.exit(0)


######################################### infinite listen

################################################## main program

# call loading screen
loading_screen()
# call infinte listen thread
infthread = Thread(target=infinite_listen)
infthread.start()

# creating screen
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# root.resizable(0, 0)

# setting screen size
root.geometry(f"{screen_width}x{screen_height}")
root.minsize(screen_width, screen_height)
root.state("zoomed")

# styling root screen
root.title("SEPTEMBER ASSISTANT")
root.option_add("*font", "Segoe 15")
root.configure(bg="white")
root.iconbitmap("assets\logo_icon.ico")
##########################################
#######screen elements declaration

################# output box

# output box creation
output_box = Text(root, width=130, height=25, wrap="word", bd=0)
output_box.pack(pady=(40, 0), padx=50)

# output box properties
output_box.configure(state="disabled")
output_box.see(END)

################## output box

################## frame for input box, speak button, settings button

# frame creation
frame = Frame(root)
frame.configure(bg="white")
frame.pack(pady = (30,0))

# input box
input_box = Entry(frame, width=100)
input_box.bind("<Return>", enter_key_pressed)
input_box.pack(side=LEFT)

# mic button
photo = PhotoImage(file="assets\mic_image.png")
photoimage = photo.subsample(2, 2)
mic_button = Button(
    frame, image=photoimage, bd=0, highlightthickness=0, command=program_thread_listen
)
mic_button.pack(side=LEFT, padx=10)

# settings button
photo1 = PhotoImage(file="assets\settings_image.png")
photoimage1 = photo1.subsample(11, 11)
settings_button = Button(
    frame,
    image=photoimage1,
    bd=0,
    highlightthickness=0,
    bg="white",
    command=settings_window,
)
settings_button.pack(side=RIGHT)

################## frame for input box, speak button, settings button

# press escape to stop speaking
root.bind("<Escape>", texttospeech_stop)
root.mainloop()
################################################## main program

sys.exit(0)
