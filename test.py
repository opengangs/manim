from manim import *

class Test1(Scene):
    def construct(self):
        text = MathTex("\\frac{d}{dx}\left(f(x) \cdot g(x)\\right) = f'(x) \cdot g(x) + f(x) \cdot g'(x)")
        self.play(Write(text))