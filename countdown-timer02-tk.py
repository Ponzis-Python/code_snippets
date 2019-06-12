#https://codereview.stackexchange.com/questions/184326/basic-countdown-timer
#Stop button added by Ponzi
import tkinter as tk
import datetime

class Countdown(tk.Frame):
    '''A Frame with label to show the time left, an entry to input the seconds to count
    down from, and a start button to start counting down.'''
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()
        self.entry.pack()
        self.start.pack(side=tk.LEFT)
        self.stop.pack(side=tk.LEFT)

    def create_widgets(self):

        self.label = tk.Label(self, text="00:00:00")
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()
        self.start = tk.Button(self, text="Start", command=self.start_button)
        self.stop = tk.Button(self, text="Stop", command=self.stop_timer)

    def countdown(self):
        '''Update label based on the time left.'''
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False

    def start_button(self):
        '''Start counting down.'''
        self.seconds_left = int(self.entry.get())   # 1. to fetch the seconds
        self.stop_timer()                           # 2. to prevent having multiple
        self.countdown()                            #    timers at once

#    def stop_button(self):

#        if self._timer_on:
#            self._timer_on = False

    def stop_timer(self):
        '''Stops after schedule from executing.'''
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):

        return datetime.timedelta(seconds=self.seconds_left)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)

    countdown = Countdown(root)
    countdown.pack()

    root.mainloop()