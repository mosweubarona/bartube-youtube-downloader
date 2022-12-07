from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#Functions
def select_path():
    # select where to save file
    path = filedialog.askdirectory()
    path_label.config(text=path, font=("Ariel", 12))

def download_file():
    #get user path
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('File downloading...')
    #get file in high res
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #where to save the file
    shutil.move(mp4_video, user_path)
    screen.title('Download Finish')

screen = Tk()
title = screen.title('Bartube Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#App logo
logo_img = PhotoImage(file='images\\bartube-log.png')
#resize
logo_img = logo_img.subsample(1, 1)
canvas.create_image(250, 80, image=logo_img)

#where link is pasted
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link Below", font=('Arial', 15))

#Select place for saving the file
path_label = Label(screen, text="Select where to save your file:", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='gray', padx='22', pady='5',font=('Arial', 10), fg='#fff', command=select_path)
#Add to window
canvas.create_window(150, 280, window=path_label)
canvas.create_window(370, 280, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download buttons
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
#add to canvas
canvas.create_window(370, 390, window=download_btn)

#instructions
instruction = Label(screen, text="Instructions to follow", font=('Arial', 12))
canvas.create_window(70, 345, window=instruction)

step1 = Label(screen, text="1. Paste the link", font=('Arial', 8))
canvas.create_window(40, 370, window=step1)

step2 = Label(screen, text="2. Select path", font=('Arial', 8))
canvas.create_window(35, 390, window=step2)

step3 = Label(screen, text="3. Click download button", font=('Arial', 8))
canvas.create_window(60, 410, window=step3)

screen.mainloop()
