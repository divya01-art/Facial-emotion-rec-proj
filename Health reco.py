import ipywidgets as widgets
from IPython.display import display

def button_click_eventhandler(button1):
    print(""" Here's your health recommendation:
    1. Get regular exercise. Just 30 minutes of walking every day can boost your mood and improve your health.
    2. Eat healthy, regular meals and stay hydrated.
    3. Make sleep a priority.

    STAY FIT, STAY HEALTHY, STAY HAPPY !!!
    """)

button1 = widgets.Button(description="Health Recommendation")

button1.on_click(button_click_eventhandler)

display(button1)
