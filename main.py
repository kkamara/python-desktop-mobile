from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
'''
https://www.youtube.com/watch?v=l8Imtec4ReQ
Kivy Course - Create Python Games and Mobile Apps
00:13:31
'''

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b = Button(text='Z', size_hint=(.2, .2))
        self.add_widget(b)
# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
'''    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'vertical'
        b1 = Button(text='A')
        b2 = Button(text='B')
        b3 = Button(text='C')
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
'''
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

if __name__ == "__main__":
    TheLabApp().run()