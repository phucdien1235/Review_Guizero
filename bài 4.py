from guizero import App, Text, PushButton, ListBox
import os
def show_file():
    lst_file_txt.clear()
    lst_txt = os.listdir(".")
    for x in lst_txt:
        if os.path.isfile(x) and x.endswith(".txt"):
            lst_file_txt.append(x)
app = App(title = "Liệt kê các file txt", height = 300, width = 200)
show_file_button = PushButton(app, text = "Liệt kê các file .txt", command = show_file)
Text(app, text = "Kết quả:")
lst_file_txt = ListBox(app, items = [])
lst_file_txt.bg = "lightgreen"

app.display()