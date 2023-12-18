from os import system

from manimlib import *


class dijkstra(Scene):
    def construct(self):
        # 标题部分
        title = Text("Dijksta Algorithm", font_size=40, color=WHITE, font="Times new Roman");
        self.play(Write(title))
        target_position = LEFT * 4.2 + UP * 3.3
        self.play(
            title.animate.move_to(target_position),
            run_time=1,  # 持续时间为2秒
            rate_func=smooth  # 使用平滑的过渡函数
        )

        # 第一个圆
        circle1 = Circle(
            radius=0.5,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle1.set_fill(color=BLUE_B, opacity=0.1)
        circle1.set_stroke(color=BLUE)
        text = Text("0", font_size=24, color=WHITE, font="Times new Roman")
        circle_text1 = VGroup(circle1, text)
        circle_text1.move_to(LEFT * 4)
        self.play(ShowCreation(circle_text1), run_time=1)

        # 第二个圆
        circle2 = Circle(
            radius=0.5,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle2.set_fill(color=BLUE_B, opacity=0.1)
        circle2.set_stroke(color=BLUE)
        text = Text("1", font_size=24, color=WHITE, font="Times new Roman")
        circle_text2 = VGroup(circle2, text)
        circle_text2.move_to(LEFT * 1.5 + UP * 1.5)
        self.play(ShowCreation(circle_text2), run_time=1)

        circle3 = Circle(
            radius=0.5,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle3.set_fill(color=BLUE_B, opacity=0.1)
        circle3.set_stroke(color=BLUE)
        text = Text("2", font_size=24, color=WHITE, font="Times new Roman")
        circle_text3 = VGroup(circle3, text)
        circle_text3.move_to(LEFT * 1.5 + DOWN * 1.5)
        self.play(ShowCreation(circle_text3), run_time=1)

        circle4 = Circle(
            radius=0.5,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle4.set_fill(color=BLUE_B, opacity=0.1)
        circle4.set_stroke(color=BLUE)
        text = Text("3", font_size=24, color=WHITE, font="Times new Roman")
        circle_text4 = VGroup(circle4, text)
        circle_text4.move_to(RIGHT * 1.5 + UP * 1.5)
        self.play(ShowCreation(circle_text4), run_time=1)

        circle5 = Circle(
            radius=0.5,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle5.set_fill(color=BLUE_B, opacity=0.1)
        circle5.set_stroke(color=BLUE)
        text = Text("4", font_size=24, color=WHITE, font="Times new Roman")
        circle_text5 = VGroup(circle5, text)
        circle_text5.move_to(RIGHT * 1.5 + DOWN * 1.5)
        self.play(ShowCreation(circle_text5), run_time=1)

        circle6 = Circle(
            radius=0.5,  # 半径
            arc_center=ORIGIN,  # 圆心
            stroke_width=3,  # 轮廓线粗细
        )
        circle6.set_fill(color=BLUE_B, opacity=0.1)
        circle6.set_stroke(color=BLUE)
        text = Text("5", font_size=24, color=WHITE, font="Times new Roman")
        circle_text6 = VGroup(circle6, text)
        circle_text6.move_to(RIGHT * 4)
        self.play(ShowCreation(circle_text6), run_time=1)

        line1 = Line(circle_text1, circle_text2)
        line2 = Line(circle_text1, circle_text3)
        line3 = Line(circle_text2, circle_text4)
        line4 = Line(circle_text2, circle_text3)
        line5 = Line(circle_text3, circle_text4)
        line6 = Line(circle_text3, circle_text5)
        line7 = Line(circle_text4, circle_text5)
        line8 = Line(circle_text5, circle_text6)
        line9 = Line(circle_text4, circle_text6)
        line_group = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9)
        self.play(ShowCreation(line_group))

        Graph_nodistance = VGroup(line_group, circle_text1, circle_text2, circle_text3, circle_text4, circle_text5,
                                  circle_text6)

        text1 = Text("5", font_size=30, color=BLUE_B, font="Times new Roman")
        text1.next_to(line1, UP, buff=0.02)
        text2 = Text("1", font_size=30, color=BLUE_B, font="Times new Roman")
        text2.next_to(line2, DOWN, buff=0.02)
        text3 = Text("3", font_size=30, color=BLUE_B, font="Times new Roman")
        text3.next_to(line3, UP)
        text4 = Text("9", font_size=30, color=BLUE_B, font="Times new Roman")
        text4.next_to(line4, RIGHT, buff=0.2)
        text5 = Text("4", font_size=30, color=BLUE_B, font="Times new Roman")
        text5.next_to(line5, UP * 0)
        text6 = Text("5", font_size=30, color=BLUE_B, font="Times new Roman")
        text6.next_to(line6, UP)
        text7 = Text("13", font_size=30, color=BLUE_B, font="Times new Roman")
        text7.next_to(line7, RIGHT, buff=0.2)
        text8 = Text("15", font_size=30, color=BLUE_B, font="Times new Roman")
        text8.next_to(line8, DOWN, buff=0.02)
        text9 = Text("14", font_size=30, color=BLUE_B, font="Times new Roman")
        text9.next_to(line9, UP, buff=0.02)
        text_group = VGroup(text1, text2, text3, text4, text5, text6, text7, text8, text9)
        self.play(Write(text_group), run_time=2)

        Graph = VGroup(Graph_nodistance, text_group)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in Graph])

        # class analysis(Scene):
        #     def construct(self):
        Graph.scale(0.7)
        Graph.move_to(UP)
        self.play(ShowCreation(Graph))
        text1 = Text("接下来让我们找到一条从0号点到5号点的最短路径", font_size=30, color=WHITE, font="FangSong")
        text1.move_to(DOWN * 1.2)
        text2 = Text("首先让我们把相邻节点的距离列出来", font_size=30, color=WHITE, font="FangSong")
        text2.move_to(DOWN * 2)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2))

        text1 = Text("0 1 5", font_size=30, color=BLUE_B, font="Times new Roman")
        text1.move_to(DOWN * 1.2 + LEFT * 2)
        self.play(Write(text1))
        text2 = Text("0 2 1", font_size=30, color=BLUE_B, font="Times new Roman")
        text2.move_to(DOWN * 1.7 + LEFT * 2)
        self.play(Write(text2))
        text3 = Text("1 2 9", font_size=30, color=BLUE_B, font="Times new Roman")
        text3.move_to(DOWN * 2.2 + LEFT * 2)
        self.play(Write(text3))
        text4 = Text("1 3 3", font_size=30, color=BLUE_B, font="Times new Roman")
        text4.move_to(DOWN * 2.7 + LEFT * 2)
        self.play(Write(text4))
        text5 = Text("2 3 4", font_size=30, color=BLUE_B, font="Times new Roman")
        text5.move_to(DOWN * 3.2 + LEFT * 2)
        self.play(Write(text5))
        text6 = Text("2 4 5", font_size=30, color=BLUE_B, font="Times new Roman")
        text6.move_to(DOWN * 1.2 + RIGHT * 2)
        self.play(Write(text6))
        text7 = Text("2 4 5", font_size=30, color=BLUE_B, font="Times new Roman")
        text7.move_to(DOWN * 1.7 + RIGHT * 2)
        self.play(Write(text7))
        text8 = Text("3 4 13", font_size=30, color=BLUE_B, font="Times new Roman")
        text8.move_to(DOWN * 2.2 + RIGHT * 2)
        self.play(Write(text8))
        text9 = Text("3 5 14", font_size=30, color=BLUE_B, font="Times new Roman")
        text9.move_to(DOWN * 2.7 + RIGHT * 2)
        self.play(Write(text9))
        text10 = Text("4 5 15", font_size=30, color=BLUE_B, font="Times new Roman")
        text10.move_to(DOWN * 3.2 + RIGHT * 2)
        self.play(Write(text10))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4), FadeOut(text5), FadeOut(text6),
                  FadeOut(text7), FadeOut(text8), FadeOut(text9), FadeOut(text10))

        # 邻接矩阵
        text1 = Text("接下来让我们用邻接矩阵来表示数据", font_size=30, color=WHITE, font="FangSong")
        text1.move_to(DOWN * 1.2)
        text2 = Text("邻接矩阵的基本用途：存放两两结点之间的距离或权值", font_size=30, color=WHITE, font="FangSong")
        text2.move_to(DOWN * 2)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait()
        self.play(FadeOut(text1))
        self.play(FadeOut(text2))
        adjacency1 = Matrix([[0, 5, 1, "inf", "inf", "inf"], [5, 0, 9, 3, "inf", "inf"], [1, 9, 0, 4, 5, "inf"],
                            ["inf", 3, 4, 0, 13, 14], ["inf", "inf", 5, 13, 0, 15], ["inf", "inf", "inf", 14, 15, 0]])
        adjacency1.move_to(DOWN * 2)
        adjacency1.scale(0.6)
        self.play(ShowCreation(adjacency1), run_time=6)
        self.wait(3)
        self.play(FadeOut(adjacency1), FadeOut(Graph))

        # 开始讲解从第零个到第五个节点的推演过程

        # graph_metrix = VGroup(Graph, adjacency)
        # graph_metrix.to_edge(LEFT)
        # graph_metrix.scale(0.8)
        Graph.to_edge(LEFT)
        Graph.scale(0.8)
        adjacency = Matrix([0, 5, 1, "inf", "inf", "inf"])
        adjacency.next_to(Graph,DOWN)
        adjacency.scale(0.8)
        self.play(ShowCreation(Graph),ShowCreation(adjacency))

        text = Text("首先找到当前的最短路径0-2，得到表1", font_size=30, color=WHITE, font="FangSong")
        text.move_to(RIGHT * 3 + UP * 2.5)
        self.play(ShowCreation(text), run_time=1)
        chart1 = Matrix(
            [["   ", "Sum", "Path"], [1, 5, "0-1"], [2, 1, "0-2"], [3, "inf", "/"], [4, "inf", "/"], [5, "inf", "/"]])
        chart1.move_to(RIGHT * 3 + DOWN * 0.5)
        self.play(ShowCreation(chart1), line2.animate.set_color(RED), run_time=4)
        self.wait(3)
        self.play(FadeOut(text), FadeOut(chart1))

        text1 = Text("找到最短路径0-2后，沿0-2路径方向查找更短的", font_size=20, color=WHITE, font="FangSong")
        text1.move_to(RIGHT * 3 + UP * 2.8)
        self.play(ShowCreation(text1), run_time=1)
        text2 = Text("到达其它顶点的路径，并对表1进行更新,得到表2", font_size=20, color=WHITE, font="FangSong")
        text2.move_to(RIGHT * 3 + UP * 2.3)
        self.play(ShowCreation(text2), run_time=1)
        chart2 = Matrix(
            [["   ", "Sum", "Path"], [1, 5, "0-1"], [2, 1, "0-2"], [3, 5, "0-2-3"], [4, 6, "0-2-4"], [5, "inf", "/"]])
        chart2.move_to(RIGHT * 3 + DOWN * 0.5)
        adjacency1 = Matrix([0, 5, 1, 5, 6, "inf"])
        adjacency1.next_to(Graph,DOWN)
        adjacency1.scale(0.8)
        self.play(ShowCreation(chart2), line5.animate.set_color(RED), line6.animate.set_color(RED) ,FadeOut(adjacency),ShowCreation(adjacency1),run_time=4)
        self.wait(3)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(chart2))

        text1 = Text("接着表二中最小的是第1个点，但是沿0-1路径查找到的0-1-2", font_size=20, color=WHITE, font="FangSong")
        text1.move_to(RIGHT * 2.8 + UP * 2.8)
        self.play(ShowCreation(text1))
        text2 = Text("路径和0-1-3路径的权重都比表二中的大，因此表3不做更新", font_size=20, color=WHITE, font="FangSong")
        text2.move_to(RIGHT * 2.8 + UP * 2.3)
        self.play(ShowCreation(text2))
        chart3 = Matrix(
            [["   ", "Sum", "Path"], [1, 5, "0-1"], [2, 1, "0-2"], [3, 5, "0-2-3"], [4, 6, "0-2-4"], [5, "inf", "/"]])
        chart3.move_to(RIGHT * 3 + DOWN * 0.5)
        self.play(ShowCreation(chart3), run_time=4)
        self.wait(4)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(chart3))

        text1 = Text("接着表三中最小的是第3个点，沿0-2-3路径方向查找", font_size=20, color=WHITE,
                     font="FangSong")
        text1.move_to(RIGHT * 2.8 + UP * 2.8)
        self.play(ShowCreation(text1))
        text2 = Text("路径，更新到第5个点的路径，得到表4", font_size=20, color=WHITE, font="FangSong")
        text2.move_to(RIGHT * 2.8 + UP * 2.3)
        self.play(ShowCreation(text2))
        chart4 = Matrix(
            [["   ", "Sum", " ", "Path"], [1, 5, " ", "0-1"], [2, 1, " ", "0-2"], [3, 5, " ", "0-2-3"],
             [4, 6, " ", "0-2-4"], [5, 19, " ", "0-2-3-5"]])
        chart4.move_to(RIGHT * 3 + DOWN * 0.5)
        adjacency2 = Matrix(["0", 5, 1, 5, 6, 19])
        adjacency2.scale(0.8)
        adjacency2.next_to(Graph,DOWN)
        self.play(FadeOut(adjacency1),ShowCreation(adjacency2))
        self.play(ShowCreation(chart4), line9.animate.set_color(RED), run_time=3)
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(chart4))

        text1 = Text("接着遍历到第4个点，沿0-2-4路径方向查找路径，", font_size=20, color=WHITE,
                     font="FangSong")
        text1.move_to(RIGHT * 2.8 + UP * 2.8)
        self.play(ShowCreation(text1))
        text2 = Text("但是沿该路径查找到的到第5个点的距离都比19大，不做更新", font_size=20, color=WHITE, font="FangSong")
        text2.move_to(RIGHT * 2.8 + UP * 2.3)
        self.play(ShowCreation(text2))
        self.play(line6.animate.set_color(WHITE))
        chart5 = Matrix(
            [["   ", "Sum", " ", "Path"], [1, 5, " ", "0-1"], [2, 1, " ", "0-2"], [3, 5, " ", "0-2-3"],
             [4, 6, " ", "0-2-4"], [5, 19, " ", "0-2-3-5"]])
        chart5.move_to(RIGHT * 3 + DOWN * 0.5)
        self.play(ShowCreation(chart5), run_time=4)
        self.wait(3)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(chart5))

        text = Text("最后第5个点，显然不用更新。", font_size=40, color=WHITE, font="FangSong")
        text.move_to(RIGHT * 3 + UP * 2.5)
        self.play(ShowCreation(text))
        chart6 = Matrix(
            [["   ", "Sum", " ", "Path"], [1, 5, " ", "0-1"], [2, 1, " ", "0-2"], [3, 5, " ", "0-2-3"],
             [4, 6, " ", "0-2-4"], [5, 19, " ", "0-2-3-5"]])
        chart6.move_to(RIGHT * 3 + DOWN * 0.5)
        self.play(ShowCreation(chart6), run_time=3)
        self.wait(1)
        self.play(FadeOut(text), FadeOut(chart6))

        graph_metrix = VGroup(Graph, adjacency2)
        self.play(FadeOut(graph_metrix))
        text = Text("至此，5个结点全部遍历完成得到最短路径为19，路径是0-2-3-5\nDijkstra Algorithm的最后让我们看一看如何用python代码实现", font_size=30, color=WHITE, font="FangSong")
        self.play(ShowCreation(text))
        self.wait(7)
        self.play(FadeOut(text))

        # 代码解析
        text1 = Text("首先我们读入数据", font_size=30, color=BLUE_B, font="FangSong")
        text1.move_to(UP * 1.5)
        self.play(Write(text1))
        text2 = Text(
            "INF = float('inf')\n#定义邻接矩阵 记录各点之间的距离\nweight = [[INF if j != i else 0 for j in range(6)] for i in range(6)]\n#解析数据，其中a是之前的九行数据\nb = [[int(i) for i in i.split(' ')] for i in a.split('\\n') if i != '']\nfor i in b:\n    weight[i[0]][i[1]] = i[2]\n    weight[i[1]][i[0]] = i[2]",
            line_spacing=10, font_size=25, color=WHITE, font="FangSong")
        text2.next_to(text1, DOWN)
        self.play(Write(text2), run_time=5)
        self.play(FadeOut(text1),FadeOut(text2))
        text1 = Text("接着让我们着眼于Dijkstra函数。其中src是起点索引；target是终点索引", font_size=25, color=BLUE_B,
                     font="FangSong")
        text1.move_to(UP * 2.5)
        self.play(Write(text1))
        # "def dijkstra(src, target):\n# 未到的点\nu = [i for i in range(6)]\n# 距离列表\ndist = weight[src][:]\n# 把起点去掉\nu.remove(src)\n# 用于记录最后更新结点\nlast_update = [src if i != INF else -1 for i in dist]\nwhile u != []:\nidx = 0\nmin_dist = INF\n# 找最近的点\nfor i in range(6):\nif i in u and dist[i] < min_dist:\nmin_dist = dist[i]\nidx = i\n# 从未到列表中去掉这个点\nu.remove(idx)\n# 更新dist（借助这个点连接的路径更新dist）\nfor j in range(6):\nif j in u and weight[idx][j] + min_dist < dist[j]:\ndist[j] = weight[idx][j] + min_dist\n# 记录更新该结点的结点编号\nlast_update[j] = idx\n# 输出从起点到终点的路径结点\ntmp = target\npath = []\nwhile tmp != src:\npath.append(tmp)\ntmp = last_update[tmp]\npath.append(src)\nprint(\"->\".join([str(i) for i in reversed(path)]))\nreturn dist[target]"
        text2 = Text("\tdef dijkstra(src, target):\n\t\
        # 未到的点\n\t\
        u = [i for i in range(6)]\n\t\
        # 距离列表\n\t\
        dist = weight[src][:]\n\t\
        # 把起点去掉\n\t\
        u.remove(src)\n\t\
        # 用于记录最后更新结点\n\t\
        last_update = [src if i != INF else -1 for i in dist]\n\t\
        while u != []:\n\t\t\
        idx = 0\n\t\t\
        min_dist = INF\n\t\t\
        # 找最近的点\n\t\t\
        for i in range(6):\n\t\t\
            if i in u and dist[i] < min_dist:\n\t\t\
                min_dist = dist[i]\n\t\t\
                idx = i\n\t",
                     line_spacing=10, font_size=20, color=WHITE, font="FangSong")
        text2.next_to(text1, DOWN)
        self.play(Write(text2), run_time=10)
        self.wait(3)
        self.play(FadeOut(text2))
        text2 = Text("\t\t\t\t#从未到列表中去掉这个点\n\t\t\t\
        u.remove(idx)\n\t\t\t\
        # 更新dist（借助这个点连接的路径更新dist）\n\t\t\
                for j in range(6):\n\t\t\t\
                if j in u and weight[idx][j] + min_dist < dist[j]:\n\t\t\t\t\
                dist[j] = weight[idx][j] + min_dist\n\t\t\t\t\
                # 记录更新该结点的结点编号\n\t\t\t\t\
                last_update[j] = idx\n\t\t\
                # 输出从起点到终点的路径结点\n\t\t\
                tmp = target\n\t\t\
                path = []\n\t\t\
                while tmp != src:\n\t\t\t\
                path.append(tmp)\n\t\t\t\
                tmp = last_update[tmp]\n\t\t\
                path.append(src)\n\t\t\
                print(\"->\".join([str(i) for i in reversed(path)]))\n\t\t\
                return dist[target]",
                     line_spacing=10, font_size=20, color=WHITE, font="FangSong")
        text2.next_to(text1, DOWN)
        self.play(Write(text2), run_time=10)
        self.wait(5)
        self.play(FadeOut(text2),FadeOut(title),FadeOut(text1))

