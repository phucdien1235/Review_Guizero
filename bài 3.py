from guizero import App, Text, Slider
def check():
    your_result.value = f"Kết quả: {"Rớt" if score.value < 5 else "Đậu"}"
app = App(title = "Xét điểm", height = 100, layout = "grid")
Text(app, grid = [0,0], text = "Điểm: ", size = 15)
score = Slider(app, grid = [1,0], end = 10, command = check)
your_result = Text(app, grid = [0,1], text = "Kết quả: Rớt", size = 15)

app.display()