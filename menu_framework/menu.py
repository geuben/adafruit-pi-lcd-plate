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

    def select(self, lcd_control):
        lcd_control.clear()
        if self._active:
            return self._select(lcd_control)
        else:
            if not self._items[self._pos].select(lcd_control):
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

    def _select(self, lcd_control):
        if isinstance(self._items[self._pos], Menu):
            self._active = False
            return True
        elif isinstance(self._items[self._pos], Back):
            return False
        else:
            self._items[self._pos].select(lcd_control)
        return True

class MenuItem(object):
    TEXT = "NOT DEFINED"
    def __init__(self):
        pass

    def select(self, lcd_control):
        print "NOT IMPLEMENTED"
        return True

    @property
    def text(self):
        return self.TEXT

class Back(MenuItem):
    TEXT = "Back"
