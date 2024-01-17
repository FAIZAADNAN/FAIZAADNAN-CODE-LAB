from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk #importing Image and ImageTk module from the python library
import json #importing json module for working json data
import requests # Importing requests module for making HTTP requests

window = Tk() # Creating the main Tkinter window
# Defining color constants for the application using hexadecimal color codes
colour0 = "#4682B4"  # SteelBlue 
colour1 = "#F0F8FF"  # AliceBlue
colour2 = "#1E90FF"  # DodgerBlue

window.geometry("1050x600") # Setting the size of the window
window.title("Currency Converter App") # Setting the title of the window 
window.configure(bg=colour0)  # Configuring the background color of the window to SteelBlue
window.resizable(0, 0) # Making the window non-resizable in height and width

top = Frame(window, width=1050, height=60, bg=colour2)# Creating a Frame widget for the top section of the window
top.grid(row=0, column=0) # Placing the top frame in the first row and column of the grid

main = Frame(window, width=1050, height=600, bg=colour0) # Frame with width 1050, height 600, and SteelBlue background
main.grid(row=1, column=0)# Placing the main frame in the second row and column of the grid

image = Image.open("b2.jpg")# Opening an image file using the PIL library
resize_image = image.resize((1050, 600)) # Resizing the image to fit the dimensions of the main content section

bg_img2 = ImageTk.PhotoImage(resize_image) # Converting the resized image to a Tkinter-compatible format

bg_image_label1 = Label(main, image=bg_img2) # Creating a Label widget in the 'main' frame to display the resized image
bg_image_label1.place(x=0, y=0) # Placing the Label widget at the top-left corner (coordinates 0, 0) of the 'main' frame


def convert(): # API endpoint for currency conversion
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    # Getting selected currencies from the ComboBox widgets
    currency_1 = combo1.get()  # Currency to convert from
    currency_2 = combo2.get()
    # Getting the amount to convert from the Entry widget
    amount = value.get()
    # Constructing the query parameters for the API request
    querystring = {"from": currency_1, "to": currency_2, "amount": amount}
    # Checking the target currency and assigning its symbol
    if currency_2 == "USD": # United States Dollar symbol
        symbol = "$"
    elif currency_2 == "PKR":
        symbol = "Rs"  # Pakistani Rupee symbol
    elif currency_2 == "EURO":
        symbol = "€" # Euro symbol
    elif currency_2 == "BRL":
        symbol = "R$"  # Brazilian Real symbol
    elif currency_2 == "CAD":
        symbol = "CA $" # Canadian Dollar symbol

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com", # RapidAPI host for the currency converter API
        'x-rapidapi-key': "5c33565547msh83e120ea3a45d4ep10ef35jsndb46a2b63215" # RapidAPI key for authentication
    }
    # Making a GET request to the currency converter API with specified headers and query parameters
    response = requests.request("GET", url, headers=headers, params=querystring)
    #JSON response to extract conversion data
    data = json.loads(response.text)
    # Extracting the converted amount from the JSON data
    converted_amount = data["result"]["convertedAmount"]
    # Formatting the converted amount with the currency symbol and two decimal places
    formatted = symbol + "{:,.2f}".format(converted_amount)
    # Displaying the formatted result
    result["text"] = formatted


# Top frame
# Opening the logo image using the PIL library
logo = Image.open("icon2.png")
# Resizing the logo image to dimensions (40, 40)
logo = logo.resize((40, 40))

# Converting the resized logo image to a Tkinter  format
logo = ImageTk.PhotoImage(logo)
# Creating a Label widget in the 'top' frame to display the application name and logo
app_name = Label(top, image=logo, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=30,
                 anchor=CENTER, font=("Arial 16 bold"), bg=colour2, fg=colour0)
app_name.place(x=0, y=0)

# Main frame

# List of available currencies
currency = ["PKR", "CAD", "BRL", "USD", "EUR"]

# Creating a Label widget in the 'main' frame for the "From" label
label2 = Label(main, text="From", width="8", height=1, pady=0, padx=0, relief="flat", anchor=NW,
               font=("Arial 10 bold"), bg=colour0, fg=colour1)
# Placing the "From" label at the specified coordinates (350, 200) in the 'main' frame
label2.place(x=350, y=200)
# Creating a Combobox widget in the 'main' frame for selecting the "From" currency
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Arial 12 bold"))
# Setting the values for the Combobox from the 'currency' list
combo1["values"] = (currency)
# Placing the Combobox at the specified coordinates (330, 250) in the 'main' frame
combo1.place(x=330, y=250)
# Creating a Label widget in the 'main' frame for the "To" label
to_label = Label(main, text="To", width="8", height=1, pady=0, padx=0, relief="flat", anchor=NW,
                 font=("Arial 10 bold"), bg=colour0, fg=colour1)
# Placing the "To" label at the specified coordinates (600, 200) in the 'main' frame
to_label.place(x=600, y=200)
# Creating a Combobox widget in the 'main' frame for selecting the "To" currency
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Arial 12 bold"))
# Setting the values for the Combobox from the 'currency' list
combo2["values"] = (currency)
# Placing the Combobox at the specified coordinates (590, 250) in the 'main' frame
combo2.place(x=590, y=250)

# Creating an Entry widget in the 'main' frame for entering the amount to convert
value = Entry(main, width=30, justify=CENTER, font=("Arial 12 bold"), relief=SOLID)
# Placing the Entry widget at the specified coordinates (400, 290) in the 'main' frame
value.place(x=400, y=290)
# Creating a Button widget in the 'main' frame for triggering the currency conversion
button = Button(main, text="Convert", width=25, padx=5, height=1, bg=colour2, fg=colour0,
                font=("Arial 12 bold"), command=convert)
# Placing the Button at the specified coordinates (400, 330) in the 'main' frame
button.place(x=400, y=330)
# Creating a Label widget in the 'main' frame for displaying the conversion result
result = Label(main, text="", width=20, height=2, pady=7, relief="solid", anchor=CENTER,
               font=("Arial 15 bold"), bg=colour0, fg=colour1)
# Placing the Label at the specified coordinates (400, 420) in the 'main' frame
result.place(x=400, y=420)

window.mainloop()