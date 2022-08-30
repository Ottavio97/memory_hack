from app.script_ui.button import Button
from app.script_ui.input import Input

class InputButton(Button):

    def __init__(self, title, interact_callback, enable_checker=None, default_value="1000", validation_checker=None):
        super().__init__(title, interact_callback, enable_checker, Input(validation_checker, default_value))

    def get_value(self):
        return self.input_handler.get_value()

    def is_valid(self):
        return self.input_handler.has_validated_value()

    def get_valid_value(self):
        return self.input_handler.get_validated_value()




