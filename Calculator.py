from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Calculator(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        output = Label(size_hint_y = 0.75, font_size=50)
        buttons = ('1', '2', '3', '+',
                   '4', '5', '6', '-',
                   '7', '8', '9', '.',
                   '0', '*', '/', '=')
        grid = GridLayout(cols=4, size_hint_y=2)
        for button in buttons:
            grid.add_widget(Button(text=button))

        clearButton = Button(text='Clear', size_hint_y=None, height=100)
        def print_button_text(instance):
            output.text += instance.text
        for button in grid.children[1:]:
            button.bind(on_press=print_button_text)
        def resize_label_text(label, new_height):
            label.fontsize = 1.8*label.height
        output.bind(height=resize_label_text)

        def evaluate_result(instance):
            try:
                output.text = str(eval(output.text))
            except SyntaxError:
                output.text = 'Python Syntax error! Rerun Program.'
        grid.children[0].bind(on_press=evaluate_result)

        def clear_label(instance):
            output.text = " "
        clearButton.bind(on_press=clear_label)
        root.add_widget(output)
        root.add_widget(grid)
        root.add_widget(clearButton)

        return root
Calculator().run()
