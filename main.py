import flet as ft
import time, datetime

seconds_passed = 0
is_clock_running = True

# number of calls to start_watch
# it is used when the user presses the start button
# when the watch label is 'working'
running_clock_instances = 0 

def main(page):
    page.title = 'Stopwatch'
    
    # theme
    page.theme_mode = 'light'
    
    # window geometry
    page.window_height = 300
    page.window_width = 500
    page.window_resizable = False
    
    
    def start_watch(e):
        global seconds_passed, is_clock_running, running_clock_instances
        if running_clock_instances == 1: # indicates that function has been called before once
            return
        if is_clock_running == False:
            is_clock_running = True
        running_clock_instances += 1
        while is_clock_running:
            time.sleep(1)
            seconds_passed += 1
            digital_clock.value = str(datetime.timedelta(seconds=seconds_passed))
            page.update()
    
    
    def stop_watch(e):
        global is_clock_running, running_clock_instances
        is_clock_running = False
        running_clock_instances = 0
        page.update()
    
    
    def reset_watch(e):
        global seconds_passed
        seconds_passed = 0
        digital_clock.value = str(datetime.timedelta(seconds=seconds_passed))
        page.update()
    
    
    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()
    
    
    def change_page(e):
        selected_page = e.control.selected_index
        if selected_page == 0: # main page is opened
            main_page.visible = True
            about_page.visible = False
            settings_page.visible = False
        elif selected_page == 1: # settings page is opened
            main_page.visible = False
            about_page.visible = False
            settings_page.visible = True
        elif selected_page == 2: # settings page is opened
            main_page.visible = False
            about_page.visible = True
            settings_page.visible = False
        page.update()
        page.drawer.open = False # closing the drawer
        page.drawer.update()
    
    
    def set_light_theme_mode():
        page.theme_mode = 'light'
        
        # all other ui elements got auto-updated with the above statement
        # so, no need to bother about them
        button_reset.color = '#eeeef1'
        button_reset.bgcolor = '#43474e'
        page.update()
        
    
    def set_dark_theme_mode():
        page.theme_mode = 'dark'
        
        # comment is given in the above defined function
        button_reset.color = '#272a2c'
        button_reset.bgcolor = '#c3c7cf'
        page.update()
    
    
    def change_theme_mode(e):
        if dropdown_theme_menu_settings.value == 'Dark':
            set_dark_theme_mode()
        elif dropdown_theme_menu_settings.value == 'Light':
            set_light_theme_mode()
        page.update()
    
    
    digital_clock = ft.Text(str(datetime.timedelta(seconds=0)), size=60)
    
    button_start = ft.IconButton(icon=ft.icons.START_SHARP, on_click=start_watch)  # start button
    button_stop  = ft.IconButton(icon=ft.icons.STOP_CIRCLE_SHARP, on_click=stop_watch)  # stop button
    button_reset = ft.ElevatedButton(text='0', on_click=reset_watch, color='#eeeef1', bgcolor='#43474e')  # reset button
    
    drawer_button = ft.Row([
            ft.IconButton(icon=ft.icons.MENU, on_click=show_drawer)],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
    
    navigation_drawer_home = ft.NavigationDrawerDestination(
        label='Home',
        icon=ft.icons.HOME_OUTLINED,
        selected_icon_content=ft.Icon(ft.icons.HOME_SHARP)
    )
    
    navigation_drawer_settings = ft.NavigationDrawerDestination(
        label='Settings',
        icon=ft.icons.SETTINGS_OUTLINED,
        selected_icon_content=ft.Icon(ft.icons.SETTINGS_SHARP)
    )
    
    navigation_drawer_about = ft.NavigationDrawerDestination(
        label='About',
        icon=ft.icons.LIGHTBULB_OUTLINED,
        selected_icon_content=ft.Icon(ft.icons.LIGHTBULB_ROUNDED)
    )

    main_page = ft.Column(controls=[
        digital_clock,
        ft.Row(controls=[
            button_start,
            button_stop,
            button_reset
        ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=True)
    
    dropdown_theme_menu_settings = ft.Dropdown(label='Theme', options=[
            ft.dropdown.Option('Light'),
            ft.dropdown.Option('Dark')], on_change=change_theme_mode)
    
    settings_page = ft.Row([       # Theme Related
        ft.Text('Theme: '),
        dropdown_theme_menu_settings
    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    
    about_page = ft.Row([ft.Column([
        ft.Text(value='Written By:', size=40),
        ft.Text(value='Muhammad Altaaf', size=20)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)],
                        alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    
    page.drawer = ft.NavigationDrawer(controls=[
        navigation_drawer_home,
        navigation_drawer_settings,
        ft.Divider(thickness=1),
        navigation_drawer_about
    ], selected_index=0, on_change=change_page)
    
    page.add(drawer_button)
    page.add(ft.Column([main_page, settings_page, about_page]))


if __name__ == '__main__':
    ft.app(target=main)
