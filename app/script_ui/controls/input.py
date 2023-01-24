from .base_control import BaseControl

class Input(BaseControl):

    def __init__(self, on_change: callable, readonly=False, **kwargs): #values should a (value, text) tuple
        super().__init__(**kwargs)
        self.text = "" if 'text' not in kwargs else kwargs['text']
        self.trigger_by_focus = True if 'trigger_by_focus' not in kwargs else kwargs['trigger_by_focus']
        self.on_change = on_change
        self.readonly = readonly

    def set_on_change(self, on_change:callable):
        self.on_change = on_change

    def build(self, id_map: {}):
        id_map[self.script_ids[-1]] = self
        if not self.trigger_by_focus:
            return '<ons-input id="{}" style="width:100%;" class="text-input text-input--material r-value" autocomplete="chrome-off" autocapitalize="off" modifier="underbar" value="{}" oninput="script.script_interact_value(event)" float {}></ons-input>'.format(self.script_ids[-1], self.text, 'readonly' if self.readonly else '')
        else:
            return '<ons-input id="{}" style="width:100%;" class="text-input text-input--material r-value" autocomplete="chrome-off" autocapitalize="off" modifier="underbar" value="{}" onchange="script.script_interact_value(event)" float {}></ons-input>'.format(self.script_ids[-1], self.text, 'readonly' if self.readonly else '')


    def handle_interaction(self, _id: str, data):
        self.text = data['value']
        if self.on_change:
            self.on_change(self.get_id(), _id, data)
        return super().handle_interaction(_id, data)

    def set_text(self, text):
        self.text = text
        [self.update_queue.put({'op': "value", 'data': {'value': self.text, 'id': x}}) for x in self.script_ids]

    def get_text(self):
        return self.text

    def on_reload(self):
        if self.text is not None:
            self.set_text(self.text)
        super().on_reload()





