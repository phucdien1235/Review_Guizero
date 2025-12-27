from guizero import App, Text, TextBox, Box, ButtonGroup, PushButton, Combo, info
def show():
    if name.value != "":
        text_name.value = f"Họ và tên: {name.value}"
        text_class.value = f"Lớp: {choose_class.value}"
        text_gt.value = f"Giới tính: {choose_gt.value}"
    else:
        info("Thông báo", "Bạn nên nhập tên của bản thân")
        return
app = App(title = "Thông tin cá nhân", height = 350)
box_name = Box(app, width = 500, height = 50, align = "top")
Text(box_name, text = "Họ và tên: ", size = 15, color = "black", align = "left")
name = TextBox(box_name, width = 50, height = 1, align = "left")
box_class = Box(app, width = 500, height = 50, align = "top")
Text(box_class, text = "Lớp:        ", size = 15, color = "black", align = "left")
choose_class = Combo(box_class, options = ["7A", "7B", "7C"], align = "left", width = 10)
box_gt = Box(app, width = 500, height = 50, align = "top")
Text(box_gt, text = "Giới tính:     ", size = 15, color = "black", align = "left")
choose_gt = ButtonGroup(box_gt, options = ["Nam", "Nữ"], align = "left", horizontal = True, width = 10)
show_button = PushButton(app, text = "Hiển thị", command = show)
box_show = Box(app, width = 500, height = 155, align = "top", layout = "grid")
text_name = Text(box_show, text = "Họ và tên: ...", size = 20, color = "black", grid = [0,0])
text_class = Text(box_show, text = "Lớp: ...", size = 20, color = "black", grid = [0,1])
text_gt = Text(box_show, text = "Giới tính: ...", size = 20, color = "black", grid = [0,2])

app.display()