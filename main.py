from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '650')

from kivymd.app import MDApp

from screens.tutorialfour.tutorialfour import TutorialFour

class MainApp(MDApp):
    def build(self):
        self.title = 'Kivy/kivyMD Tutorials'
        
    def on_start(self):
        self.root.current= 'tutorial_four'
        
if __name__ == '__main__':
    MainApp().run()