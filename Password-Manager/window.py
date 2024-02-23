import re
import random
import requests
import string
import pyperclip
import inspect
import pyotp
import qrcode
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def btn_clicked():
    print("Button Clicked")

def hide():
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = show, relief = "flat")
    b1.place(x = 891, y = 357, width = 54, height = 61)
    entry0.config(show="*")
    
def show():
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = hide, relief = "flat")
    b1.place(x = 891, y = 357, width = 54, height = 61)
    entry0.config(show="") 
    
def check_login(username, password):
    return username == "Yousef" and password == "password"

def password_generator(size=10):
    password = []
    while len(password) < size:
        password.append(random.choice(string.ascii_lowercase))  
        if len(password) < size:
            password.append(random.choice(string.ascii_uppercase))  
        if len(password) < size:
            password.append(random.choice(string.digits)) 
        if len(password) < size:
            password.append(random.choice(string.punctuation))  
    random.shuffle(password)  
    return ''.join(password)

def generate_password():
    password = password_generator(10)
    password_label.config(text=password,fg="#B0BBE3")
    pyperclip.copy(password)
    
def password_checker(entered_password):
    if len(entered_password) >= 8:
        if bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d])', entered_password)):
            result_label.config(text="Strong Password", fg="green")
        else:
            result_label.config(text="Weak Password", fg="red")
    else:
        result_label.config(text="Invalid Password", fg="red")

def check_password():
    entered_password = entry2.get()
    password_checker(entered_password)

def key_return(event):
    username = entry1.get()
    password = entry0.get()
    on_login_button_clicked(entry1, entry0)

def add_top_level1():
    window1.destroy()
    global top1
    top1 = Tk()
    top1.geometry("500x300")
    top1.configure(bg = "#202037")
    top1.title("Password manager")
    top1.iconbitmap("icon.ico")

    canvas = Canvas(top1, bg = "#202037", height = 300, width = 500, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    global entrytop1
    entrytop1_img = PhotoImage(file = f"img_textBox0top.png")
    entrytop1_bg = canvas.create_image(363.0, 85.0, image = entrytop1_img)
    entrytop1 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A", font=top_text_font)
    entrytop1.place(x = 262.0, y = 65, width = 202.0, height = 38)

    global entrytop2
    entrytop2_img = PhotoImage(file = f"img_textBox1top.png")
    entrytop2_bg = canvas.create_image(363.0, 141.0, image = entrytop2_img)
    entrytop2 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop2.place(x = 262.0, y = 121, width = 202.0, height = 38)

    global entrytop3
    entrytop3_img = PhotoImage(file = f"img_textBox2top.png")
    entrytop3_bg = canvas.create_image(363.0, 197.0, image = entrytop3_img)
    entrytop3 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop3.place(x = 262.0, y = 177, width = 202.0, height = 38)

    img0 = PhotoImage(file = f"img0top.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = close_top_level1, relief = "flat")
    b0.place(x = 181, y = 244, width = 137, height = 40)

    background_img = PhotoImage(file = f"backgroundtop.png")
    background = canvas.create_image(211.5, 112.0, image=background_img)
    
    top1.resizable(False, False)
    top1.mainloop()

def add_top_level2():
    window2.destroy()
    global top2
    top2 = Tk()
    top2.geometry("500x300")
    top2.configure(bg = "#202037")
    top2.title("Password manager")
    top2.iconbitmap("icon.ico")

    canvas = Canvas(top2, bg = "#202037", height = 300, width = 500, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    global entrytop4
    entrytop4_img = PhotoImage(file = f"img_textBox0top.png")
    entrytop4_bg = canvas.create_image(363.0, 85.0, image = entrytop4_img)
    entrytop4 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop4.place(x = 262.0, y = 65, width = 202.0, height = 38)
    
    global entrytop5
    entrytop5_img = PhotoImage(file = f"img_textBox1top.png")
    entrytop5_bg = canvas.create_image(363.0, 141.0, image = entrytop5_img)
    entrytop5 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop5.place(x = 262.0, y = 121, width = 202.0, height = 38)

    global entrytop6
    entrytop6_img = PhotoImage(file = f"img_textBox2top.png")
    entrytop6_bg = canvas.create_image(363.0, 197.0, image = entrytop6_img)
    entrytop6 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop6.place(x = 262.0, y = 177, width = 202.0, height = 38)

    img0 = PhotoImage(file = f"img0top.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = close_top_level2, relief = "flat")
    b0.place(x = 181, y = 244, width = 137, height = 40)

    background_img = PhotoImage(file = f"backgroundtop.png")
    background = canvas.create_image(211.5, 112.0, image=background_img)
    
    top2.resizable(False, False)
    top2.mainloop()

def add_top_level3():
    window3.destroy()
    global top3
    top3 = Tk()
    top3.geometry("500x300")
    top3.configure(bg = "#202037")
    top3.title("Password manager")
    top3.iconbitmap("icon.ico")

    canvas = Canvas(top3, bg = "#202037", height = 300, width = 500, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    global entrytop7
    entrytop7_img = PhotoImage(file = f"img_textBox0top.png")
    entrytop7_bg = canvas.create_image(363.0, 85.0, image = entrytop7_img)
    entrytop7 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop7.place(x = 262.0, y = 65, width = 202.0, height = 38)

    global entrytop8
    entrytop8_img = PhotoImage(file = f"img_textBox1top.png")
    entrytop8_bg = canvas.create_image(363.0, 141.0, image = entrytop8_img)
    entrytop8 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop8.place(x = 262.0, y = 121, width = 202.0, height = 38)
  
    global entrytop9
    entrytop9_img = PhotoImage(file = f"img_textBox2top.png")
    entrytop9_bg = canvas.create_image(363.0, 197.0, image = entrytop9_img)
    entrytop9 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop9.place(x = 262.0, y = 177, width = 202.0, height = 38)

    img0 = PhotoImage(file = f"img0top.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = close_top_level3, relief = "flat")
    b0.place(x = 181, y = 244, width = 137, height = 40)

    background_img = PhotoImage(file = f"backgroundtop.png")
    background = canvas.create_image(211.5, 112.0, image=background_img)
    
    top3.resizable(False, False)
    top3.mainloop()
    
def add_top_level4():
    window4.destroy()
    global top4
    top4 = Tk()
    top4.geometry("500x300")
    top4.configure(bg = "#202037")
    top4.title("Password manager")
    top4.iconbitmap("icon.ico")

    canvas = Canvas(top4, bg = "#202037", height = 300, width = 500, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    global entrytop10
    entrytop10_img = PhotoImage(file = f"img_textBox0top.png")
    entrytop10_bg = canvas.create_image(363.0, 85.0, image = entrytop10_img)
    entrytop10 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop10.place(x = 262.0, y = 65, width = 202.0, height = 38)

    global entrytop11
    entrytop11_img = PhotoImage(file = f"img_textBox1top.png")
    entrytop11_bg = canvas.create_image(363.0, 141.0, image = entrytop11_img)
    entrytop11 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop11.place(x = 262.0, y = 121, width = 202.0, height = 38)

    global entrytop12
    entrytop12_img = PhotoImage(file = f"img_textBox2top.png")
    entrytop12_bg = canvas.create_image(363.0, 197.0, image = entrytop12_img)
    entrytop12 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop12.place(x = 262.0, y = 177, width = 202.0, height = 38)

    img0 = PhotoImage(file = f"img0top.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = close_top_level4, relief = "flat")
    b0.place(x = 181, y = 244, width = 137, height = 40)

    background_img = PhotoImage(file = f"backgroundtop.png")
    background = canvas.create_image(211.5, 112.0, image=background_img)
    
    top4.resizable(False, False)
    top4.mainloop()
  
def add_top_level5():
    window5.destroy()
    global top5
    top5 = Tk()
    top5.geometry("500x300")
    top5.configure(bg = "#202037")
    top5.title("Password manager")
    top5.iconbitmap("icon.ico")

    canvas = Canvas(top5, bg = "#202037", height = 300, width = 500, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    global entrytop13
    entrytop13_img = PhotoImage(file = f"img_textBox0top.png")
    entrytop13_bg = canvas.create_image(363.0, 85.0, image = entrytop13_img)
    entrytop13 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop13.place(x = 262.0, y = 65, width = 202.0, height = 38)

    global entrytop14
    entrytop14_img = PhotoImage(file = f"img_textBox1top.png")
    entrytop14_bg = canvas.create_image(363.0, 141.0, image = entrytop14_img)
    entrytop14 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop14.place(x = 262.0, y = 121, width = 202.0, height = 38)

    global entrytop15
    entrytop15_img = PhotoImage(file = f"img_textBox2top.png")
    entrytop15_bg = canvas.create_image(363.0, 197.0, image = entrytop15_img)
    entrytop15 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#383A5A",  font=top_text_font)
    entrytop15.place(x = 262.0, y = 177, width = 202.0, height = 38)

    img0 = PhotoImage(file = f"img0top.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = close_top_level5, relief = "flat")
    b0.place(x = 181, y = 244, width = 137, height = 40)

    background_img = PhotoImage(file = f"backgroundtop.png")
    background = canvas.create_image(211.5, 112.0, image=background_img)
    
    top5.resizable(False, False)
    top5.mainloop()
    
def close_top_level1():
    global site1
    global username1
    global password1
    site1 = entrytop1.get()
    username1 = entrytop2.get()
    password1 = entrytop3.get()
    top1.destroy()
    
def close_top_level2():
    global site2
    global username2
    global password2
    site2 = entrytop4.get()
    username2 = entrytop5.get()
    password2 = entrytop6.get()
    top2.destroy()
    
def close_top_level3():
    global site3
    global username3
    global password3
    site3 = entrytop7.get()
    username3 = entrytop8.get()
    password3 = entrytop9.get()
    top3.destroy()
    
def close_top_level4():
    global site4
    global username4
    global password4
    site4 = entrytop10.get()
    username4 = entrytop11.get()
    password4 = entrytop12.get()
    top4.destroy()
    
def close_top_level5():
    global site5
    global username5
    global password5
    site5 = entrytop13.get()
    username5 = entrytop14.get()
    password5 = entrytop15.get()
    top5.destroy()

def add1():
    if inspect.stack()[1][3] == "importpassword":
        window1.destroy()
    else:
        add_top_level1()
    global window2
    window2 = Tk()
    window2.title("Password manager")
    window2.geometry("1000x600")
    window2.configure(bg = "#202037")
    window2.iconbitmap("icon.ico")

    canvas = Canvas(window2, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background2.png")
    background = canvas.create_image(499.0, 149.0, image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = destroy2, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
    b1.place(x = 501, y = 0, width = 499, height = 80)

    img2 = PhotoImage(file = f"img2.png")
    plus2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = add2, relief = "flat")
    plus2.place(x = 448, y = 542, width = 101, height = 42)

    global showimg3
    showimg3 = PhotoImage(file = f"img3.png")
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassx, relief = "flat")
    b3.place(x = 895, y = 147, width = 62, height = 42)
    
    img9 = PhotoImage(file = f"img9.png")
    save = Button(image = img9, borderwidth = 0, highlightthickness = 0, command = save_data1, relief = "flat")
    save.place(x = 24, y = 542, width = 131, height = 42)
    
    newimg = PhotoImage(file = f"new.png")
    new = Button(image = newimg, borderwidth = 0, highlightthickness = 0, command = remove_data1, relief = "flat")
    new.place(x = 843, y = 542, width = 131, height = 42)
    
    global entrypass0
    entrypass0_img = PhotoImage(file = f"img_textBox4P.png")
    entrypass0_bg = canvas.create_image(782.0, 172.0, image = entrypass0_img)
    entrypass0 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass0.config(show="*")
    entrypass0.insert(0, password1)
    entrypass0.place(x = 704.0, y = 152, width = 156.0, height = 38)
    
    global passwordone
    passwordone = entrypass0.get()

    global site1_label
    site1_label = Label(window2, text=site1, bg="#B0BBE3", font=label_font, fg="#202037")
    site1_label.place(x=65, y=155)
    
    global username1_label
    username1_label = Label(window2, text=username1, bg="#B0BBE3", font=label_font, fg="#202037")
    username1_label.place(x=445, y=155)
    
    d1()
    
    window2.resizable(False, False)
    window2.mainloop()

def hidepassx():
    encrypted_password = aes_crypt(passwordone, key, 'encrypt')
    entrypass0.config(show="*")

    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassx, relief = "flat")
    b3.place(x = 895, y = 147, width = 62, height = 42)
    with open('encrypted_file1.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassx():
    with open('encrypted_file1.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass0.config(show="")
    entrypass0.delete(0, 'end')
    entrypass0.insert(0, decrypted_password)
    
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = hidepassx, relief = "flat")
    b3.place(x = 895, y = 147, width = 62, height = 42)
    
def add2():
    if inspect.stack()[1][3] == "importpassword":
        window1.destroy()
    else:
        add_top_level2()
    global window3
    window3 = Tk()
    window3.title("Password manager")
    window3.geometry("1000x600")
    window3.configure(bg = "#202037")
    window3.iconbitmap("icon.ico")

    canvas = Canvas(window3, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background3.png")
    background = canvas.create_image(499.0, 189.5, image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = destroy3, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
    b1.place(x = 501, y = 0, width = 499, height = 80)

    img2 = PhotoImage(file = f"img2.png")
    plus3 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = add3, relief = "flat")
    plus3.place(x = 448, y = 542, width = 101, height = 42)
    
    global showimg3
    showimg3 = PhotoImage(file = f"img3.png")
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassx2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)

    global showimg4
    showimg4 = PhotoImage(file = f"img4.png")
    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = showpassx1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)

    img9 = PhotoImage(file = f"img9.png")
    save = Button(image = img9, borderwidth = 0, highlightthickness = 0, command = save_data2, relief = "flat")
    save.place(x = 24, y = 542, width = 131, height = 42)
    
    global entrypass1
    entrypass1_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass1_bg = canvas.create_image(782.0, 253.0, image = entrypass1_img)
    entrypass1 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass1.config(show="*")
    entrypass1.insert(0, password2)
    entrypass1.place(x = 704.0, y = 233, width = 156.0, height = 38)

    global passwordtwo
    passwordtwo = entrypass1.get()

    global entrypass0
    entrypass0_img = PhotoImage(file = f"img_textBox4P.png")
    entrypass0_bg = canvas.create_image(782.0, 172.0, image = entrypass0_img)
    entrypass0 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass0.config(show="*")
    entrypass0.insert(0, password1)
    entrypass0.place(x = 704.0, y = 152, width = 156.0, height = 38)
    
    global passwordone
    passwordone = entrypass0.get()
    
    global site1_label
    site1_label = Label(window3, text=site1, bg="#B0BBE3", font=label_font, fg="#202037")
    site1_label.place(x=65, y=155)
    
    global username1_label
    username1_label = Label(window3, text=username1, bg="#B0BBE3", font=label_font, fg="#202037")
    username1_label.place(x=445, y=155)
    
    global site2_label
    site2_label = Label(window3, text=site2, bg="#B0BBE3", font=label_font, fg="#202037")
    site2_label.place(x=65, y=240)
    
    global username2_label
    username2_label = Label(window3, text=username2, bg="#B0BBE3", font=label_font, fg="#202037")
    username2_label.place(x=445, y=240)

    newimg = PhotoImage(file = f"new.png")
    new = Button(image = newimg, borderwidth = 0, highlightthickness = 0, command = remove_data2, relief = "flat")
    new.place(x = 843, y = 542, width = 131, height = 42)
    
    d2()
    
    window3.resizable(False, False)
    window3.mainloop()

def hidepassx1():
    encrypted_password = aes_crypt(passwordone, key, 'encrypt')
    entrypass0.config(show="*")

    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = showpassx1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)
    with open('encrypted_file1.txt', 'w') as file:
        file.write(encrypted_password)
        
def showpassx1():
    with open('encrypted_file1.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass0.config(show="")
    entrypass0.delete(0, 'end')
    entrypass0.insert(0, decrypted_password)
    
    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = hidepassx, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)
    
def hidepassx2():
    encrypted_password = aes_crypt(passwordtwo, key, 'encrypt')
    entrypass1.config(show="*")

    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassx2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)
    with open('encrypted_file2.txt', 'w') as file:
        file.write(encrypted_password)
    
    
def showpassx2():
    with open('encrypted_file2.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass1.config(show="")
    entrypass1.delete(0, 'end')
    entrypass1.insert(0, decrypted_password)
    
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = hidepassx2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)

    
def add3():
    if inspect.stack()[1][3] == "importpassword":
        window1.destroy()
    else:
        add_top_level3()
    global window4
    window4 = Tk()
    window4.title("Password manager")
    window4.geometry("1000x600")
    window4.configure(bg = "#202037")
    window4.iconbitmap("icon.ico")

    canvas = Canvas(window4, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background4.png")
    background = canvas.create_image(499.0, 230.0, image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0, borderwidth = 0, command = destroy4,highlightthickness = 0, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, relief = "flat")
    b1.place(x = 501, y = 0, width = 499, height = 80)

    img2 = PhotoImage(file = f"img2.png")
    plus4= Button(image = img2, borderwidth = 0, highlightthickness = 0, command = add4, relief = "flat")
    plus4.place(x = 448, y = 542, width = 101, height = 42)

    global showimg3
    showimg3 = PhotoImage(file = f"img3.png")
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassy2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)
 
    global showimg4
    showimg4 = PhotoImage(file = f"img4.png")
    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = showpassy1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)

    global showimg5
    showimg5 = PhotoImage(file = f"img5.png")
    b5 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassy3, relief = "flat")
    b5.place(x = 895, y = 311, width = 62, height = 42)

    img9 = PhotoImage(file = f"img9.png")
    save = Button(image = img9, borderwidth = 0, highlightthickness = 0, command = save_data3, relief = "flat")
    save.place(x = 24, y = 542, width = 131, height = 42)
    
    newimg = PhotoImage(file = f"new.png")
    new = Button(image = newimg, borderwidth = 0, highlightthickness = 0, command = remove_data3, relief = "flat")
    new.place(x = 843, y = 542, width = 131, height = 42)
    
    global entrypass2
    entrypass2_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass2_bg = canvas.create_image(782.0, 336.0, image = entrypass2_img)
    entrypass2 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass2.config(show="*")
    entrypass2.insert(0, password3)
    entrypass2.place(x = 704.0, y = 316, width = 156.0, height = 38)
    
    global passwordthree
    passwordthree = entrypass2.get()
    
    global entrypass1
    entrypass1_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass1_bg = canvas.create_image(782.0, 253.0, image = entrypass1_img)
    entrypass1 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass1.config(show="*")
    entrypass1.insert(0, password2)
    entrypass1.place(x = 704.0, y = 233, width = 156.0, height = 38)
   
    global passwordtwo
    passwordtwo = entrypass1.get()
    
    global entrypass0
    entrypass0_img = PhotoImage(file = f"img_textBox4P.png")
    entrypass0_bg = canvas.create_image(782.0, 172.0, image = entrypass0_img)
    entrypass0 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass0.config(show="*")
    entrypass0.insert(0, password1)
    entrypass0.place(x = 704.0, y = 152, width = 156.0, height = 38)
    
    global passwordone
    passwordone = entrypass0.get()

    global site1_label
    site1_label = Label(window4, text=site1, bg="#B0BBE3", font=label_font, fg="#202037")
    site1_label.place(x=65, y=155)
    
    global username1_label
    username1_label = Label(window4, text=username1, bg="#B0BBE3", font=label_font, fg="#202037")
    username1_label.place(x=445, y=155)
    
    global site2_label
    site2_label = Label(window4, text=site2, bg="#B0BBE3", font=label_font, fg="#202037")
    site2_label.place(x=65, y=240)
    
    global username2_label
    username2_label = Label(window4, text=username2, bg="#B0BBE3", font=label_font, fg="#202037")
    username2_label.place(x=445, y=240)
    
    global site3_label
    site3_label = Label(window4, text=site3, bg="#B0BBE3", font=label_font, fg="#202037")
    site3_label.place(x=65, y=320)
    
    global username3_label
    username3_label = Label(window4, text=username3, bg="#B0BBE3", font=label_font, fg="#202037")
    username3_label.place(x=445, y=320)
    
    d3()
    
    window4.resizable(False, False)
    window4.mainloop()
    
def hidepassy1():
    encrypted_password = aes_crypt(passwordone, key, 'encrypt')
    entrypass0.config(show="*")

    b4 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassy1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)
    with open('encrypted_file1.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassy1():
    with open('encrypted_file1.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass0.config(show="")
    entrypass0.delete(0, 'end')
    entrypass0.insert(0, decrypted_password)
    
    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = hidepassy1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)

def hidepassy2():
    encrypted_password = aes_crypt(passwordtwo, key, 'encrypt')
    entrypass1.config(show="*")
    
    b3 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassy2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)
    with open('encrypted_file2.txt', 'w') as file:
        file.write(encrypted_password)

    
def showpassy2():
    with open('encrypted_file2.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass1.config(show="")
    entrypass1.delete(0, 'end')
    entrypass1.insert(0, decrypted_password)
    
    b3 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = hidepassy2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)
    
def hidepassy3():
    encrypted_password = aes_crypt(passwordthree, key, 'encrypt')
    entrypass2.config(show="*")
    
    b5 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassy3, relief = "flat")
    b5.place(x = 895, y = 311, width = 62, height = 42)
    with open('encrypted_file3.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassy3():
    with open('encrypted_file3.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass2.config(show="")
    entrypass2.delete(0, 'end')
    entrypass2.insert(0, decrypted_password)
    
    b5 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = hidepassy3, relief = "flat")
    b5.place(x = 895, y = 311, width = 62, height = 42)
    
def add4():
    if inspect.stack()[1][3] == "importpassword":
        window1.destroy()
    else:
        add_top_level4()
    global window5
    window5 = Tk()
    window5.title("Password manager")
    window5.geometry("1000x600")
    window5.configure(bg = "#202037")
    window5.iconbitmap("icon.ico")

    canvas = Canvas(window5, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background5.png")
    background = canvas.create_image(499.0, 270.5, image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = destroy5, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
    b1.place(x = 501, y = 0, width = 499, height = 80)

    img2 = PhotoImage(file = f"img2.png")
    plus5 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = add5, relief = "flat")
    plus5.place(x = 448, y = 542, width = 101, height = 42)
    
    newimg = PhotoImage(file = f"new.png")
    new = Button(image = newimg, borderwidth = 0, highlightthickness = 0, command = remove_data4, relief = "flat")
    new.place(x = 843, y = 542, width = 131, height = 42)
    
    global showimg3
    showimg3 = PhotoImage(file = f"img3.png")
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassz2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)
 
    global showimg4
    showimg4 = PhotoImage(file = f"img4.png")
    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = showpassz1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)

    global showimg5
    showimg5 = PhotoImage(file = f"img5.png")
    b5 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassz3, relief = "flat")
    b5.place(x = 895, y = 311, width = 62, height = 42)
    
    global showimg6
    showimg6 = PhotoImage(file = f"img6.png")
    b6 = Button(image = showimg6, borderwidth = 0, highlightthickness = 0, command = showpassz4, relief = "flat")
    b6.place(x = 895, y = 393, width = 62, height = 42)
    
    img9 = PhotoImage(file = f"img9.png")
    save = Button(image = img9, borderwidth = 0, highlightthickness = 0, command = save_data4, relief = "flat")
    save.place(x = 24, y = 542, width = 131, height = 42)
    
    global entrypass3
    entrypass3_img = PhotoImage(file = f"img_textBox1P.png")
    entrypass3_bg = canvas.create_image(782.0, 415.0, image = entrypass3_img)
    entrypass3 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass3.config(show="*")
    entrypass3.insert(0, password4)
    entrypass3.place(x = 704.0, y = 395, width = 156.0, height = 38)
    
    global passwordfour
    passwordfour = entrypass3.get()
    
    global entrypass2
    entrypass2_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass2_bg = canvas.create_image(782.0, 336.0, image = entrypass2_img)
    entrypass2 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass2.config(show="*")
    entrypass2.insert(0, password3)
    entrypass2.place(x = 704.0, y = 316, width = 156.0, height = 38)

    global passwordthree
    passwordthree = entrypass2.get()

    global entrypass1
    entrypass1_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass1_bg = canvas.create_image(782.0, 253.0, image = entrypass1_img)
    entrypass1 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass1.config(show="*")
    entrypass1.insert(0, password2)
    entrypass1.place(x = 704.0, y = 233, width = 156.0, height = 38)
   
    global passwordtwo
    passwordtwo = entrypass1.get()

    global entrypass0
    entrypass0_img = PhotoImage(file = f"img_textBox4P.png")
    entrypass0_bg = canvas.create_image(782.0, 172.0, image = entrypass0_img)
    entrypass0 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass0.config(show="*")
    entrypass0.insert(0, password1)
    entrypass0.place(x = 704.0, y = 152, width = 156.0, height = 38)
    
    global passwordone
    passwordone = entrypass0.get()

    global site1_label
    site1_label = Label(window5, text=site1, bg="#B0BBE3", font=label_font, fg="#202037")
    site1_label.place(x=65, y=155)
    
    global username1_label
    username1_label = Label(window5, text=username1, bg="#B0BBE3", font=label_font, fg="#202037")
    username1_label.place(x=445, y=155)
    
    global site2_label
    site2_label = Label(window5, text=site2, bg="#B0BBE3", font=label_font, fg="#202037")
    site2_label.place(x=65, y=240)
    
    global username2_label
    username2_label = Label(window5, text=username2, bg="#B0BBE3", font=label_font, fg="#202037")
    username2_label.place(x=445, y=240)
    
    global site3_label
    site3_label = Label(window5, text=site3, bg="#B0BBE3", font=label_font, fg="#202037")
    site3_label.place(x=65, y=320)
    
    global username3_label
    username3_label = Label(window5, text=username3, bg="#B0BBE3", font=label_font, fg="#202037")
    username3_label.place(x=445, y=320)
        
    global site4_label
    site4_label = Label(window5, text=site4, bg="#B0BBE3", font=label_font, fg="#202037")
    site4_label.place(x=65, y=400)
    
    global username4_label
    username4_label = Label(window5, text=username4, bg="#B0BBE3", font=label_font, fg="#202037")
    username4_label.place(x=445, y=400)
    
    d4()
    
    window5.resizable(False, False)
    window5.mainloop()

def hidepassz1():
    encrypted_password = aes_crypt(passwordone, key, 'encrypt')
    entrypass0.config(show="*")
    
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassz1, relief = "flat")
    b3.place(x = 895, y = 147, width = 62, height = 42)
    with open('encrypted_file1.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassz1():
    with open('encrypted_file1.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass0.config(show="")
    entrypass0.delete(0, 'end')
    entrypass0.insert(0, decrypted_password)
    
    b4 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = hidepassz1, relief = "flat")
    b4.place(x = 895, y = 147, width = 62, height = 42)

def hidepassz2():
    encrypted_password = aes_crypt(passwordtwo, key, 'encrypt')
    entrypass1.config(show="*")
    
    b3 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassz2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)
    with open('encrypted_file2.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassz2():
    with open('encrypted_file2.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass1.config(show="")
    entrypass1.delete(0, 'end')
    entrypass1.insert(0, decrypted_password)
    
    b3 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = hidepassz2, relief = "flat")
    b3.place(x = 895, y = 229, width = 62, height = 42)

    
def hidepassz3():
    encrypted_password = aes_crypt(passwordthree, key, 'encrypt')
    entrypass2.config(show="*")
    
    b5 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassz3, relief = "flat")
    b5.place(x = 895, y = 311, width = 62, height = 42)
    with open('encrypted_file3.txt', 'w') as file:
        file.write(encrypted_password)
            
def showpassz3():
    with open('encrypted_file3.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass2.config(show="")
    entrypass2.delete(0, 'end')
    entrypass2.insert(0, decrypted_password)
    
    b5 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = hidepassz3, relief = "flat")
    b5.place(x = 895, y = 311, width = 62, height = 42)


def hidepassz4():
    encrypted_password = aes_crypt(passwordthree, key, 'encrypt')
    entrypass3.config(show="*")
    
    b6 = Button(image = showimg6, borderwidth = 0, highlightthickness = 0, command = showpassz4, relief = "flat")
    b6.place(x = 895, y = 393, width = 62, height = 42)
    with open('encrypted_file3.txt', 'w') as file:
        file.write(encrypted_password)
            
def showpassz4():
    with open('encrypted_file4.txt', 'r') as file:
        encrypted_password = file.read()
    
    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass3.config(show="")
    entrypass3.delete(0, 'end')
    entrypass3.insert(0, decrypted_password)
    
    b6 = Button(image = showimg6, borderwidth = 0, highlightthickness = 0, command = hidepassz4, relief = "flat")
    b6.place(x = 895, y = 393, width = 62, height = 42)

def add5():
    if inspect.stack()[1][3] == "importpassword":
        window1.destroy()
    else:
        add_top_level5()
    global window6
    window6 = Tk()
    window6.title("Password manager")
    window6.geometry("1000x600")
    window6.configure(bg = "#202037")
    window6.iconbitmap("icon.ico")

    canvas = Canvas(window6, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background6.png")
    background = canvas.create_image(499.0, 311.0, image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = destroy6, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
    b1.place(x = 501, y = 0, width = 499, height = 80)

    img2 = PhotoImage(file = f"img2.png")
    plus6 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = add6, relief = "flat")
    plus6.place(x = 448, y = 542, width = 101, height = 42)
    
    newimg = PhotoImage(file = f"new.png")
    new = Button(image = newimg, borderwidth = 0, highlightthickness = 0, command = remove_data5, relief = "flat")
    new.place(x = 843, y = 542, width = 131, height = 42)
    
    global showimg3
    showimg3 = PhotoImage(file = f"img3.png")
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassc2, relief = "flat")
    b3.place(x = 895, y = 230, width = 62, height = 42)
    
    global showimg7
    showimg7 = PhotoImage(file = f"img4.png")
    b4 = Button(image = showimg7, borderwidth = 0, highlightthickness = 0, command = showpassc5, relief = "flat")
    b4.place(x = 895, y = 475, width = 62, height = 42)
    
    global showimg6
    showimg6 = PhotoImage(file = f"img5.png")
    b5 = Button(image = showimg6, borderwidth = 0, highlightthickness = 0, command = showpassc4, relief = "flat")
    b5.place(x = 895, y = 393, width = 62, height = 42)

    global showimg4
    showimg4 = PhotoImage(file = f"img6.png")
    b6 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = showpassc1, relief = "flat")
    b6.place(x = 895, y = 147, width = 62, height = 42)

    global showimg5
    showimg5 = PhotoImage(file = f"img7.png")
    b7 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassc3, relief = "flat")
    b7.place(x = 895, y = 311, width = 62, height = 42)

    img9 = PhotoImage(file = f"img9.png")
    save = Button(image = img9, borderwidth = 0, highlightthickness = 0, command = save_data5, relief = "flat")
    save.place(x = 24, y = 542, width = 131, height = 42)
    
    global entrypass4
    entrypass4_img = PhotoImage(file = f"img_textBox0P.png")
    entrypass4_bg = canvas.create_image(782.0, 497.0, image = entrypass4_img)
    entrypass4 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass4.config(show="*")
    entrypass4.insert(0, password5)
    entrypass4.place(x = 704.0, y = 475, width = 156.0, height = 38)
    
    global passwordfive
    passwordfive = entrypass4.get()
    
    global entrypass3
    entrypass3_img = PhotoImage(file = f"img_textBox1P.png")
    entrypass3_bg = canvas.create_image(782.0, 415.0, image = entrypass3_img)
    entrypass3 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass3.config(show="*")
    entrypass3.insert(0, password4)
    entrypass3.place(x = 704.0, y = 395, width = 156.0, height = 38)
    
    global passwordfour
    passwordfour = entrypass3.get()

    global entrypass2
    entrypass2_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass2_bg = canvas.create_image(782.0, 336.0, image = entrypass2_img)
    entrypass2 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass2.config(show="*")
    entrypass2.insert(0, password3)
    entrypass2.place(x = 704.0, y = 316, width = 156.0, height = 38)
    
    global passwordthree
    passwordthree = entrypass2.get()

    global entrypass1
    entrypass1_img = PhotoImage(file = f"img_textBox3P.png")
    entrypass1_bg = canvas.create_image(782.0, 253.0, image = entrypass1_img)
    entrypass1 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass1.config(show="*")
    entrypass1.insert(0, password2)
    entrypass1.place(x = 704.0, y = 233, width = 156.0, height = 38)

    global passwordtwo
    passwordtwo = entrypass1.get()

    global entrypass0
    entrypass0_img = PhotoImage(file = f"img_textBox4P.png")
    entrypass0_bg = canvas.create_image(782.0, 172.0, image = entrypass0_img)
    entrypass0 = Entry(bd = 0, bg = "#6781e0", highlightthickness = 0, font=text_font, justify="center", fg="#383A5A")
    entrypass0.config(show="*")
    entrypass0.insert(0, password1)
    entrypass0.place(x = 704.0, y = 152, width = 156.0, height = 38)
    
    global passwordone
    passwordone = entrypass0.get()

    global site1_label
    site1_label = Label(window6, text=site1, bg="#B0BBE3", font=label_font, fg="#202037")
    site1_label.place(x=65, y=155)
    
    global username1_label
    username1_label = Label(window6, text=username1, bg="#B0BBE3", font=label_font, fg="#202037")
    username1_label.place(x=445, y=155)
    
    global site2_label
    site2_label = Label(window6, text=site2, bg="#B0BBE3", font=label_font, fg="#202037")
    site2_label.place(x=65, y=240)
    
    global username2_label
    username2_label = Label(window6, text=username2, bg="#B0BBE3", font=label_font, fg="#202037")
    username2_label.place(x=445, y=240)

    global site3_label
    site3_label = Label(window6, text=site3, bg="#B0BBE3", font=label_font, fg="#202037")
    site3_label.place(x=65, y=320)
    
    global username3_label
    username3_label = Label(window6, text=username3, bg="#B0BBE3", font=label_font, fg="#202037")
    username3_label.place(x=445, y=320)

    global site4_label
    site4_label = Label(window6, text=site4, bg="#B0BBE3", font=label_font, fg="#202037")
    site4_label.place(x=65, y=400)
    
    global username4_label
    username4_label = Label(window6, text=username4, bg="#B0BBE3", font=label_font, fg="#202037")
    username4_label.place(x=445, y=400)
    
    global site5_label
    site5_label = Label(window6, text=site5, bg="#B0BBE3", font=label_font, fg="#202037")
    site5_label.place(x=65, y=480)
    
    global username5_label
    username5_label = Label(window6, text=username5, bg="#B0BBE3", font=label_font, fg="#202037")
    username5_label.place(x=445, y=480)

    d5()
    
    window6.resizable(False, False)
    window6.mainloop()

def hidepassc1():
    encrypted_password = aes_crypt(passwordone, key, 'encrypt')
    entrypass0.config(show="*")

    b6 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = showpassc1, relief = "flat")
    b6.place(x = 895, y = 147, width = 62, height = 42)
    with open('encrypted_file1.txt', 'w') as file:
        file.write(encrypted_password)

def showpassc1():
    with open('encrypted_file1.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass0.config(show="")
    entrypass0.delete(0, 'end')
    entrypass0.insert(0, decrypted_password)

    b6 = Button(image = showimg4, borderwidth = 0, highlightthickness = 0, command = hidepassc1, relief = "flat")
    b6.place(x = 895, y = 147, width = 62, height = 42)

def hidepassc2():
    encrypted_password = aes_crypt(passwordtwo, key, 'encrypt')
    entrypass1.config(show="*")

    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = showpassc2, relief = "flat")
    b3.place(x = 895, y = 230, width = 62, height = 42)
    with open('encrypted_file2.txt', 'w') as file:
        file.write(encrypted_password)
def showpassc2():
    with open('encrypted_file2.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass1.config(show="")
    entrypass1.delete(0, 'end')
    entrypass1.insert(0, decrypted_password)  
 
    b3 = Button(image = showimg3, borderwidth = 0, highlightthickness = 0, command = hidepassc2, relief = "flat")
    b3.place(x = 895, y = 230, width = 62, height = 42)
    
def hidepassc3():
    encrypted_password = aes_crypt(passwordthree, key, 'encrypt')
    entrypass2.config(show="*")

    b7 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = showpassc3, relief = "flat")
    b7.place(x = 895, y = 311, width = 62, height = 42)
    with open('encrypted_file3.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassc3():
    with open('encrypted_file3.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass2.config(show="")
    entrypass2.delete(0, 'end') 
    entrypass2.insert(0, decrypted_password) 
  
    b7 = Button(image = showimg5, borderwidth = 0, highlightthickness = 0, command = hidepassc3, relief = "flat")
    b7.place(x = 895, y = 311, width = 62, height = 42)
    

def hidepassc4():
    encrypted_password = aes_crypt(passwordfour, key, 'encrypt')
    entrypass3.config(show="*")

    b5 = Button(image = showimg6, borderwidth = 0, highlightthickness = 0, command = showpassc4, relief = "flat")
    b5.place(x = 895, y = 393, width = 62, height = 42)
    with open('encrypted_file4.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassc4():
    with open('encrypted_file4.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass3.config(show="")
    entrypass3.delete(0, 'end')
    entrypass3.insert(0, decrypted_password)
   
    b5 = Button(image = showimg6, borderwidth = 0, highlightthickness = 0, command = hidepassc4, relief = "flat")
    b5.place(x = 895, y = 393, width = 62, height = 42)
    
    
def hidepassc5():
    encrypted_password = aes_crypt(passwordfive, key, 'encrypt')
    entrypass4.config(show="*")

    b4 = Button(image = showimg7, borderwidth = 0, highlightthickness = 0, command = showpassc5, relief = "flat")
    b4.place(x = 895, y = 475, width = 62, height = 42)
    with open('encrypted_file5.txt', 'w') as file:
        file.write(encrypted_password)
    
def showpassc5():
    with open('encrypted_file5.txt', 'r') as file:
        encrypted_password = file.read()

    decrypted_password = aes_crypt(encrypted_password, key, 'decrypt')
    entrypass4.config(show="")
    entrypass4.delete(0, 'end')  
    entrypass4.insert(0, decrypted_password)
   
    b4 = Button(image = showimg7, borderwidth = 0, highlightthickness = 0, command = hidepassc5, relief = "flat")
    b4.place(x = 895, y = 475, width = 62, height = 42)
    
def add6():
    messagebox.showinfo("Password manager", "You have reached the limit of passwords can be saved on the beta program")

def otp():
    windowc.destroy()
    global otpwindow
    otpwindow = Tk()
    otpwindow.geometry("500x300")
    otpwindow.title("Password manager")
    otpwindow.configure(bg = "#202037")
    otpwindow.iconbitmap("icon.ico")

    canvas = Canvas(otpwindow, bg = "#202037", height = 300, width = 500, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    global otp_entry
    otp_entry_img = PhotoImage(file = f"otpimg_textBox0.png")
    otp_entry_bg = canvas.create_image(363.0, 141.0, image = otp_entry_img)
    otp_entry = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, font=top_text_font)
    otp_entry.place(x = 262.0, y = 121, width = 202.0, height = 38)

    img0 = PhotoImage(file = f"otpimg0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = otp_verify, relief = "flat")
    b0.place(x = 181, y = 227, width = 137, height = 40)
    
    background_img = PhotoImage(file = f"otpbackground.png")
    background = canvas.create_image(203.5, 90.5, image=background_img)

    otpwindow.resizable(False, False)
    otpwindow.mainloop()

def otp_verify():
    key = "PasswordManagerMySuperSecretKey"
    uri = pyotp.totp.TOTP(key).provisioning_uri(name = "Yousef", issuer_name="Password Manager")
    qrcode.make(uri).save("totp.png")
    otp = otp_entry.get()
    totp = pyotp.TOTP(key)
    if (totp.verify(otp)) == True:
        password_saved()
    else:
        messagebox.showerror("Password manager", "The 2FA OTP is not correct")
        
def password_saved():
    if inspect.stack()[1][3] == "remove_data":
        pass
    elif inspect.stack()[1][3] == "otp_verify":
        otpwindow.destroy()
    else:
        windowc.destroy()
    global window1
    window1 = Tk()
    window1.title("Password manager")
    window1.geometry("1000x600")
    window1.configure(bg = "#202037")
    window1.iconbitmap("icon.ico")

    canvas = Canvas(window1, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background1.png")
    background = canvas.create_image(499.0, 108.5, image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command=destroy1, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, relief = "flat")
    b1.place(x = 501, y = 0, width = 499,height = 80)

    img2 = PhotoImage(file = f"img2.png")
    plus1 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = add1, relief = "flat")
    plus1.place(x = 448, y = 542, width = 101, height = 42)

    importpassword()

    window1.resizable(False, False)
    window1.mainloop()

        
def importpassword():
    global l
    l=[]
    try:
        with open('C:/Users/youse/Desktop/d.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if ' , ' in line:
                    value = line.strip().split(' , ')
                    l.extend(value)
            if len(l) < 4:
                global site1 ,username1, password1
                site1 = l[0]
                username1 = l[1]
                password1 = l[2]
                add1()
            elif 3 < len(l) < 7:
                global site2 ,username2 ,password2
                site1 = l[0]
                username1 = l[1]
                password1 = l[2]
                site2 = l[3]
                username2 = l[4]
                password2 = l[5]
                add2()
            elif 6 < len(l) < 10:
                global site3 ,username3 ,password3
                site1 = l[0]
                username1 = l[1]
                password1 = l[2]
                site2 = l[3]
                username2 = l[4]
                password2 = l[5]
                site3 = l[6]
                username3 = l[7]
                password3 = l[8]
                add3()
            elif 6 < len(l) < 10:
                global site4 ,username4 ,password4
                site1 = l[0]
                username1 = l[1]
                password1 = l[2]
                site2 = l[3]
                username2 = l[4]
                password2 = l[5]
                site3 = l[6]
                username3 = l[7]
                password3 = l[8]
                site4 = l[9]
                username4 = l[10]
                password4 = l[11]
                add4()
            else:
                global site5 ,username5 ,password5
                site1 = l[0]
                username1 = l[1]
                password1 = l[2]
                site2 = l[3]
                username2 = l[4]
                password2 = l[5]
                site3 = l[6]
                username3 = l[7]
                password3 = l[8]
                site4 = l[9]
                username4 = l[10]
                password4 = l[11]
                site5 = l[12]
                username5 = l[13]
                password5 = l[14]
                add5()
    except:
        pass

def destroy1():
    window1.destroy()
    check()
    
def destroy2():
    window2.destroy()
    check()
    
def destroy3():
    window3.destroy()
    check()
    
def destroy4():
    window4.destroy()
    check()
    
def destroy5():
    window5.destroy()
    check()
    
def destroy6():
    window6.destroy()
    check()
        
def d1():
    with open("C:/Users/youse/Desktop/d.txt", "w") as f:
        f.write(site1+" , "+username1+" , "+passwordone+"\n")

def d2():
    with open("C:/Users/youse/Desktop/d.txt", "w") as f:
        f.write(site1+" , "+username1+" , "+passwordone+"\n")
        f.write(site2+" , "+username2+" , "+passwordtwo+"\n")
        
def d3():
    with open("C:/Users/youse/Desktop/d.txt", "w") as f:
        f.write(site1+" , "+username1+" , "+passwordone+"\n")
        f.write(site2+" , "+username2+" , "+passwordtwo+"\n")
        f.write(site3+" , "+username3+" , "+passwordthree+"\n")

def d4():
    with open("C:/Users/youse/Desktop/d.txt", "w") as f:
        f.write(site1+" , "+username1+" , "+passwordone+"\n")
        f.write(site2+" , "+username2+" , "+passwordtwo+"\n")
        f.write(site3+" , "+username3+" , "+passwordthree+"\n")
        f.write(site4+" , "+username4+" , "+passwordfour+"\n")

def d5():
    with open("C:/Users/youse/Desktop/d.txt", "w") as f:
        f.write(site1+" , "+username1+" , "+passwordone+"\n")
        f.write(site2+" , "+username2+" , "+passwordtwo+"\n")
        f.write(site3+" , "+username3+" , "+passwordthree+"\n")
        f.write(site4+" , "+username4+" , "+passwordfour+"\n")
        f.write(site5+" , "+username5+" , "+passwordfive+"\n")

def save_data1():
    with open("cloud.txt", "w") as f:
        f.write("----------------------------------\n"+"site : "+site1+"\n"+"Username : "+username1)
        encrypted_password = aes_crypt(passwordone, key, 'encrypt')
        with open("encrypted_file1.txt", "w") as f:
            f.write(encrypted_password)
    global files_to_append
    files_to_append = [
        'encrypted_file1.txt',
    ]
    append_text_files(files_to_append)
        
def save_data2():
    with open("cloud.txt", "w") as f:
        f.write("----------------------------------\n"+"site : "+site1+"\n"+"Username : "+username1)
        f.write("\n----------------------------------\n"+"site : "+site2+"\n"+"Username : "+username2)
        encrypted_password = aes_crypt(passwordtwo, key, 'encrypt')
        with open("encrypted_file2.txt", "w") as f:
            f.write(encrypted_password)
    global files_to_append            
    files_to_append = [
        'encrypted_file1.txt',
        'encrypted_file2.txt',
    ]
    append_text_files(files_to_append)

def save_data3():
    with open("cloud.txt", "w") as f:
        f.write("----------------------------------\n"+"site : "+site1+"\n"+"Username : "+username1)
        f.write("\n----------------------------------\n"+"site : "+site2+"\n"+"Username : "+username2)
        f.write("\n----------------------------------\n"+"site : "+site3+"\n"+"Username : "+username3)
        encrypted_password = aes_crypt(passwordthree, key, 'encrypt')
        with open("encrypted_file3.txt", "w") as f:
            f.write(encrypted_password)
    global files_to_append
    files_to_append = [
        'encrypted_file1.txt',
        'encrypted_file2.txt',
        'encrypted_file3.txt',
    ]
    append_text_files(files_to_append)
    
def save_data4():
    with open("cloud.txt", "w") as f:
        f.write("----------------------------------\n"+"site : "+site1+"\n"+"Username : "+username1)
        f.write("\n----------------------------------\n"+"site : "+site2+"\n"+"Username : "+username2)
        f.write("\n----------------------------------\n"+"site : "+site3+"\n"+"Username : "+username3)
        f.write("\n----------------------------------\n"+"site : "+site4+"\n"+"Username : "+username4)
        encrypted_password = aes_crypt(passwordfour, key, 'encrypt')
        with open("encrypted_file4.txt", "w") as f:
            f.write(encrypted_password)
    global files_to_append
    files_to_append = [
        'encrypted_file1.txt',
        'encrypted_file2.txt',
        'encrypted_file3.txt',
        'encrypted_file4.txt',
    ]
    append_text_files(files_to_append)
    
def save_data5():
    with open("cloud.txt", "w") as f:
        f.write("----------------------------------\n"+"site : "+site1+"\n"+"Username : "+username1)
        f.write("\n----------------------------------\n"+"site : "+site2+"\n"+"Username : "+username2)
        f.write("\n----------------------------------\n"+"site : "+site3+"\n"+"Username : "+username3)
        f.write("\n----------------------------------\n"+"site : "+site4+"\n"+"Username : "+username4)
        f.write("\n----------------------------------\n"+"site : "+site5+"\n"+"Username : "+username5)
        encrypted_password = aes_crypt(passwordfive, key, 'encrypt')
        with open("encrypted_file5.txt", "w") as f:
            f.write(encrypted_password)
    global files_to_append
    files_to_append = [
        'encrypted_file1.txt',
        'encrypted_file2.txt',
        'encrypted_file3.txt',
        'encrypted_file4.txt',
        'encrypted_file5.txt',
    ]
    append_text_files(files_to_append)
    
def pad(data):
    padding_size = BLOCKSIZE - (len(data) % BLOCKSIZE)
    padding = bytes([padding_size]) * padding_size
    return data + padding

def unpad(data):
    padding_size = data[-1]
    
    if padding_size > BLOCKSIZE:
        raise ValueError("Input data is not padded or padding is corrupt")
    return data[:-padding_size]

def aes_crypt(password, key, mode):
    cipher = AES.new(key, AES.MODE_CBC)

    if mode == 'encrypt':
        padded_password = pad(password.encode())
        encrypted_password = cipher.encrypt(padded_password)
        return b64encode(cipher.iv + encrypted_password).decode('utf-8')
    elif mode == 'decrypt':
        data = b64decode(password)
        iv = data[:16]
        encrypted_password = data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted_password = cipher.decrypt(encrypted_password)
        unpadded_password = unpad(decrypted_password)
        return unpadded_password.decode('utf-8')
    else:
        raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")
        
def remove_data1():
    window2.destroy()
    remove_data()

def remove_data2():
    window3.destroy()
    remove_data()

def remove_data3():
    window4.destroy()
    remove_data()

def remove_data4():
    window5.destroy()
    remove_data()
    
def remove_data5():
    window6.destroy()
    remove_data()

def remove_data():
    with open("cloud.txt", "w") as f:
        f.write("")
    with open("C:/Users/youse/Desktop/d.txt", "w") as f:
        f.write("")
    password_saved()

def append_text_files(file_paths):
    try:
        with open("encrypted_file.txt", 'a') as output:
            for file_path in file_paths:
                with open(file_path, 'r') as input_file:
                    content = input_file.read()
                    output.write(content)
                    output.write('\n')
    except Exception as e:
        print(f"An error occurred: {e}")
    local_file_path = 'encrypted_file.txt'
    upload_to_fileio(local_file_path)

def upload_to_fileio(file_path):
    try:
        with open(file_path, 'rb') as file:
            response = requests.post('https://file.io', files={'file': file})
            if response.status_code == 200:
                response_data = response.json()
                file_url = response_data.get('link')
                with open("cloud.txt", "w") as f:
                    f.write("File uploaded successfully. You can download it from: "+file_url)
                    messagebox.showinfo("Password manager", "Saved Successfully to the cloud")
            else:
                messagebox.showerror("Password manager", "Failed to upload file. Status code:"+response.status_code)
    except FileNotFoundError:
        messagebox.showerror("Password manager", "There no file to be uploaded")

def check():
    global windowc
    windowc = Tk()
    windowc.title("Password manager")
    windowc.geometry("1000x600")
    windowc.configure(bg = "#202037")
    text_font = Font(family="Helvetica", size=16)
    windowc.iconbitmap("icon.ico")

    canvas = Canvas(windowc, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file = f"img0p1.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, relief = "flat")
    b0.place(x = 0, y = 0, width = 499, height = 80)

    img1 = PhotoImage(file = f"img1p1.png")
    b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = generate_password, relief = "flat")
    b1.place(x = 361, y = 179, width = 206, height = 60)

    img2 = PhotoImage(file = f"img2p1.png")
    b2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = check_password, relief = "flat")
    b2.pack()
    b2.place(x = 738, y = 452, width = 206, height = 60)
    
    img3 = PhotoImage(file = f"img3p1.png")
    b3 = Button(image = img3, borderwidth = 0, highlightthickness = 0, command = otp, relief = "flat")
    b3.place(x = 501, y = 0, width = 499, height = 80)
    
    initial_password = password_generator(10)
    global password_label
    password_label = Label(windowc, text=initial_password, bg="#202037", font=label_font, fg="#202037")
    password_label.place(x=700, y=196)
    
    global entry2
    entry2_img = PhotoImage(file = f"img_textBox1p1.png")
    entry2_bg = canvas.create_image(771.5, 368.5, image = entry2_img)
    entry2 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#4F517D", font=temp_text_font)
    entry2.insert(0, 'Enter Password Here')
    entry2.place(x = 611.0, y = 338, width = 321.0, height = 59)
    entry2.bind("<FocusIn>", temp_checker)
    
    global result_label
    result_label = Label(windowc, text="", bg="#202037", font=text_font, fg="#B0BBE3")
    result_label.place(x=560, y=465)

    background_img = PhotoImage(file = f"backgroundp1.png")
    background = canvas.create_image(273.0, 288.5, image=background_img)

    windowc.resizable(False, False)
    windowc.mainloop()

def temp_checker(e):
   entry2.delete(0,"end")
   entry2.config(fg="#383A5A", font=text_font)
   
def on_login_button_clicked(entry1, entry0):
    username = entry1.get()
    password = entry0.get()
    if check_login(username, password):
        window.destroy()
        global windowc
        windowc = Tk()
        windowc.title("Password manager")
        windowc.geometry("1000x600")
        windowc.configure(bg = "#202037")
        windowc.iconbitmap("icon.ico")
    
        canvas = Canvas(windowc, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        img0 = PhotoImage(file = f"img0p1.png")
        b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, relief = "flat")
        b0.place(x = 0, y = 0, width = 499, height = 80)

        img1 = PhotoImage(file = f"img1p1.png")
        b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = generate_password, relief = "flat")
        b1.place(x = 361, y = 179, width = 206, height = 60)

        img2 = PhotoImage(file = f"img2p1.png")
        b2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = check_password, relief = "flat")
        b2.pack()
        b2.place(x = 738, y = 452, width = 206, height = 60)

        img3 = PhotoImage(file = f"img3p1.png")
        b3 = Button(image = img3, borderwidth = 0, highlightthickness = 0, command = otp, relief = "flat")
        b3.place(x = 501, y = 0, width = 499, height = 80)

        initial_password = password_generator(10)
        global password_label
        password_label = Label(windowc, text=initial_password, bg="#202037", font=label_font, fg="#202037")
        password_label.place(x=700, y=196)
        
        global entry2
        entry2_img = PhotoImage(file = f"img_textBox1p1.png")
        entry2_bg = canvas.create_image(771.5, 368.5, image = entry2_img)
        entry2 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#4F517D", font=temp_text_font)
        entry2.insert(0, 'Enter Password Here')
        entry2.place(x = 611.0, y = 338, width = 321.0, height = 59)
        entry2.bind("<FocusIn>", temp_checker)
        
        global result_label
        result_label = Label(windowc, text="", bg="#202037", font=text_font, fg="#B0BBE3")
        result_label.place(x=560, y=465)

        background_img = PhotoImage(file = f"backgroundp1.png")
        background = canvas.create_image(273.0, 288.5, image=background_img)

        windowc.resizable(False, False)
        windowc.mainloop()
    else:
        messagebox.showerror("Login", "Invalid username or password")
        entry1.delete(0 ,'end')
        entry0.delete(0 ,'end')

def temp_username(e):
   entry1.delete(0,"end")
   entry1.config(fg="#383A5A", font=text_font)
   
def temp_password(e):
   entry0.delete(0,"end")
   entry0.config(fg="#383A5A", font=text_font)
   entry0.config(show="*")
   
window = Tk()
window.title("Password manager")
window.geometry("1000x600")
window.configure(bg = "#202037")
window.iconbitmap("icon.ico")
temp_text_font = Font(family="Helvetica", size=13)
text_font = Font(family="Helvetica", size=13, weight="bold")
label_font = Font(family="Helvetica", size=30, weight="bold")
top_text_font = Font(family="Helvetica", size=1)

canvas = Canvas(window, bg = "#202037", height = 600, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"backgroundLOGIN.png")
background = canvas.create_image(435.0, 300.0, image=background_img)

img0 = PhotoImage(file = f"img0LOGIN.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command=lambda: on_login_button_clicked(entry1, entry0), relief = "flat")
b0.place(x = 675, y = 468, width = 180, height = 55)

entry0_img = PhotoImage(file = f"img_textBox0LOGIN.png")
entry0_bg = canvas.create_image(760.5, 387.5, image = entry0_img)
entry0 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#4F517D", font=temp_text_font)
entry0.insert(0, 'Ex: Password')
entry0.place(x = 600.0, y = 357, width = 321.0, height = 59)
entry0.bind("<FocusIn>", temp_password)

img1 = PhotoImage(file = f"img1LOGIN.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = show, relief = "flat")
b1.place(x = 891, y = 357,width = 54,height = 61)

entry1_img = PhotoImage(file = f"img_textBox1LOGIN.png")
entry1_bg = canvas.create_image(760.5, 265.5, image = entry1_img)
entry1 = Entry(bd = 0, bg = "#b0bbe3", highlightthickness = 0, fg="#4F517D", font=temp_text_font)
entry1.insert(0, 'Ex: Ahmed')
entry1.place(x = 600.0, y = 235, width = 321.0, height = 59)
entry1.bind("<FocusIn>", temp_username)

window.bind('<Return>', key_return)

key = get_random_bytes(32)
BLOCKSIZE = 16

window.resizable(False, False)
window.mainloop()