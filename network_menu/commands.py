from menu_framework.menu import Menu, MenuItem
import netifaces

class NetworkMenu(Menu, MenuItem):
    TEXT = "Networking"
    def __init__(self, items):
        super(NetworkMenu, self).__init__(items)

class IpAddress(MenuItem):
    TEXT = "IP Address"

    def _get_interface_ip(self, interface):
        interface_info = netifaces.ifaddresses(interface)
        ip_address = "None"
        if 2 in interface_info:
            ip_address = interface_info[2][0]['addr']
        return ip_address

    def select(self, lcd_control):
        interfaces = netifaces.interfaces()
        interfaces.remove('lo') 
        message = interfaces[0] + ":" + self._get_interface_ip(interfaces[0])
        line_lengths = [len(message)]
        if len(interfaces) > 1:
            message += "\n" 
            line2 = interfaces[1] + ":" + self._get_interface_ip(interfaces[1])
            message += line2
            line_lengths.append(len(line2))
        lcd_control.message(message)
        max_line_length = max(line_lengths)
                
        import time
        if max_line_length > 16:
            for digit in xrange(16, max_line_length):
                lcd_control.DisplayLeft()
                time.sleep(0.5)
        time.sleep(5)

class DHCP(MenuItem):
    TEXT = "DHCP"
