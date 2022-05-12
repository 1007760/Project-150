from tkinter import *
import random
root = Tk()
root.title("Random Country")
root.geometry("500x500")
country_input = Entry(root)
country_input.place(relx = 0.5, rely = 0.2, anchor = CENTER)
capital_input = Entry(root)
capital_input.place(relx = 0.5, rely = 0.3, anchor = CENTER)
country_label = Label(root)
country_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
capital_label = Label(root)
capital_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
random_country = Label(root)
random_country.place(relx = 0.5, rely = 0.7, anchor = CENTER)
random_city = Label(root)
random_city.place(relx = 0.5, rely = 0.8, anchor = CENTER)
country_list = []
capital_list = []

def add_Input() :
    enter_name1 = country_input.get()
    country_list.append(enter_name1)
    country_label["text"] = "Country name is : " + str(country_list)
    enter_name2 = capital_input.get()
    capital_list.append(enter_name2)
    capital_label["text"] = "City name is : " + str(capital_list)
    
def random_Number() :
    length1 = len(country_list)
    random_number1 = random.randint(0,length1-1)
    country_random1 = country_list[random_number1]
    random_country["text"] = "Random country is : " + str(country_random1)
    length2 = len(capital_list)
    random_number2 = random.randint(0,length2-1)
    capital_random1 = capital_list[random_number2]
    random_city["text"] = "Random capital is : " + str(capital_random1)
    
btn1 = Button(root, text = "Input Names", command = add_Input)
btn1.place(relx = 0.5, rely = 0.9, anchor = CENTER)
btn2 = Button(root, text = "Randomize Names", command = random_Number)
btn2.place(relx = 0.5, rely = 1.0, anchor = CENTER)
root.mainloop()