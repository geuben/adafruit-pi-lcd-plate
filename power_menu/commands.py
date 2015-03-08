from helpers import get_console_kit_method
from menu_framework.menu import Menu, MenuItem

class PowerMenu(Menu, MenuItem):
    TEXT = "Power"
    def __init__(self, items):
        super(PowerMenu, self).__init__(items)

class Shutdown(MenuItem):
    TEXT = "Shutdown"

    def select(self, lcd_control):
        print "NOT IMPLEMENTED"
        print "Shutting down..."
        get_console_kit_method('Stop')()

class Reboot(MenuItem):
    TEXT = "Reboot"

    def select(self, lcd_control):
        get_console_kit_method('Restart')()
