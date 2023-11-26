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
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
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
    
    
    digital_clock = ft.Text(str(datetime.timedelta(seconds=0)), size=60)
    
    button_start = ft.IconButton(icon=ft.icons.START_SHARP, on_click=start_watch)  # start button
    button_stop  = ft.IconButton(icon=ft.icons.STOP_CIRCLE_SHARP, on_click=stop_watch)  # stop button
    button_reset = ft.ElevatedButton(text='0', on_click=reset_watch, color='#272a2c', bgcolor='#c3c7cf')  # reset button

    main_page = ft.Column([
        digital_clock,
        ft.Row([
            button_start,
            button_stop,
            button_reset
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(main_page)


if __name__ == '__main__':
    ft.app(target=main)
