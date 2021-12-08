from kivy.app import App
from kivy.graphics import Ellipse, Rectangle, Color
from kivy.metrics import dp
from kivy.properties import Clock, StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass


class BallApp(App):
    pass


class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("0")
    count_enabled = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
        self.ball_size = dp(25)
        with self.canvas:
            self.ball = Ellipse(pos=(3*self.center_x, 6*self.center_y), size=(self.ball_size, self.ball_size))
        self.rect1 = False
        self.rect2 = False
        self.rect3 = False
        self.rect4 = False
        self.i = 0


    def on_button_up_click(self):
        x, y = self.ball.pos
        if y + 1.2*self.ball_size< self.height:
            y += 10
            self.ball.pos = (x, y)


    def on_button_right_click(self):
        x, y = self.ball.pos
        if x + 1.2*self.ball_size < self.width:
            x += 10
            self.ball.pos = (x, y)

    def on_button_down_click(self):
        x, y = self.ball.pos
        if y > self.height*1/5:
            y -= 10
            self.ball.pos = (x, y)

    def on_button_left_click(self):
        x, y = self.ball.pos
        if x > 0:
            x -= 10
            self.ball.pos = (x, y)

    def on_any_button_click(self):

        x, y = self.ball.pos
        if x > 80 and x < 120 and y > 480 and y < 520:
            with self.canvas:
                Color(0, 1, 0)
                Rectangle(pos=(100, 500), size=(15, 15))
            self.rect1 = True

        if x > 480 and x < 520 and y > 380 and y < 420:
            with self.canvas:
                Color(0, 1, 0)
                Rectangle(pos=(500, 400), size=(15, 15))
            self.rect2 = True


        if x > 180 and x < 220 and y > 330 and y < 370:
            with self.canvas:
                Color(0, 1, 0)
                Rectangle(pos=(200, 350), size=(15, 15))
            self.rect3 = True

        if x > 680 and x < 720 and y > 180 and y < 220:
            with self.canvas:
                Color(0, 1, 0)
                Rectangle(pos=(700, 200), size=(15, 15))
            self.rect4 = True

    def update(self, dt):
        if self.rect1 is False or self.rect2 is False or self.rect3 is False or self.rect4 is False:
            self.i += 1
            self.my_text = str(self.i)

    def on_button_start_click(self):
        self.ball_size = dp(25)
        with self.canvas:
            Color(1, 0, 0)
            Rectangle(pos=(100, 500), size=(15, 15))
            Rectangle(pos=(500, 400), size=(15, 15))
            Rectangle(pos=(200, 350), size=(15, 15))
            Rectangle(pos=(700, 200), size=(15, 15))

BallApp().run()
