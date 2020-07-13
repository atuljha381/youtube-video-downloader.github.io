from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog

root = Tk()
root.geometry("400x350")
root.resizable(True, True)


root.title("Youtube Downloader")
def Browse():

    download_directory = filedialog.askdirectory(initialdir="D:\\program files\\data_science\\Youtube Downloader")
    download_Path.set(download_directory)


def download():
    try:
        myVar.set("Downloading...")
        root.update()
        download_Folder = download_Path.get()
        YouTube(link.get()).streams.first().download(download_Folder)
        link.set("Video downloaded successfully")
        messagebox.showinfo("Video download successfully to "+download_Folder)
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")

download_Path=StringVar()
#create label widget to welcome user
Label(root, text="Welcome to youtube\ndownloader application", font="Consolas 15 bold ").pack()
#declare string type variable
myVar=StringVar()
#setting default text to myVar
myVar.set("Enter link below")
#Create entry widget to enter url
Entry(root, textvariable=myVar, width=40).pack(pady=10)
#declaring string type variable
link=StringVar()
#create entry widget to get link
Entry(root,textvariable=link,width=40).pack(pady=10)

Button(root,command=Browse,text="Browse").pack()
#create and call download function to download video
Button(root,text="Download video", command=download).pack()
root.mainloop()
