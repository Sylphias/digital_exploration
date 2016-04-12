from kivy.app import App 
from kivy.uix.label import Label  

class AlternateApp(App):
	
  def build(self):
    self.label = Label(text='hello', on_touch_down=self.alternate ) 
    return self.label

  def alternate(self,instance, touch):
    self.label.text = 'mouse touch down occurs'
    pass


myapp=AlternateApp()
myapp.run()