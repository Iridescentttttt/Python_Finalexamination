from manimlib import *

class HMM(Scene):
    def construct(self):
# phase1
# phase1
# phase1

        text = Text(
            "What is Marcov Model?",
            font="Times New Roman"
        )
        self.play(Write(text))

        text2 = Text(
            "Marcov Model",
            font="Times New Roman",
            color=BLUE
        ).move_to(TOP - UP * 0.5 + LEFT * 5.3).scale(0.6)
        self.play(ReplacementTransform(text, text2))

        tex = TexText(
            r"time series of random variable:\\"
            r"$s_1,s_2,s_3,...,s_t,...$"
        )
        self.play(ShowCreation(tex))
        self.wait(5)

        l = Line(
            start=ORIGIN,
            end=UP * 2
        )
        self.play(MoveAlongPath(tex, l))

        tex2 = Tex(
            r"P(s_t|s_1,s_2,s_3,...,s_{t-1}) = P(s_t|s_{t-1})",
            text_to_color_map={"P(s_t|s_{t-1})": BLUE}
        )
        tex2.next_to(tex, DOWN)
        self.play(ShowCreation(tex2))
        self.wait(5)

        # 画MARCOV图示
        # 画MARCOV图示
        # 画MARCOV图示

        c1 = Circle(
            color=BLUE,
            radius=0.5
        )
        c2 = Circle(
            color=BLUE,
            radius=0.5
        )
        c3 = Circle(
            color=BLUE,
            radius=0.5
        )
        c4 = Circle(
            color=BLUE,
            radius=0.5
        )
        t1 = TexText(
            "m1"
        ).scale(0.7)
        t2 = TexText(
            "m2"
        ).scale(0.7)
        t3 = TexText(
            "m3"
        ).scale(0.7)
        t4 = TexText(
            "m4"
        ).scale(0.7)

        set1 = VGroup(c1, t1)
        set2 = VGroup(c2, t2)
        set3 = VGroup(c3, t3)
        set4 = VGroup(c4, t4)
        setC = VGroup(set1, set2, set3, set4).arrange(RIGHT, buff=2)
        self.play(Write(setC))
        self.wait(2)

        # draw the lines
        a1 = CurvedArrow(
            start_point=c1.get_start(),
            end_point=c2.get_start() + LEFT
        )
        a2 = CurvedArrow(
            start_point=c2.get_start(),
            end_point=c3.get_start() + LEFT
        )
        a3 = CurvedArrow(
            start_point=c3.get_start(),
            end_point=c4.get_start() + LEFT
        )
        a4 = CurvedArrow(
            start_point=c2.get_start(),
            end_point=c4.get_start() + LEFT,
            color=BLUE
        )
        t11 = TexText(
            "1.0"
        ).scale(0.5).next_to(a1, DOWN * 0.3)
        t12 = TexText(
            "0.6"
        ).scale(0.5).next_to(a2, DOWN * 0.3)
        t13 = TexText(
            "0.3"
        ).scale(0.5).next_to(a3, DOWN * 0.3)
        t14 = TexText(
            "0.4",
            color=BLUE
        ).scale(0.5).next_to(a4, DOWN * 0.3)
        set11 = VGroup(a1, t11)
        set12 = VGroup(a2, t12)
        set13 = VGroup(a3, t13)
        set14 = VGroup(a4, t14)

        self.play(Write(set11)), self.play(Write(set12)), self.play(Write(set13))
        self.wait()
        self.play(Write(set14))
        self.wait(10)

        set = VGroup(set1, set2, set3, set4, set11, set12, set13, set14)
        setA = VGroup(tex, tex2, text2)
        self.play(Uncreate(set))
        self.play(Uncreate(setA))

#phase2
#phase2
#phase2

        map1={
            r"$s_1,s_2,s_3,...,s_T$": BLUE,
            r"$o_t$":BLUE,
            r"$s_t$":BLUE
        }
        text1=Text(
            "Hidden Marcov Model(HMM)",
            t2c={"Hidden Marcov Model(HMM)":BLUE},
            font="Times New Roman",
        )
        self.play(Write(text1.scale(0.7)))

        #self.wait(2)

        text2 = text1.copy().scale(0.8).move_to(TOP - UP * 0.5 + LEFT * 3.5)
        self.play(ReplacementTransform(text1,text2))

        tex=TexText(r"time series $s_1,s_2,s_3,...,s_T$ is now invisible",
                    tex_to_color_map = map1
                    )
        self.play(Write(tex))
        self.wait()
        self.play(Uncreate(tex))

        tex1=TexText(
            r"for every $s_t$, there is an output $o_t$\\",
            r"$o_t$ is only relevant to $s_t$" ,
            tex_to_color_map = map1
        ).scale(0.9)
        self.play(Write(tex1))
        tex2 = tex1.copy().scale(0.9).move_to(UP * 2.2)
        self.play(ReplacementTransform(tex1,tex2))

        c1 = Circle(
            color=BLUE,
            radius=0.5
        )
        c2 = Circle(
            color=BLUE,
            radius=0.5
        )
        c3 = Circle(
            color=BLUE,
            radius=0.5
        )
        c4 = Circle(
            color=BLUE,
            radius=0.5
        )
        t1 = TexText(
            "s1"
        ).scale(0.7)
        t2 = TexText(
            "s2"
        ).scale(0.7)
        t3 = TexText(
            "s3"
        ).scale(0.7)
        t4 = TexText(
            "s4"
        ).scale(0.7)

        set1 = VGroup(c1, t1)
        set2 = VGroup(c2, t2)
        set3 = VGroup(c3, t3)
        set4 = VGroup(c4, t4)
        setC1 = VGroup(set1, set2, set3, set4).arrange(RIGHT, buff=2)


        a1=Arrow(
            start=c1.get_start()+LEFT*0.25,
            end=c2.get_start()+LEFT*0.75
        )
        a2 = Arrow(
            start=c2.get_start()+LEFT*0.25,
            end=c3.get_start()+LEFT*0.75
        )
        a3 = Arrow(
            start=c3.get_start()+LEFT*0.25,
            end=c4.get_start()+LEFT*0.75
        )
        setC2=VGroup(setC1,a1,a2,a3)
        self.play(Write(setC2.move_to(DOWN*2)))

        c5 = Circle(
            radius=0.5,
            color=RED
        )
        c6 = Circle(
            radius=0.5,
            color=RED
        )
        c7 = Circle(
            radius=0.5,
            color=RED
        )
        c8 = Circle(
            radius=0.5,
            color=RED
        )
        t5 = TexText(
            "o1"
        ).scale(0.7)
        t6 = TexText(
            "o2"
        ).scale(0.7)
        t7 = TexText(
            "o3"
        ).scale(0.7)
        t8 = TexText(
            "o4"
        ).scale(0.7)

        set5 = VGroup(c5, t5)
        set6 = VGroup(c6, t6)
        set7 = VGroup(c7, t7)
        set8 = VGroup(c8, t8)
        setC3 = VGroup(set5, set6, set7, set8).arrange(RIGHT, buff=2).move_to(RIGHT*2)

        a5 = Arrow(
            start=c1.get_start() + LEFT * 0.25,
            end=c5.get_start() + LEFT * 0.75
        )
        a6 = Arrow(
            start=c2.get_start() + LEFT * 0.25,
            end=c6.get_start() + LEFT * 0.75
        )
        a7 = Arrow(
            start=c3.get_start() + LEFT * 0.25,
            end=c7.get_start() + LEFT * 0.75
        )
        a8 = Arrow(
            start=c4.get_start() + LEFT * 0.25,
            end=c8.get_start() + LEFT * 0.75
        )

        setC4 = VGroup(setC3, a5, a6, a7, a8)
        self.play(Write(setC4))

        set=VGroup(text2,tex2)
        self.play(Uncreate(set))

        tex1=TexText(
            r"$y_1,y_2,y_3,...,y_N$ \qquad input syllable",
            r"\\"
            r"$w_1,w_2,w_3,...,w_N$ \qquad candidate character",
            tex_to_color_map = {"$y_1,y_2,y_3,...,y_N$":BLUE,
                                "$w_1,w_2,w_3,...,w_N$":BLUE}
        )
        self.play(Write(tex1.scale(0.9).move_to(UP*2.2)))
        self.wait(5)

        tex2=TexText(
            r"$w_t$is only relevant to $w_{t-1}$,so it is memoryless\\"
            r"$y_t$is only relevant to $w_t$\\",
            r"We can use HMM to estimate $w_t$",
            tex_to_color_map={"$y_t$": BLUE,
                              "$w_t$": BLUE,"$w_{t-1}$":BLUE,
                              "HMM":BLUE}
        )
        self.play(FadeTransform(tex1,tex2.scale(0.9).move_to(UP*2.2)))

        setC5=VGroup(setC2,setC4)
        self.play(FadeOut(setC5))

#用w,y替代HMM模型
#用w,y替代HMM模型
#用w,y替代HMM模型


        c1 = Circle(
            color=BLUE,
            radius=0.5
        )
        c2 = Circle(
            color=BLUE,
            radius=0.5
        )
        c3 = Circle(
            color=BLUE,
            radius=0.5
        )
        c4 = Circle(
            color=BLUE,
            radius=0.5
        )
        t1 = TexText(
            "w1"
        ).scale(0.7)
        t2 = TexText(
            "w2"
        ).scale(0.7)
        t3 = TexText(
            "w3"
        ).scale(0.7)
        t4 = TexText(
            "w4"
        ).scale(0.7)

        set1 = VGroup(c1, t1)
        set2 = VGroup(c2, t2)
        set3 = VGroup(c3, t3)
        set4 = VGroup(c4, t4)
        setC1 = VGroup(set1, set2, set3, set4).arrange(RIGHT, buff=2)

        a1 = Arrow(
            start=c1.get_start() + LEFT * 0.25,
            end=c2.get_start() + LEFT * 0.75
        )
        a2 = Arrow(
            start=c2.get_start() + LEFT * 0.25,
            end=c3.get_start() + LEFT * 0.75
        )
        a3 = Arrow(
            start=c3.get_start() + LEFT * 0.25,
            end=c4.get_start() + LEFT * 0.75
        )
        setC2 = VGroup(setC1, a1, a2, a3)
        setC2.move_to(DOWN * 2)

        c5 = Circle(
            radius=0.5,
            color=RED
        )
        c6 = Circle(
            radius=0.5,
            color=RED
        )
        c7 = Circle(
            radius=0.5,
            color=RED
        )
        c8 = Circle(
            radius=0.5,
            color=RED
        )
        t5 = TexText(
            "y1"
        ).scale(0.7)
        t6 = TexText(
            "y2"
        ).scale(0.7)
        t7 = TexText(
            "y3"
        ).scale(0.7)
        t8 = TexText(
            "y4"
        ).scale(0.7)

        set5 = VGroup(c5, t5)
        set6 = VGroup(c6, t6)
        set7 = VGroup(c7, t7)
        set8 = VGroup(c8, t8)
        setC3 = VGroup(set5, set6, set7, set8).arrange(RIGHT, buff=2).move_to(RIGHT * 2)

        a5 = Arrow(
            start=c1.get_end() + LEFT * 0.25,
            end=c5.get_end() + LEFT * 0.75
        )
        a6 = Arrow(
            start=c2.get_start() + LEFT * 0.25,
            end=c6.get_start() + LEFT * 0.75
        )
        a7 = Arrow(
            start=c3.get_start() + LEFT * 0.25,
            end=c7.get_start() + LEFT * 0.75
        )
        a8 = Arrow(
            start=c4.get_start() + LEFT * 0.25,
            end=c8.get_start() + LEFT * 0.75
        )

        setC4 = VGroup(setC3, a5, a6, a7, a8)
        setC5 = VGroup(setC2,setC4)
        self.play(Write(setC5))

        self.play(Uncreate(tex2))

        setC6=setC5.copy().scale(0.7).move_to(UP)
        self.play(ReplacementTransform(setC5,setC6))


#接下来化简公式 全都用TexText写
#接下来化简公式 全都用TexText写
#接下来化简公式 全都用TexText写

        tex1 = Tex(
            # r"$\begin{align}$",
            r"\arg\max_{w\in W} P(w_1,w_2,...,w_N|y_1,y_2,..y_N)",
            # r"$\end{align}$",
        ).move_to(DOWN * 2)
        self.play(Write(tex1))

        self.play(Uncreate(setC6))

        tex2 = TexText(
            r"$P(A|B)$=$\frac{P(B|A)P(A)}{P(B)}$",
            tex_to_color_map={r"$\frac{P(B|A)P(A)}{P(B)}$": BLUE}
        )
        self.play(Write(tex2))
        l = Line(
            start=ORIGIN,
            end=UP * 2
        )

        self.play(MoveAlongPath(tex2, l))

        tex3 = TexText(
            r"$P(w_1,w_2,...,w_N|y_1,y_2,...,y_N)= $"
            r"$\frac{P(y_1,y_2,...,y_N|w_1,...,w_N)P(w_1,w_2,...,w_N)}{P(y_1,y_2,...,y_N)}$"
            ,
            tex_to_color_map={
                r"$\frac{P(y_1,y_2,...,y_N|w_1,...,w_N)P(w_1,w_2,...,w_N)}{P(y_1,y_2,...,y_N)}$": BLUE
            }
        ).scale(0.7).move_to(UP * 0.6)
        self.play(FadeTransform(tex2, tex3))
        self.wait()
        tex4 = TexText(
            r"$P(y_1,y_2,...,y_N)=1$",
            color=YELLOW
        ).move_to(UP * 2)
        self.play(Write(tex4))

        tex5 = TexText(
            r"$= P(y_1,y_2,...,y_N|w_1,...,w_N)P(w_1,w_2,...,w_N)$",
            color=YELLOW
        ).scale(0.7).next_to(tex3, DOWN)
        self.play(FadeTransform(tex4, tex5))

        tex52 = TexText(
            r"$P(y_1,y_2,...,y_N|w_1,...,w_N) \hspace{1cm} P(w_1,w_2,...,w_N)$",
            color=BLUE
        ).move_to(UP * 2)

        set1 = VGroup(tex3, tex5)
        self.play(FadeTransform(set1, tex52))
        self.play(Uncreate(tex1))


        tex61 = Tex(
            r"P(w_1,w_2,...,w_N) &= P(w_N|w_1,...,w_{N-1})P(w_1,...,w_{N-1})\\",
            r"&=P(w_N|w_1,...,w_{N-1})P(w_{N-1}|w_1,...,w_{N-2})P(w_1,...,w_{N-2})\\",

        ).scale(0.7).move_to(DOWN*0.5)

        tex62=Tex(
            r"&=\prod_t^N P(w_t|w_1,...,w_{t-1})\\",
            r"&=\prod_t^N P(w_t|w_{t-1})",
            tex_to_color_map={"\prod_t^N P(w_t|w_{t-1})":YELLOW}
        ).scale(0.7).next_to(tex61,DOWN).shift(LEFT*1.4)

        set2=VGroup(tex61,tex62)

        self.play(Write(tex61))
        self.wait(2)
        self.play(Write(tex62))

        tex7 = TexText(
            r"$\prod_t^N P(w_t|w_{t-1})$",
            color=YELLOW
        ).scale(0.8).move_to(UP+RIGHT*3.5)
        self.play(FadeTransform(set2,tex7))

        tex8 = Tex(
            r"P(y_1,y_2,...,y_N|w_1,w_2,...,w_N) ",
            r"&=\prod_t^N P(y_t|w_1,w_2,...,w_N) \\",
            r"&= \prod_t^N P(y_t|w_t)",
            tex_to_color_map={r"&= \prod_t^N P(y_t|w_t)":YELLOW}
        ).scale(0.7).move_to(DOWN)
        self.play(Write(tex8))

        tex9 = TexText(
            r"$\prod_t^N P(y_t|w_t)$",
            color=YELLOW
        ).scale(0.8).move_to(UP+LEFT*3)
        self.play(FadeTransform(tex8, tex9))


        tex10 = Tex(
            r"&\arg\max_{w\in W} P(w_1,w_2,...,w_N|y_1,y_2,..y_N)\\",
            r"&=P(y_1,y_2,...,y_N|w_1,...,w_N)P(w_1,w_2,...,w_N)\\",
            r"&=\prod_t^N P(w_t|w_{t-1})P(y_t|w_t)"
        ).scale(0.8).shift(DOWN)
        self.play(Write(tex10))

        set3=VGroup(tex52,tex7,tex9)
        self.play(Uncreate(set3))
        tex11=Tex(
            r"&\arg\max_{w\in W} P(w_1,w_2,...,w_N|y_1,y_2,..y_N)\\",
            r"&=\prod_t^N P(w_t|w_{t-1})P(y_t|w_t)",
            color=BLUE
        )
        self.play(FadeTransform(tex10,tex11))
        self.wait(3)


