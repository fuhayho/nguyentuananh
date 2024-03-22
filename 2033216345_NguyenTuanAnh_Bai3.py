from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
          for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    def button_1_click(self, **event_args):
        input_numbers = self.text_box_1.text.strip().split()
        input_numbers = [int(num) for num in input_numbers]
       
        self.bubble_sort(input_numbers)
       
        self.text_box_2.text = ' '.join(map(str, input_numbers))

    def text_box_2_pressed_enter(self, **event_args):
        pass

    def text_box_1_pressed_enter(self, **event_args):
        pass