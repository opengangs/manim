from manim import *
import numpy as np

class MovingDot(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        axes = Axes(
            x_range = [-1, 1],
            y_range = [-1, 1],
            x_length = 10,
            #y_length = 10,
            tips = False
        )

        sin = axes.get_graph(lambda x : np.sqrt(1 - x * x), color = GREEN, x_range = [-1, 1])
        Min = Dot(axes.i2gp(sin.t_min, sin))
        moving_dot = Dot(axes.i2gp(sin.t_min, sin), color = ORANGE)
        Max = Dot(axes.i2gp(sin.t_max, sin), color = BLUE)
        #cos = axes.get_graph(lambda x : np.cos(x), color = BLUE)
        #tan = axes.get_graph(lambda x : np.tan(x), color = RED)
        #sinh = axes.get_graph(lambda x : np.sinh(x), color = RED)

        self.add(axes, sin, Min, Max, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_center(mob):
            mob.move_to(moving_dot.get_center())
        
        self.camera.frame.add_updater(update_center)
        self.play(MoveAlongPath(moving_dot, sin, rate_func = rate_functions.exponential_decay))
        self.camera.frame.remove_updater(update_center)

        self.play(Restore(self.camera.frame))