# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
 
def Widgets():
 
    head_label = Label(root, text="YouTube Video Downloader Using Tkinter",
                       padx=15,
                       pady=15,
                       font="Awesome",
                       bg="#c4302b",
                       fg="#000000")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)
 
    root.linkText = Entry(root,
                          width=28,
                          fg="#00a22b",
                          bg="#ffffff",
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
 
    browse_B = Button(root,
                      text="Choose your destination folder HERE!",
                      command=Browse,
                      width=25,
                      font="Awesome",
                      bg='red',
                     relief=GROOVE)
    browse_B.grid(row=3,
                  column=1,
                  pady=1,   
                  padx=1)
 
    Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        font="Awesome",
                        bg="#c4302b",
                        fg="#000000",
                        relief=GROOVE,
                        )
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)
 
 
# Defining Browse() to select a
# destination folder to save the video
 
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")
 
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
 
# Defining Download() to download the video
 
 
def Download():
 
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
 
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)
 
 
 root = tk.Tk()
 
root.geometry("500x280")
root.resizable(True, False)
root.title("YouTube Video Downloader")
root.config(background="#000000")
 
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
 
# Calling the Widgets() function
Widgets()
 
# Defining infinite loop to run
# application
root.mainloop()