import flet as ft
import time, datetime

seconds_passed = 0

def main(page):
    page.title = 'Stopwatch'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def start_watch(e):
        global seconds_passed
        while True:
            time.sleep(1)
            seconds_passed += 1
            digital_clock.value = str(datetime.timedelta(seconds=seconds_passed))
            page.update()
            
    
    digital_clock = ft.Text(str(datetime.timedelta(seconds=0)))
    
    button_start = ft.IconButton(icon=ft.icons.START_SHARP, on_click=start_watch) # start button
    button_stop  = ft.IconButton(icon=ft.icons.STOP_CIRCLE_SHARP) # stop button
    button_reset = ft.ElevatedButton(text='0') # reset button

    main_page = ft.Column([
        digital_clock,
        ft.Row([
            button_start,
            button_stop,
            button_reset
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(main_page)


if __name__ == '__main__':
    ft.app(target=main)
