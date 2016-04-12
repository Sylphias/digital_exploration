from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
	def build(self):
		self.main = Label(text='Slide Me', on_touch_move = self.detect)
		return self.main
	def detect(self, instance, touch):
		if not instance.collide_point(touch.x, touch.y):
			return False
		if touch.dx<-40:
			self.main.text ="Slide Left"
		if touch.dx>40:
			self.main.text = "Slide Right"
		if touch.dy<-40:
			self.main.text = "Slide Down"
		if touch.dy>40:
			self.main.text = "Slide Up"
		return True

if __name__=='__main__':
	SlideDetectApp().run()