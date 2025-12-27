from guizero import App, Text, TextBox, PushButton, Box
import os
def save():
    with open("info.txt", "w", encoding = "utf-8") as file:
        file.write(what_information.value)
    check_how_file()
def read():
    try:
        with open("info.txt", "r", encoding = "utf-8") as file:
            content = file.read()
        what_information.value = content
    except FileNotFoundError:
        pass
def check_how_file():
    if "info.txt" not in os.listdir("."):
        how_file.value = "Tình trạng hiện tại của file: Không tồn tại"
    else:
        how_file.value = "Tình trạng hiện tại của file: Tồn tại"
app = App(title = "Lưu và đọc file", height = 250)
Text(app, text = "Nội dung:")
what_information = TextBox(app, text = "Nhập ở đây", multiline = True, height = 5, width = 60, command = check_how_file)
box_button = Box(app, width = 500, height = 50)
Text(box_button, text = "                                           ", align = "left")
save_button = PushButton(box_button, text = "Save file", command = save, align = "left")
read_button = PushButton(box_button, text = "Read file", command = read, align = "left")
how_file = Text(app, text = "Tình trạng hiện tại của file: ...")

app.display()