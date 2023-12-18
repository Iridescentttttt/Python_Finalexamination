from manimlib import *


class fourthpart(Scene):
    def construct(self):
        # 标题部分
        title = Text("4.个性化的语言模型", font_size=50, color=WHITE, font="FangSong")
        self.play(Write(title))
        target_position = LEFT * 4.2 + UP * 3.3
        title.scale(0.7)
        self.play(
            title.animate.move_to(target_position),
            run_time=1,  # 持续时间为2秒
            rate_func=smooth  # 使用平滑的过渡函数
        )

        text1 = Text("由于不同人平时写的东西主体不同，由于文化程度的差异，\n",
                     font_size=30, color=WHITE, font="FangSong")
        text2 = Text(
            "用词习惯不同，说话和写作的水平也不同，\n",
            font_size=30, color=WHITE, font="FangSong")
        text3 = Text(
            "因此，他们各自应该有各自的语言模型。",
            font_size=30, color=WHITE, font="FangSong")
        text1.move_to(UP)
        text3.move_to(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(7)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3))

        text1 = Text("接下来有两个问题要解决",
                     font_size=30, color=WHITE, font="FangSong")
        text2 = Text("1.如何训练一个个性化的语言模型",
                     font_size=30, color=BLUE_B, font="FangSong")
        text3 = Text("2.怎样处理好它和通用语言模型的关系",
                     font_size=30, color=BLUE_B, font="FangSong")
        text1.move_to(UP)
        text3.move_to(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3))

        text1 = Text("为每个人训练一个特定的语言模型最好是收集足够多这个人自己写的文字",
                     font_size=25, color=WHITE, font="FangSong")
        text2 = Text("但是训练一个词汇量在几万的二元模型需要几千万词的语料",
                     font_size=30,  font="FangSong",t2c={"几万": BLUE, "二元模型": BLUE, "几千万词": ORANGE})
        text3 = Text("这显然是不现实的，因此我们使用一种更好的方法",
                     font_size=30, color=WHITE, font="FangSong")
        text1.move_to(UP)
        text3.move_to(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(7)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3))

        text1 = Text("更好的方法是找到大量符合用户经常输入的内容和用语习惯的语料",
                     font_size=30, color=WHITE, font="FangSong")
        text2 = Text("显然这其中的关键在于如何找到这些符合条件的语料",
                     font_size=30,  color=WHITE,font="FangSong")
        text3 = Text("这里要用到余弦定理和文本分类的技术了",
                     font_size=30, font="FangSong",t2c={"余弦定理": BLUE, "文本分类": BLUE})
        text1.move_to(UP)
        text3.move_to(DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(5)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3))


        text = Text("步骤如下：\n1).将训练语言模型的文本或者语料按照主题\n  分成很多不同的类别，C1,C2,...,C1000\n2).然后求每个分类的特征向量（TF-IDF）X1,...,X1000\n3).统计某人输入的文本，得到他输入的词的特征向量Y\n4).计算Y和Xi的余弦\n5).选择前K个和Y距离最近的类对应的文本，\n  作为用户的语言模型的训练数据\n6).用筛选的训练数据训练语言模型M1",font_size=30, color=WHITE, font="FangSong")
        self.play(Write(text),run_time=5)
        self.wait(8)
        self.play(FadeOut(text))

        text1 = Text("个性化模型M1对常用词效果更好，但是通用模型M0对相对偏僻的词效果好",
                     font_size=28, color=WHITE, font="FangSong")
        text2 = Text("解决方法如下：",
                     font_size=30, color=WHITE, font="FangSong")
        text3 = Text("1).可以用最大熵模型对M0、M1进行综合，但是成本较高",
                     font_size=30, color=BLUE, font="FangSong")
        text4 = Text("2).线性插值的简化模型",
                     font_size=30, font="FangSong", color=BLUE)
        text1.move_to(UP*0.7)
        text3.move_to(DOWN*0.8)
        text4.move_to(DOWN*1.6)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.wait(8)

        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))

        text1 = Text("假设M0、M1都是二元模型，计算(Wi-1,Wi)的概率为P1(Wi-1,Wi)和P0(Wi-1,Wi)",
                     font_size=25, color=WHITE, font="FangSong")
        text2 = Text("对新的模型M'，其条件概率为：",
                     font_size=25, color=WHITE, font="FangSong")
        text3 = Tex(r"(W_{i-1},W_i)'=\lambda(W_{i-1})*P_0(W_i|W_{i-1})+(1-\lambda(W_{i-1}))*P_1(W_i|W_{i-1})",color=BLUE_B,font_size=40)
        text4 = Text("其中，0<λ(Wi-1)<1是一个插值参数",
                     font_size=25, font="FangSong", t2c={"余弦定理": BLUE, "文本分类": BLUE})
        text5 = Text("虽然最大熵模型更好但是难以训练，线性插值模型也能达到80%的效果",
                     font_size=25, color=WHITE, font="FangSong")
        text6 = Text("Google拼音输入法的个性化语言模型就是这么实现的",
                     font_size=25, color=WHITE, font="FangSong")
        text1.move_to(UP*2)
        text2.move_to((UP*1))
        text4.move_to(DOWN)
        text5.move_to(DOWN*2)
        text6.move_to(DOWN*3)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(11)
        #self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4),FadeOut(text5), FadeOut(text6))

        text=VGroup(text1,text2,text3,text4,text5,text6)
        text6 = Text("The End",
                     font_size=80, color=WHITE, font="Times New Roman")
        self.play(Transform(text,text6))
        self.wait(3)