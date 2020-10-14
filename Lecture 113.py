from forex_python.converter import CurrencyRates
from tkinter import *
from datetime import *



print(datetime.now)


def show_table(event):
    c = CurrencyRates()
    cur_from = "THB"
    dict_currency = c.get_rates(cur_from)
    #print(dict_currency)

    input_amount = float(textbox_input_currency.get())

    r = 2 #Start row for label currency

    for cur in sorted(dict_currency):
        if cur != cur_from:
            convert_amount = round(c.convert(cur_from, cur, input_amount), 2)
            corvertion_rate = round(c.get_rate(cur_from, cur), 2)

            Label(main_window, text =str(cur)).grid(row = r, column = 0)        
            Label(main_window, text = convert_amount).grid(row = r, column = 1)
            Label(main_window, text = corvertion_rate).grid(row = r, column = 2)


            r += 1


### GUI ###
main_window = Tk()

label_input_currency = Label(main_window, text = "ใส่จำนวนเงิน THB : ")
label_input_currency.grid(row = 0, column = 0)

textbox_input_currency = Entry(main_window)
textbox_input_currency.grid(row = 0, column = 1)

button_convert_currency = Button(main_window, text = "คำนวณ")
button_convert_currency.grid(row = 0, column = 2)
button_convert_currency.bind('<Button-1>', show_table)

label_header1 = Label(main_window, text = "Currency")
label_header1.grid(row = 1, column = 0)
label_header2 = Label(main_window, text = "Converted Amount")
label_header2.grid(row = 1, column = 1)
label_header3 = Label(main_window, text = "Rate")
label_header3.grid(row = 1, column = 2)

main_window.mainloop()
### GUI ###


