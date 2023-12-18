
from manimlib import *


class thirdpart(Scene):
    def construct(self):
        # 标题部分
        title = Text("3.拼音转汉字的算法", font_size=50, color=WHITE, font="FangSong")
        self.play(Write(title))
        target_position = LEFT * 4.2 + UP * 3.3
        title.scale(0.7)
        self.play(
            title.animate.move_to(target_position),
            run_time=1,  # 持续时间为2秒
            rate_func=smooth  # 使用平滑的过渡函数
        )

        #拼音转汉字的算法，其实可以看成一个动态规划的问题，自底向上的过程。
        content=Text("拼音转汉字的算法，其实可以看成一个动态规划的问题，自底向上\n的过程。如下图拼音到汉字的转换过程:", font_size=30, color=WHITE, font="FangSong")
        content.move_to(UP*2)
        self.play(Write(content))

        #最重要的一张图
        # 创建连续的四个长方形
        rectangles = VGroup(*[Rectangle(width=1, height=0.5) for _ in range(5)])

        # 设置长方形的位置
        rectangles.arrange(RIGHT, buff=1.3)
        rectangles.move_to(UP)
        self.play(ShowCreation(rectangles))
        # 添加文字到长方形内部
        texts = ["y_1", "y_2", "y_3", "...","y_N"]

        texttex0 = Tex(texts[0])
        texttex0.move_to(rectangles[0])
        texttex1 = Tex(texts[1])
        texttex1.move_to(rectangles[1])
        texttex2 = Tex(texts[2])
        texttex2.move_to(rectangles[2])
        texttex3 = Tex(texts[3])
        texttex3.move_to(rectangles[3])
        texttex4 = Tex(texts[4])
        texttex4.move_to(rectangles[4])
        self.play(Write(texttex1),Write(texttex4),Write(texttex3),Write(texttex2),Write(texttex0),run_time=0.5)

        start=Text("起点", font_size=30, color=WHITE, font="FangSong")
        start.move_to(LEFT*6+DOWN*1.2)
        self.play(Write(start))

        end = Text("终点", font_size=30, color=WHITE, font="FangSong")
        end.move_to(RIGHT * 6 + DOWN * 1.2)
        self.play(Write(end))

        circle1 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle1.set_fill(color=BLUE_B, opacity=0.1)
        circle1.set_stroke(color=BLUE)
        letax1=Tex("w_{11}")
        letax1.scale(0.7)
        circle_text1 = VGroup(circle1, letax1)
        circle_text1.move_to(LEFT * 4.6)
        self.play(ShowCreation(circle_text1), run_time=0.1)

        circle2 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle2.set_fill(color=BLUE_B, opacity=0.1)
        circle2.set_stroke(color=BLUE)
        letax2=Tex("w_{12}")
        letax2.scale(0.7)
        circle_text2 = VGroup(circle2, letax2)
        circle_text2.next_to(circle_text1,DOWN*2)
        self.play(ShowCreation(circle_text2), run_time=0.1)

        circle3 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle3.set_fill(color=BLUE_B, opacity=0.1)
        circle3.set_stroke(color=BLUE)
        letax3 = Tex("w_{13}")
        letax3.scale(0.7)
        circle_text3 = VGroup(circle3, letax3)
        circle_text3.next_to(circle_text2, DOWN * 2)
        self.play(ShowCreation(circle_text3), run_time=0.1)

        circle4 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle4.set_fill(color=BLUE_B, opacity=0.1)
        circle4.set_stroke(color=BLUE)
        letax4 = Tex("w_{21}")
        letax4.scale(0.7)
        circle_text4 = VGroup(circle4, letax4)
        circle_text4.next_to(rectangles[1],DOWN)
        self.play(ShowCreation(circle_text4), run_time=0.1)

        circle5 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle5.set_fill(color=BLUE_B, opacity=0.1)
        circle5.set_stroke(color=BLUE)
        letax5 = Tex("w_{22}")
        letax5.scale(0.7)
        circle_text5 = VGroup(circle5, letax5)
        circle_text5.next_to(circle_text4, DOWN)
        self.play(ShowCreation(circle_text5), run_time=0.1)

        circle6 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle6.set_fill(color=BLUE_B, opacity=0.1)
        circle6.set_stroke(color=BLUE)
        letax6 = Tex("w_{23}")
        letax6.scale(0.7)
        circle_text6 = VGroup(circle6, letax6)
        circle_text6.next_to(circle_text5, DOWN)
        self.play(ShowCreation(circle_text6), run_time=0.1)

        circle7 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle7.set_fill(color=BLUE_B, opacity=0.1)
        circle7.set_stroke(color=BLUE)
        letax7 = Tex("w_{24}")
        letax7.scale(0.7)
        circle_text7 = VGroup(circle7, letax7)
        circle_text7.next_to(circle_text6, DOWN)
        self.play(ShowCreation(circle_text7), run_time=0.1)

        circle8 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle8.set_fill(color=BLUE_B, opacity=0.1)
        circle8.set_stroke(color=BLUE)
        letax8 = Tex("w_{31}")
        letax8.scale(0.7)
        circle_text8 = VGroup(circle8, letax8)
        circle_text8.next_to(rectangles[2], DOWN*5)
        self.play(ShowCreation(circle_text8), run_time=0.1)

        circle9 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle9.set_fill(color=BLUE_B, opacity=0.1)
        circle9.set_stroke(color=BLUE)
        letax9 = Tex("w_{32}")
        letax9.scale(0.7)
        circle_text9 = VGroup(circle9, letax9)
        circle_text9.next_to(circle_text8, DOWN*1.5)
        self.play(ShowCreation(circle_text9), run_time=0.1)

        circle10 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle10.set_fill(color=BLUE_B, opacity=0.1)
        circle10.set_stroke(color=BLUE)
        letax10 = Tex("w_{N1}")
        letax10.scale(0.7)
        circle_text10 = VGroup(circle10, letax10)
        circle_text10.next_to(rectangles[4], DOWN*3.5)
        self.play(ShowCreation(circle_text10), run_time=0.1)

        circle11 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle11.set_fill(color=BLUE_B, opacity=0.1)
        circle11.set_stroke(color=BLUE)
        letax11 = Tex("w_{N2}")
        letax11.scale(0.7)
        circle_text11 = VGroup(circle11, letax11)
        circle_text11.next_to(circle_text10, DOWN)
        self.play(ShowCreation(circle_text11), run_time=0.1)

        circle12 = Circle(
            radius=0.35,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle12.set_fill(color=BLUE_B, opacity=0.1)
        circle12.set_stroke(color=BLUE)
        letax12 = Tex("w_{N3}")
        letax12.scale(0.7)
        circle_text12 = VGroup(circle12, letax12)
        circle_text12.next_to(circle_text11, DOWN)
        self.play(ShowCreation(circle_text12), run_time=0.1)

        line1 = Line(start, circle_text1)
        line2 = Line(start, circle_text2)
        line3 = Line(start, circle_text3)
        line4 = Line(circle_text1, circle_text4)
        line5 = Line(circle_text1, circle_text5)
        line6 = Line(circle_text1, circle_text6)
        line7 = Line(circle_text1, circle_text7)
        line8 = Line(circle_text2, circle_text4)
        line9 = Line(circle_text2, circle_text5)
        line10 = Line(circle_text2, circle_text6)
        line11 = Line(circle_text2, circle_text7)
        line12 = Line(circle_text3, circle_text4)
        line13 = Line(circle_text3, circle_text5)
        line14 = Line(circle_text3, circle_text6)
        line15 = Line(circle_text3, circle_text7)
        line16 = Line(circle_text4, circle_text8)
        line17 = Line(circle_text4, circle_text9)
        line18 = Line(circle_text5, circle_text8)
        line19 = Line(circle_text5, circle_text9)
        line20 = Line(circle_text6, circle_text8)
        line21 = Line(circle_text6, circle_text9)
        line22 = Line(circle_text7, circle_text8)
        line23 = Line(circle_text7, circle_text9)
        dot1 = Dot()  # 创建一个默认的点对象
        dot1.move_to(DOWN*0.7+RIGHT*1.5)
        dot2 = Dot()  # 创建一个默认的点对象
        dot2.move_to((DOWN*2.1+RIGHT*1.5))
        dot3 = Dot()  # 创建一个默认的点对象
        dot3.move_to(DOWN*0.7+RIGHT*3)
        dot4 = Dot()  # 创建一个默认的点对象
        dot4.move_to(DOWN*2.1+RIGHT*3)
        self.add(dot1,dot2,dot3,dot4)  # 将点对象添加到场景中
        line24 = Line(circle_text8, dot1)
        line25 = Line(circle_text8, dot2)
        line26 = Line(circle_text9, dot1)
        line27 = Line(circle_text9, dot2)
        line28 = ArcBetweenPoints(dot1.get_center(), dot3.get_center(), angle=-TAU/4)
        line29 = ArcBetweenPoints(dot2.get_center(), dot4.get_center(), angle=-TAU/4)
        line30 = Line(dot3, circle_text10)
        line31 = Line(dot3, circle_text11)
        line32 = Line(dot3, circle_text12)
        line33 = Line(dot4, circle_text10)
        line34 = Line(dot4, circle_text11)
        line35 = Line(dot4, circle_text12)
        line36 = Line(circle_text10, end)
        line37 = Line(circle_text11, end)
        line38 = Line(circle_text12, end)

        self.play(ShowCreation(line1),ShowCreation(line2),ShowCreation(line3),ShowCreation(line4),ShowCreation(line5),ShowCreation(line6),ShowCreation(line7),ShowCreation(line8),ShowCreation(line9),ShowCreation(line10),ShowCreation(line11),ShowCreation(line12),ShowCreation(line13),ShowCreation(line14),ShowCreation(line15),ShowCreation(line16),ShowCreation(line17),ShowCreation(line18),ShowCreation(line19),ShowCreation(line20),ShowCreation(line21),ShowCreation(line22),ShowCreation(line23),ShowCreation(line24),ShowCreation(line25),ShowCreation(line26),ShowCreation(line27),ShowCreation(line28),ShowCreation(line29),ShowCreation(line30),ShowCreation(line31),ShowCreation(line32),ShowCreation(line33),ShowCreation(line34),ShowCreation(line35),ShowCreation(line36),ShowCreation(line37),ShowCreation(line38),run_time=2)

        self.wait(4)

        self.play(FadeOut(content))
        text = Text("其中，y1,y2,y3,…,yN是使用者输入的拼音串；w11,w12,w13是第一\n个音y1的候选汉字，以此类推。",
                    font_size=30, color=WHITE, font="FangSong")
        text.move_to(UP * 2)
        self.play(FadeIn(text))
        self.play(FadeToColor(rectangles,BLUE_B))
        self.wait(2)
        self.play(FadeOut(text))

        text = Text("可见，从第一个汉字到最后一个汉字有很多种组合的可能。\n拼音输入法需要根据上下文给定拼音查找下的最优句子",
                    font_size=30, color=WHITE, font="FangSong")
        text.move_to(UP * 2)
        self.play(Write(text))
        self.wait(15)


        picture=VGroup(texttex2,texttex0,texttex1,texttex3,texttex4,start,end,rectangles,dot2,dot3,dot4,dot1,letax1,letax2,letax3,letax4,letax5,letax6,letax7,letax8,letax9,letax10,letax11,letax12,circle1,circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9,circle10,circle11,circle12,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38)
        self.play(FadeOut(picture))



        tex1 = Tex(r"w_1,w_2,...,w_N",r"&= \arg\max_{w\in W} P(w_1,w_2,...,w_N|y_1,y_2,..y_N)")
        tex1.set_color(BLUE_B)
        self.play(Write(tex1))
        self.wait(2)
        # self.play(FadeOut(tex1))

        text1 = Text(
            "利用贝叶斯公式和隐马尔可夫模型可以对公式进行简化",
            font_size=30, color=WHITE, font="FangSong")
        text1.move_to(UP * 2)
        self.play(Transform(text,text1))
        self.wait(4)

        tex2 = Tex(r"w_1,w_2,...,w_N",r"&= \arg\max_{w\in W} P(w_1,w_2,...,w_N|y_1,y_2,..y_N)\\",
        r"&=P(y_1,y_2,...,y_N|w_1,...,w_N)P(w_1,w_2,...,w_N)\\",
        r"&\approx \arg\max_{w\in W} \prod_t^N P(w_i|w_{i-1})P(y_i|w_i)")
        tex2.set_color(BLUE_B)
        tex2.move_to(DOWN*0.5)
        # self.play(Write(tex1))
        self.play(Transform(tex1,tex2))
        self.wait(5)
        self.play(FadeOut(text1))
        self.play(FadeOut(tex2))

        self.clear()

        text = Text(
            "接下来让我们对刚才提到的马尔可夫链做一个简单的了解",
            font_size=30, color=WHITE, font="FangSong")
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))



##########################################################################插入马尔科夫视频




        # 标题部分
        title = Text("3.拼音转汉字的算法", font_size=50, color=WHITE, font="FangSong")
        target_position = LEFT * 4.2 + UP * 3.3
        title.scale(0.7)
        title.move_to(target_position)
        self.play(Write(title))

        text1 = Text(
            "然后对之前的公式两边取对数，乘法就会变成加法，就变成了类似于寻找\n最短路径的问题了。此处我们使用两个节点（单词）之前的转移概率和\n生成概率的乘积作为迪杰斯特拉算法中两点之间的距离",
            font_size=23, color=WHITE, font="FangSong")
        text1.move_to(UP * 2)
        self.play(Write(text1),Write(picture),run_time=3)
        self.wait(13)
        self.play(FadeOut(text1),FadeOut(picture))

        #w_1,w_2,...,w_N", r"&= \arg\max_{w\in W} P(w_1,w_2,...,w_N|y_1,y_2,..y_N)

        text1 = Text(
            "也就是用下式作为最短路径问题中两点之间的距离",
            font_size=30, color=WHITE, font="FangSong")
        text1.move_to(UP)
        self.play(Write(text1))

        tex1 = Tex(r"D(W_{i-1},W_i) = -logP(W_i|W_{i-1})*P(Y_i|W_i)")
        tex1.set_color(BLUE_B)
        tex1.move_to(DOWN)
        self.play(Write(tex1))
        self.wait(2)
        self.clear()

        text1 = Text(
            "接下来让我们了解一下求解最短路径问题的Dijkstra算法",
            font_size=23, color=WHITE, font="FangSong")
        self.play(Write(text1))
        self.wait(5)
        self.play(FadeOut(text1))

###################################################插入dijkstra算法视频