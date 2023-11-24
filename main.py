

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#f8rom kivy.uix.canvas import Canvas



kv1 = """
<FastCalMan>:
    
    canvas:
        Color:
            rgba: 0.334,0.34,1,1
        Rectangle:
            size: self.size
    
    orientation: 'vertical'
    spacing: 20
    padding: '20dp','20dp','20dp','40dp'
    
    
    
    
    BoxLayout:
        
        Label:
            text: 'FASTCALMAN'
            font_size: '30sp'
        Button:
            text: "ABOUT"
            size_hint_x: None
            width: "200px"
            background_normal: ""
            background_color: 1,.2,.2,1
            on_release: 
    BoxLayout:
        
        size_hint_x: None
        width: "800px"
        Label:
            text: 'MIL'
        TextInput:
            font_size: '25sp'
            id: mil
    BoxLayout:
        
        size_hint_x: None
        width:"800px"
        Label:
            text: 'QUINHETOS'
        TextInput:
            font_size: '25sp'
            id: qui
    BoxLayout:
        
        size_hint_x: None
        width: "800px"
        Label:
            text: 'DUZENTOS'
        TextInput:
            font_size: '25sp'
            id: duz
    BoxLayout:
        
        size_hint_x: None
        width: "800px"
        Label:
            text: 'CEM'
        TextInput:
            font_size: '25sp'
            id: cem
    BoxLayout:
        
        size_hint_x: None
        width: "800px"
        Label:
            text: 'CINQUENTA'
        TextInput:
            font_size: '25sp'
            id: cim
    BoxLayout:
        
        size_hint_x: None
        width: "800px"
        Label:
            text: 'VINTE'
        TextInput:
            id: vin
            font_size: '25sp'
    Label:
        id: resul
        text: ' campo de resultado...'
        font_size: '26sp'
    Button:
        text: 'calcular'
        on_press: root.calcular()
        background_normal: ""
        background_color: 0.1,0.95,0.1,0.8
    




"""
Builder.load_string(kv1)

class FastCalMan(BoxLayout):
    def calcular(self):
        
        mil1 = self.ids.mil.text
        qui1 = self.ids.qui.text
        duz1 = self.ids.duz.text
        cem1 = self.ids.cem.text
        cim1 = self.ids.cim.text
        vin1 = self.ids.vin.text
        
        mil2 = 0
        qui2= 0
        duz2 = 0
        cem2 = 0
        cim2 = 0
        vin2 = 0
        
        if mil1 != "":
            mil2 = int(mil1)*1000
        
        if qui1 != "":
            qui2 = int(qui1)*500
        
        if duz1 != "":
            duz2 = int(duz1)*200
        
        if cem1 != "":
            cem2 = int(cem1)*100
        
        if cim1 != "":
            cim2 = int(cim1)*50
        
        if vin1 != "":
            vin2 = int(vin1)*20
        resul = mil2+qui2+duz2+cem2+cim2+vin2
        
        self.ids.resul.text = str(resul)+" MTS"
        

class construtor(App):
    def build(self):
        return FastCalMan()
 
 
 
 
construtor().run()
 
 
