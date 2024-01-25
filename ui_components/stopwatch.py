import time, datetime
import flet as ft


class Stopwatch(ft.Column):
    def __init__(
        self,
        digits_size: float | None = 60,
        buttons_size: float | None = 40,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.digital_clock = ft.Text(
            str(datetime.timedelta(seconds=0)), size=digits_size
        )

        self.button_start = ft.IconButton(
            icon=ft.icons.START_SHARP, icon_size=buttons_size, on_click=self.start_watch
        )  # start button
        self.button_stop = ft.IconButton(
            icon=ft.icons.STOP_CIRCLE_SHARP,
            icon_size=buttons_size,
            on_click=self.stop_watch,
        )  # stop button
        self.button_reset = ft.ElevatedButton(
            text="0", on_click=self.reset_watch, color="#eeeef1", bgcolor="#43474e"
        )  # reset button

        self.controls = [
            self.digital_clock,
            ft.Row(
                [self.button_start, self.button_stop, self.button_reset],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ]

        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.seconds_passed = 0
        self.running_clock_instances = 0
        self.is_clock_running = True

    def start_watch(self, e):
        if (
            self.running_clock_instances == 1
        ):  # indicates that function has been called before once
            return
        if self.is_clock_running == False:
            self.is_clock_running = True
        self.running_clock_instances += 1
        while self.is_clock_running:
            time.sleep(1)
            self.seconds_passed += 1
            self.digital_clock.value = str(
                datetime.timedelta(seconds=self.seconds_passed)
            )
            self.page.update()

    def stop_watch(self, e):
        self.is_clock_running = False
        self.running_clock_instances = 0
        self.page.update()

    def reset_watch(self, e):
        self.seconds_passed = 0
        self.digital_clock.value = str(datetime.timedelta(seconds=self.seconds_passed))
        self.page.update()

    def build(self):
        return self
