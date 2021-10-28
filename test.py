from manim import *



class MoveText(Scene):
    def construct(self):
        formula = MathTex("2x", " - ", "3", " = y", color=BLUE)
        formula1 = MathTex("2x", "-", "3", "= y", "+", "3", color=BLUE)
        self.play(Write(formula))
        formula2 = MathTex("+", "3", color=BLUE).next_to(formula1[3], RIGHT)#.shift(LEFT)
        formula3 = MathTex("2x", color=BLUE).align_to(formula[2])
        self.play(Transform(formula[2], formula2), FadeOut(formula[1]), Transform(formula[0], formula3))

class DynamicProgramming(Scene):
    
    def title(self):
        code = Text("COMP3121/9101", color = BLUE)
        title = Text("Dynamic Programming", color = BLUE).shift(DOWN)
        self.play(Write(code))
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(code), FadeOut(title))
    
    def chapter1(self):
        text = "What is dynamic programming?"
        text1 = Text(text, color = BLUE)
        text2 = Text(text, color = BLUE).to_edge(UP).scale(0.75)
        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1, text2))

        table = MathTable(
            [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
            include_outer_lines = True
            )
        self.play(Write(table))

    def construct(self):
        self.title()
        self.chapter1()