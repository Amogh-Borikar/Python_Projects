import tkinter

my_window = tkinter.Tk()
my_window.title("Mile to Km converter")
my_window.config(padx=20, pady=20)

def convert_M_to_Km():
    miles = mile_input_entry.get()
    km = float(miles) * 1.609
    Km_result.config(text=f"{km}")


mile_input_entry = tkinter.Entry(width=10)
mile_input_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

Km_result = tkinter.Label(text="0")
Km_result.grid(column=1, row=1)

Km_label = tkinter.Label(text="Km")
Km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=convert_M_to_Km)
calculate_button.grid(column=1, row=2)

my_window.mainloop()