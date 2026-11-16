from kivy.app import App
from kivy.uix.label import Label

from app.database.models import inicializar_base_datos


class HydrocalafquenApp(App):
    title = "Hydrocalafquen"

    def build(self):
        return Label(text="Hydrocalafquen\nBitácora de apnea")


if __name__ == "__main__":
    inicializar_base_datos()
    HydrocalafquenApp().run()