class Menu(object):
    def __init__(self, items):
        self._items = items
        self._items.append(Back())
        self._pos = 0
        self._active = True
 
    def items(self):
        return self._items

    def num_items(self):
        return len(self._items)

    def message(self):
        if self._active:
            return self._message()
        else:
            return self._items[self._pos].message()

    def _message(self):
        if self._pos == (self.num_items() - 1):
            return "> " + self._items[self._pos].text
        else:
            return "> " + self._items[self._pos].text + "\n- " + self._items[self._pos+1].text

    def up(self):
        if self._active:
            self._up()
        else:
            self._items[self._pos].up()

    def down(self):
        if self._active:
            self._down()
        else:
            self._items[self._pos].down()

    def select(self):
        if self._active:
            return self._select()
        else:
            if not self._items[self._pos].select():
                self._active = True
                return False
            else:
                return True

    def _down(self):
        if self._pos < (len(self._items) - 1):
            self._pos += 1

    def _up(self):
        if self._pos > 0:
            self._pos -= 1

    def _select(self):
        if isinstance(self._items[self._pos], Menu):
            self._active = False
            return True
        elif isinstance(self._items[self._pos], Back):
            return False
        else:
            self._items[self._pos].select()
        return True

class MenuItem(object):
    TEXT = "NOT DEFINED"
    def __init__(self):
        pass

    def select(self):
        print "NOT IMPLEMENTED"
        return True

    @property
    def text(self):
        return self.TEXT


class NetworkMenu(Menu, MenuItem):
    TEXT = "Networking"
    def __init__(self, items):
        super(NetworkMenu, self).__init__(items)

class Back(MenuItem):
    TEXT = "Back"

class IpAddress(MenuItem):
    TEXT = "IP Address"

class DHCP(MenuItem):
    TEXT = "DHCP"

class PowerMenu(Menu, MenuItem):
    TEXT = "Power"
    def __init__(self, items):
        super(PowerMenu, self).__init__(items)

class Shutdown(MenuItem):
    TEXT = "Shutdown"

    def select(self):
        print "Shutting down..."

class Reboot(MenuItem):
    TEXT = "Reboot"

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
        main_menu.select()
        lcd.clear()
        lcd.message(main_menu.message())
