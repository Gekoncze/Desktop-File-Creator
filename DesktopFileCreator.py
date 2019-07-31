#!/usr/bin/python

# https://developer.gnome.org/pygtk/stable/
# https://developer.gnome.org/pygtk/stable/gtk-constants.html
# https://developer.gnome.org/pygtk/stable/gdk-constants.html
# https://docs.huihoo.com/pygtk/2.0-tutorial/ch-ButtonWidget.html
# https://specifications.freedesktop.org/menu-spec/latest/apa.html
# https://specifications.freedesktop.org/menu-spec/latest/apas02.html
# https://specifications.freedesktop.org/menu-spec/latest/apas03.html
# https://developer.gnome.org/integration-guide/stable/desktop-files.html.en
# https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#localized-keys
# https://specifications.freedesktop.org/menu-spec/menu-spec-latest.html#onlyshowin-registry
# https://developer.gnome.org/ModemManager/unstable/ref-dbus-standard-interfaces.html

import DesktopFileCreatorTodo
from DesktopFileCreatorWindow import MainWindow

#import sys
#for path in sys.path:
#     print(path)

mainWindow = MainWindow()
mainWindow.run()
