def get_console_kit_method(method_name):
    # http://stackoverflow.com/questions/23013274/shutting-down-computer-linux-using-python
    import dbus
    sys_bus = dbus.SystemBus()
    console_kit_service = sys_bus.get_object('org.freedesktop.ConsoleKit',
                                             '/org/freedesktop/ConsoleKit/Manager')
    console_kit_interface = dbus.Interface(console_kit_service,
             'org.freedesktop.ConsoleKit.Manager')
    method = console_kit_interface.get_dbus_method(method_name)
    return method
