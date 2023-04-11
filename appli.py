from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import bluetooth_communication as bc


class Commande(BoxLayout):
    def crea_button(self, text, function=0):
        button = Button()
        button.text = text
        if function !=0 :
            button.bind(on_press= bc.bluetooth_cmd)
        self.add_widget(button)
        return button
    
    def crea_Label(self, text):
        label = Label()
        label.text = text
        self.add_widget(label)
        return label

    def build (self):
        self.orientation="vertical"
        self.texte = self.crea_Label(" Télécommande ")
        self.up = self.crea_button("up",1)
        self.up = self.crea_button("down",1)
        self.up = self.crea_button("right",1)
        self.up = self.crea_button("left",1)


    

class telecommandeApp(App):
    
    def build(self):
        layout=Commande()
        layout.build()
        return layout


if __name__ == '__main__':
     
    telecommandeApp().run()