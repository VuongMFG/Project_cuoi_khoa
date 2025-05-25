import tkinter
from datetime import datetime
from PIL import Image, ImageTk
import os
import ctypes

# Creat main window
root = tkinter.Tk()
root.title("Hướng dẫn làm việc")
root.geometry("900x600")  
# Creat input box
label_line = tkinter.Label(root, text="Line")
label_line.place(x = 20, y = 10)
input_box_line = tkinter.Entry(root)
input_box_line.place(x =20, y=40)
label_process = tkinter.Label(root, text="Process")
label_process.place(x = 200, y = 10)
input_box_process = tkinter .Entry(root)
input_box_process.place(x=200, y=40)

# Main function

# Read config file for log path
def main():
    with open("config.txt", mode= "r", newline="", encoding="utf-8") as config:
        path = config.read()
        # Open log 
    now = datetime.now()
    now_str = now.strftime("%Y%m%d")
    with open("{}\\MES_{}.txt".format(path,now_str), "r") as log:
        lines = log.readlines()
    keyword = "Model"
    for line in reversed(lines):
        if keyword in line:
            try:
                model_name = line[6]
            except ValueError:
                print("Chưa có HDLV")
            break
    # Update new image    
    global photo  
    try:
        path = f"C:/Users/Administrator/Desktop/Working_Instruction_Image/{input_box_line.get()}/{input_box_process.get()}/{model_name}.png"
        if os.path.exists(path):
            img2 = Image.open(path)
            img2 = img2.resize((800, 500))
            photo = ImageTk.PhotoImage(img2)
            wi.config(image=photo)
        else:
            wi.config(image='',text="Chưa có HDLV", font=("Arial",16,"bold"))
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, "Lỗi hệ thống", "Thông báo", 0)
    root.after(1000,main) # run main fuction in loop

# Init image window
img1 = Image.open("image.png")
img1 = img1.resize((800, 500))
photo = ImageTk.PhotoImage(img1)
wi = tkinter.Label(root,image=photo)
wi.place(x=50, y= 100)
# Start button
button = tkinter.Button(root, text="START", command=main)
button.pack(pady=10)
root.mainloop()