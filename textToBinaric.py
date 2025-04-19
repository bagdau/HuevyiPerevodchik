import customtkinter as ctk

def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def convert_text():
    input_text = input_entry.get()
    if input_text.strip():
        binary_result = text_to_binary(input_text)
        output_textbox.delete("1.0", ctk.END)
        output_textbox.insert(ctk.END, binary_result)
    else:
        output_textbox.delete("1.0", ctk.END)
        output_textbox.insert(ctk.END, "Какой блядь ваше любимый слово? Введите его туда.")

app = ctk.CTk()
app.title("Короче непонятный переводчик непонятного кода")
app.geometry("500x400")

input_label = ctk.CTkLabel(app, text="Баха сказал: Ввести текст", font=("Arial", 14))
input_label.pack(pady=10)

input_entry = ctk.CTkEntry(app, width=400, font=("Arial", 14))
input_entry.pack(pady=10)

convert_button = ctk.CTkButton(app, text="Начнем нахой", command=convert_text)
convert_button.pack(pady=20)

output_label = ctk.CTkLabel(app, text="Непонятный презентация:", font=("Arial", 14))
output_label.pack(pady=10)

output_textbox = ctk.CTkTextbox(app, width=400, height=150, font=("Courier", 12))
output_textbox.pack(pady=10)

app.mainloop()