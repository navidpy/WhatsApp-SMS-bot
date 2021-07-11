from tkinter import *
import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

window = Tk()
window.resizable(False, False)
window.geometry('300x350')
window.title("whatsapp sms")


def exit_app():
    driver.close()
    window.destroy()


def start():
    text1 = a.get()
    num = int(sp.get())
    vales = [lb.get(i) for i in lb.curselection()]
    for i in vales:
        user = driver.find_element_by_xpath(f'//span[@title="{i}"]')
        user.click()
        time.sleep(2)
        text = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        for j in range(num):
            text.click()
            text.send_keys(text1)
            text.send_keys(Keys.ENTER)


lbl = Label(window, text="whatsapp sms bot", fg="red", bg="yellow", font=('tahoma', 23, "bold"))
lbl.place(x=4, y=4)

btn = Button(window, text="        Exit        ", font=('tahoma', 10, "bold"), fg='red'
             , command=exit_app, cursor='hand2', bd=6)
btn.place(x=8, y=308)
start = Button(window, text="              Start               ", font=('tahoma', 10, "bold"), fg='blue'
               , command=start, cursor='hand2', bd=6)
start.place(x=120, y=308)

L1 = Label(window, text="Enter your message :", font=('tahoma', 9, "bold"))
L1.place(x=1, y=65)
a = Entry(window, fg='blue', bd=4, font=('tahoma', 9, "bold"))
a.place(x=129, y=65)
L1 = Label(window, text="Enter number :", font=('tahoma', 9, "bold"))
L1.place(x=15, y=105)
sp = Spinbox(window, from_=0, to=100, bd=4, font=('tahoma', 8, "bold"), fg='purple')
sp.place(x=125, y=105)

L1 = Label(window, text="Enter your message :", font=('tahoma', 9, "bold"))
L1.place(x=1, y=190)
lb = Listbox(window, font=('tahoma', 8, "bold"), bd=4)
lb.config(selectmode='multiple')
lb.place(x=134, y=140)

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
ad = WebDriverWait(driver, 10000).until(EC.presence_of_element_located(
    (By.XPATH, '//span[@dir="auto"]')))
time.sleep(1)
main = driver.find_elements_by_xpath('//span[@dir="auto"]')
b = [l.get_attribute('title') for l in main]
time.sleep(3)
for i in b:
    if i != "":
        lb.insert(END, i)

window.mainloop()
