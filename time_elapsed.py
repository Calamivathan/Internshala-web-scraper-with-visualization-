import time
import tkinter as tk

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop_and_print(self):
        if self.start_time is None:
            raise Exception("Timer was not started.")
        end_time = time.time()
        execution_time = end_time - self.start_time
        minutes, seconds = divmod(execution_time, 60)
        minutes = int(minutes)
        seconds = int(seconds)
        time_format = "{:02d}min {:02d}sec".format(minutes, seconds)
        print("Total execution time:", time_format)
        self._show_popup(time_format)

    def _show_popup(self, time_format):
        root = tk.Tk()
        root.title("Execution Time")
        label = tk.Label(root, text=f"Total execution time: {time_format}", padx=20, pady=20)
        label.pack()
        button = tk.Button(root, text="OK", command=root.destroy, padx=20, pady=10)
        button.pack()
        root.mainloop()
