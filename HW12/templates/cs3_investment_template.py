from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


class Investment(App):

	def build(self):
		layout= GridLayout(cols=2)
		layout.add_widget(Label(text="Investment Ammount", halign='left'))
		pass
		btn = Button(text="Calculate", on_press=self.calculate)
		layout.add_widget(btn)
		return layout

	def calculate(self, instance):
		invAmt = None
		years = None
		mthIntRate = None
		self.txtFutureVal.text= None



Investment().run()