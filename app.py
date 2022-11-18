from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageChops
import requests
import urllib
import webbrowser

def getUser(user):
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url=url).json()
    if response:
        rName = response['name']
        bioText = response['bio']
        id = response['id']
        av = response['avatar_url']
        pageUrl = response['html_url']
        company = response['company']
        location = response['location']
        email = response['email']
        twitter = response['twitter_username']
        publicRepos = response['public_repos']
        followers = response['followers']
        following = response['following']
        creationTime = response['created_at']

        return (rName, bioText, id, av, pageUrl, company, location, email, twitter, publicRepos, followers, following, creationTime)
    else:
        print('idek')

def link():
    user = nameEntry.get()
    info = getUser(user)
    url = f"{info[4]}"
    webbrowser.open_new(url)

def main():
    user = nameEntry.get()
    info = getUser(user)
    if info:
        urllib.request.urlretrieve(f"{info[3]}", "avatar.png")
        image = Image.open(r"avatar.png").convert('RGBA')
        nimg = image.resize((200,200))
        img = ImageTk.PhotoImage(nimg)
        imageLabel.configure(image=img)
        imageLabel.image = img
        ct = info[12]
        head, sep, tail = ct.partition('T')
        informationsLabel['text'] = f"ID: {info[2]}\nName: {info[0]}\nBio: {info[1]}\nCompany: {info[5]}\nLocation: {info[6]}\nEmail: {info[7]}\nTwitter: {info[8]}\nPublic Repos: {info[9]}\nFollowers: {info[10]}\nFollowing: {info[11]}\nAccount Creation Time: {head}"

window = Tk()
window.geometry("700x500")
window.title("GitHub Userinfo App")
window.resizable(False,False) # to make the window not resizable
window['background'] = "#7289da" # to set the background colour
window.iconbitmap(r'favicon.ico')

nameEntry = Entry(window, font="Arial 14",width=16, justify="center")
nameEntry.place(x=70, y=50, height=37)
nameEntry.focus()

linkBtn = Button(window, font="Arial 12", text="GitHub Page", command=link)
linkBtn.place(x = 70, y= 110)

searchBtn = Button(window, font="Arial 12", text="Search", command=main)
searchBtn.place(x = 270, y= 53)

imageLabel = Label(window)
imageLabel['background'] = "#7289da"
imageLabel.pack(padx= 70, side=LEFT)

informationsLabel= Label(window, font="Arial 13")
informationsLabel['background'] = "#7289da"
informationsLabel.pack(side=RIGHT, padx=20)


window.mainloop()