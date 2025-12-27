from guizero import App, Text, TextBox, Combo, PushButton, info
import os
def do_action():
    match what_action.value:
        case "Lưu":
            with open("data.txt", "w", encoding = "utf-8") as file:
                file.write(save_text.value)
        case "Đọc":
            if os.path.exists("data.txt"):
                with open("data.txt", "r", encoding = "utf-8") as file:
                    content = file.read()
                save_text.value = content
            else:
                info("Thông báo", "Vui lòng tạo file!")
        case "Xóa":
            if os.path.exists("data.txt"):
                with open("data.txt", "w", encoding = "utf-8") as file:
                    file.write("")
                    save_text.clear()
            else:
                info("Thông báo", "Vui lòng tạo file!")
app = App(title = "Thực hành match-case", layout = "grid")
Text(app, grid = [0,0], text = "Dữ liệu lưu: ")
save_text = TextBox(app, grid = [1,0], width = 50, height = 1)
Text(app, grid = [0,1], text = "Hành động: ")
what_action = Combo(app, grid = [1,1], options = ["Lưu", "Đọc", "Xóa"], selected = "Lưu")
do_action_button = PushButton(app, grid = [1,2], text = "Thực hiện", command = do_action)
Text(app, grid = [0,3], text = "Kết quả: ")
file_result = Text(app, grid = [1,3], text = "")

app.display()