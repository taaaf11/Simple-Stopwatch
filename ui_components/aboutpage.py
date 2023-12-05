import flet as ft


class AboutPage(ft.Column):
    def __init__(self, author_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author_name = author_name
        self.controls = [
            ft.Text('Written by:', size=40),
            ft.Text(self.author_name, size=30)
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def build(self):
        return self
