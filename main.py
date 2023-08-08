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
01:37:34
'''

class TheLabApp(App):
    '''
    Mainclass must be in this format.
    TheLabApp for TheLab.kv
    '''
    pass

class CanvasExample1(Widget):
    pass

if __name__ == "__main__":
    TheLabApp().run()