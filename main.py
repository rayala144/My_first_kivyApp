import kivy
# import kivy.uix
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('2.1.0')


class MyRoot(BoxLayout):
    def __int__(self):
        super(MyRoot, self).__init__()

    def generate_num(self):
        self.random_Label.text = str(random.randint(0, 1000))
        # self.random_Label.font_size = random.randint(50, 100)


class NeuralRandom(App):
    def build(self):
        return MyRoot()


neuralRandom = NeuralRandom()
neuralRandom.run()
