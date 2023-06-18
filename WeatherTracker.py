from gtts import gTTS
from playsound import playsound
from tkinter import *
import requests
import json


def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("C:\\Users\\user\\PycharmProjects\\pythonProject\\speak.mp3")
    playsound("C:\\Users\\user\\PycharmProjects\\pythonProject\\speak.mp3")


def greet():
    speak("Welcome to Python Weather Tracker")


def user_info(city, country):
    url = f"https://api.weatherapi.com/v1/current.json?key=3b7cc10d13b44696bfe81250230506&q={city},{country}"
    request = requests.get(url)
    user_dict = json.loads(request.text)
    text = f"The current  temperature in {city},{country} is {user_dict['current']['temp_c']}"
    speak(text)


root = Tk()
root.geometry("280x170")
root.minsize(150, 150)
root.maxsize(280, 170)

user_country = StringVar()
user_city = StringVar()

# changing the bg of window
frame_bg = Frame(root, background='#9AC5F4')
frame_bg.pack(fill='both', expand=True)

# adding head to frame_bg
label_head = Label(frame_bg, text="Welcome to Python Weather Tracker", font=("Chakra Petch", 10, "bold"), fg="white",
                   bg="#27374D", borderwidth=5, relief="ridge")
label_head.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# columnspan is used to specify the number of the columns that a widget should span
# label_head widget spans two columns (column 0 and column 1) using columnspan=2

label_country = Label(frame_bg, text="Enter the country", font=("Chakra Petch", 10, "bold"), bg="#9AC5F4", fg="#321E1E")
label_country.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_country = Entry(frame_bg, textvariable=user_country)
entry_country.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_city = Label(frame_bg, text="Enter the city", font=("Chakra Petch", 10, "bold"), bg="#9AC5F4", fg="#321E1E")
label_city.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_city = Entry(frame_bg, textvariable=user_city)
entry_city.grid(row=2, column=1, padx=10, pady=5, sticky="w")


# here sticky is used to set the widget's position relative to the cell
# and anchor is used to set the reference point for the widget's position within the cell


def user_input():
    country = user_country.get()
    city = user_city.get()
    user_info(city, country)


apply_button = Button(frame_bg, text="Apply", command=user_input, font=("Chakra Petch", 10, "bold"), fg="#321E1E",
                      bg="white")
apply_button.grid(row=3, column=1, sticky='nw', ipadx=3)
# ipad is used to give internal space between the contents of a widget and the edges of widget

quit_button = Button(frame_bg, text="Quit", command=quit, font=("Chakra Petch", 10, "bold"), fg="#321E1E", bg="white")
quit_button.grid(row=3, column=1, sticky='ne', padx=13, ipadx=3)

# # delaying the function greet by 100 milliseconds
# # so that window is displayed before the greet function() is called
root.after(100, greet)

root.mainloop()
