from ui_components import Stopwatch
import flet as ft


def main(page: ft.Page):
    page.title = 'Stopwatch'
    
    # theme
    page.theme_mode = 'light'
    
    # window geometry
    page.window_height = 350
    page.window_width = 500
    page.window_resizable = False
    
    # alignments
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def change_page(e):
        selected_page = e.control.selected_index
        if selected_page == 0: # main page is opened
            home_view.visible = True
            about_view.visible = False
        elif selected_page == 1: # about page is opened
            home_view.visible = False
            about_view.visible = True
            
        page.update()
    
    def set_light_theme_mode():
        page.theme_mode = 'light'
        
        # all other ui elements get auto-updated with the above statement
        # so, no need to bother about them
        home_view.button_reset.color = '#eeeef1'
        home_view.button_reset.bgcolor = '#43474e'
        
        # change button icon accordingly
        page.floating_action_button.icon = ft.icons.DARK_MODE_SHARP
        page.update()
    
    def set_dark_theme_mode():
        page.theme_mode = 'dark'
        
        # comment is given in the above defined function
        home_view.button_reset.color = '#272a2c'
        home_view.button_reset.bgcolor = '#c3c7cf'
        
        # change button icon accordingly
        page.floating_action_button.icon = ft.icons.LIGHT_MODE_SHARP
        page.update()
    
    def change_theme_mode(e):
        if page.theme_mode == 'light':
            set_dark_theme_mode()
        elif page.theme_mode == 'dark':
            set_light_theme_mode()
        page.update()
    
    page.appbar = ft.AppBar(title=ft.Text('Stopwatch'))
    
    page.drawer = ft.NavigationDrawer(controls=[
        ft.NavigationDrawerDestination(
            label='Home',
            icon=ft.icons.HOME_OUTLINED,
            selected_icon_content=ft.Icon(ft.icons.HOME_SHARP)
        ),
        ft.Divider(thickness=1),
        ft.NavigationDrawerDestination(
            label='About',
            icon=ft.icons.LIGHTBULB_OUTLINED,
            selected_icon_content=ft.Icon(ft.icons.LIGHTBULB_ROUNDED)
        )
    ], selected_index=0, on_change=change_page)
    
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.DARK_MODE_SHARP, on_click=change_theme_mode)

    home_view = Stopwatch()
    
    about_view = ft.Column([
        ft.Text('Written by:', size=40),
        ft.Text('Muhammad Altaaf', size=30),
        ft.Container(content=ft.Divider(thickness=2), width=40),
        ft.OutlinedButton(icon=ft.icons.LINK_ROUNDED, text='Source code')
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    
    page.add(home_view, about_view)

if __name__ == '__main__':
    ft.app(target=main)
