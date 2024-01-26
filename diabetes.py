from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GlicemiaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        layout.add_widget(Label(text="Nome:"))
        self.nome_input = TextInput()
        layout.add_widget(self.nome_input)

        layout.add_widget(Label(text="Idade:"))
        self.idade_input = TextInput()
        layout.add_widget(self.idade_input)

        layout.add_widget(Label(text="Data:"))
        self.data_input = TextInput()
        layout.add_widget(self.data_input)

        layout.add_widget(Label(text="Horário:"))
        self.horario_input = TextInput()
        layout.add_widget(self.horario_input)

        layout.add_widget(Label(text="Glicemia:"))
        self.glicemia_input = TextInput()
        layout.add_widget(self.glicemia_input)

        processar_button = Button(text="Processar", on_press=self.processar_dados)
        layout.add_widget(processar_button)

        limpar_button = Button(text="Limpar", on_press=self.limpar_campos)
        layout.add_widget(limpar_button)

        self.resultado_label = Label(text="")
        layout.add_widget(self.resultado_label)

        return layout

    def processar_dados(self, instance):
        nome = self.nome_input.text
        idade = self.idade_input.text
        data = self.data_input.text
        horario = self.horario_input.text

        try:
            glicemia = int(self.glicemia_input.text)
            resultado = "Glicemia Elevada" if glicemia > 160 else "Siga em frente"
            self.resultado_label.text = f"Nome: {nome}\nIdade: {idade}\nData: {data}\nHorário: {horario}\nGlicemia: {glicemia}\n{resultado}"
        except ValueError:
            self.resultado_label.text = "Por favor, insira um valor numérico para a glicemia."

    def limpar_campos(self, instance):
        self.nome_input.text = ""
        self.idade_input.text = ""
        self.data_input.text = ""
        self.horario_input.text = ""
        self.glicemia_input.text = ""
        self.resultado_label.text = ""

if __name__ == '__main__':
    GlicemiaApp().run()
