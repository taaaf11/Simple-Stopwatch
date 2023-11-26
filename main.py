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
    page.theme_mode = 'dark'
    
    # window geometry
    page.window_height = 300
    page.window_width = 500
    page.window_resizable = False
    
    
    def start_watch(e):
        global seconds_passed, is_clock_running, running_clock_instances
        if running_clock_instances == 1: # indicates that function has called before
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
        if selected_page == 0:
            main_page.visible = True
            about_page.visible = False
        elif selected_page == 1:
            main_page.visible = False
            about_page.visible = True
        page.update()
        page.drawer.open = False # closing the drawer
        page.drawer.update()
    
    
    digital_clock = ft.Text(str(datetime.timedelta(seconds=0)), size=60)
    
    button_start = ft.IconButton(icon=ft.icons.START_SHARP, on_click=start_watch)  # start button
    button_stop  = ft.IconButton(icon=ft.icons.STOP_CIRCLE_SHARP, on_click=stop_watch)  # stop button
    button_reset = ft.ElevatedButton(text='0', on_click=reset_watch, color='#272a2c', bgcolor='#c3c7cf')  # reset button
    
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
    
    
    about_page = ft.Row([ft.Column([
        ft.Text(value='Written By:', size=40),
        ft.Text(value='Muhammad Altaaf', size=20)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)],
                        alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    
    page.drawer = ft.NavigationDrawer(controls=[
        navigation_drawer_home,
        navigation_drawer_about
    ], selected_index=0, on_change=change_page)
    
    page.add(drawer_button)
    page.add(ft.Column([main_page, about_page]))


if __name__ == '__main__':
    ft.app(target=main)
