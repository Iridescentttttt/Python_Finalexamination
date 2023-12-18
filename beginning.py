from manimlib import *

class begin(Scene):
    def construct(self):
        # 标题部分
        title = Text("拼音输入法的数学原理", font_size=50, color=WHITE, font="FangSong");
        title.move_to((UP*1.2))
        self.play(Write(title))

        text1 = Text("第五组(蟒蛇入门)：黄苇依 何玥仪 李振凯", font_size=40, color=WHITE, font="FangSong");
        self.play(Write(text1))

        text2 = Text("Powered by : Python + Manim", font_size=40, font="Times New Roman", t2c={"Python": BLUE, "Manim": ORANGE});
        text2.move_to(DOWN*1.2)
        self.play(Write(text2))

        self.wait(5)