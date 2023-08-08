from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
'''
https://www.youtube.com/watch?v=l8Imtec4ReQ
Kivy Course - Create Python Games and Mobile Apps
01:25:41
'''

class WidgetsExample(GridLayout):
    count_enabled = BooleanProperty(False)
    count = 1
    my_text = StringProperty('1')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_button_click(self, button_widget):
        print('Button clicked')
        if self.count_enabled == False:
            self.count += 1
            self.my_text = str(self.count)
    def on_toggle_button_state(self, toggle_button_widget):
        print('toggle state :', toggle_button_widget.state)
        if toggle_button_widget.state == 'normal':
            toggle_button_widget.text = 'OFF'
            self.count_enabled = False
        elif toggle_button_widget.state == 'down':
            toggle_button_widget.text = 'ON'
            self.count_enabled = True
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'lr-bt'
        for i in range(0, 100):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(
                text=str(i + 1), size_hint=(None, None), size=(size, size))
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