from menu_framework.menu import Menu, MenuItem
from power_menu.commands import PowerMenu, Shutdown, Reboot
from network_menu.commands import NetworkMenu, IpAddress, DHCP

class AboutItem(MenuItem):
    TEXT = "About"
    def __init__(self):
        pass



import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

main_menu = Menu(
    [
        NetworkMenu(
            [
                IpAddress(),
                DHCP()
            ]
        ),
        PowerMenu(
            [
                Shutdown(),
                Reboot()
            ]
        ),
        AboutItem(),
    ]
)

lcd.message(main_menu.message())
while True:
    if lcd.is_pressed(LCD.DOWN):
        while lcd.is_pressed(LCD.DOWN):
            pass
        main_menu.down()
        lcd.clear()
        lcd.message(main_menu.message())
    if lcd.is_pressed(LCD.UP):
        while lcd.is_pressed(LCD.UP):
            pass
        main_menu.up()
        lcd.clear()
        lcd.message(main_menu.message())
    if lcd.is_pressed(LCD.SELECT):
        while lcd.is_pressed(LCD.SELECT):
            pass
        lcd.clear()
        main_menu.select(lcd)
        lcd.clear()
        lcd.message(main_menu.message())
