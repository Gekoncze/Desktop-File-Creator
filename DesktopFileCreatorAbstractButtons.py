import pygtk
pygtk.require('2.0')
import gtk

class ValueMenu(gtk.Menu):
    def __init__(self, entry, add, values):
        super(ValueMenu, self).__init__()
        for value in values:
            if type(value) == list:
                menuItem = ValueMenuItem(entry, add, value[0], value[1])
                self.append(menuItem)
                menuItem.show()
            else:
                menuItem = ValueMenuItem(entry, add, value, None)
                self.append(menuItem)
                menuItem.show()
    
class ValueMenuItem(gtk.MenuItem):
    def __init__(self, entry, add, value, values):
        super(ValueMenuItem, self).__init__()
        self.entry = entry
        self.add = add
        self.set_label(value)
        self.connect("activate", self.onActivate)
        if values is not None:
            menu = ValueMenu(entry, add, values)
            self.set_submenu(menu)
        
    def onActivate(self, e):
        if self.add:
            if not self.contains(self.get_label()):
                self.entry.set_text(self.entry.get_text() + self.get_label() + ";")
        else:
            self.entry.set_text(self.get_label())
    
    def contains(self, value):
        tokens = list(filter(None, self.entry.get_text().split(";")))
        for token in tokens:
            if token == value:
                return True
        return False
    
class SetValuesButton(gtk.Button):
    def __init__(self, entry, values):
        super(SetValuesButton, self).__init__()
        self.menu = ValueMenu(entry, False, values)
        self.set_label("<")
        self.connect("button_press_event", self.onActivate)
        
    def onActivate(self, button, e):
        self.menu.popup(None, None, None, e.button, e.time)
    
class AddValuesButton(gtk.Button):
    def __init__(self, entry, values):
        super(AddValuesButton, self).__init__()
        self.menu = ValueMenu(entry, True, values)
        self.set_label("+")
        self.connect("button_press_event", self.onActivate)
        
    def onActivate(self, button, e):
        self.menu.popup(None, None, None, e.button, e.time)

class ValueMenu(gtk.Menu):
    def __init__(self, entry, add, values):
        super(ValueMenu, self).__init__()
        for value in values:
            if type(value) == list:
                menuItem = ValueMenuItem(entry, add, value[0], value[1])
                self.append(menuItem)
                menuItem.show()
            else:
                menuItem = ValueMenuItem(entry, add, value, None)
                self.append(menuItem)
                menuItem.show()
    
class ValueMenuItem(gtk.MenuItem):
    entry = None
    add = None
    
    def __init__(self, entry, add, value, values):
        super(ValueMenuItem, self).__init__()
        self.entry = entry
        self.add = add
        self.set_label(value)
        self.connect("button_press_event", self.onActivate)
        if values is not None:
            menu = ValueMenu(entry, add, values)
            self.set_submenu(menu)
        
    def onActivate(self, widget, e):
        if self.add:
            if not self.contains(self.get_label()):
                self.entry.set_text(self.entry.get_text() + self.get_label() + ";")
        else:
            self.entry.set_text(self.get_label())
    
    def contains(self, value):
        tokens = list(filter(None, self.entry.get_text().split(";")))
        for token in tokens:
            if token == value:
                return True
        return False
    
class SetFilePathButton(gtk.Button):
    entry = None
    
    def __init__(self, entry):
        super(SetFilePathButton, self).__init__()
        self.entry = entry
        self.set_label("...")
        self.connect("button_press_event", self.onActivate)
        
    def onActivate(self, button, e):
        dialog = gtk.FileChooserDialog (title = "Choose File", parent = self.get_toplevel(), action = gtk.FILE_CHOOSER_ACTION_OPEN, buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK), backend = None)
        result = dialog.run()
        if result == gtk.RESPONSE_OK:
            if dialog.get_filename() is not None:
                if len(dialog.get_filename()) > 0:
                    self.entry.set_text(self.addLauncher(dialog.get_filename()))
        dialog.destroy()
        
    def addLauncher(self, path):
        if path.endswith(".sh"): return "sh " + path
        if path.endswith(".py"): return "python " + path
        if path.endswith(".jar"): return "java -jar " + path
        return path
        
class SetDirectoryPathButton(gtk.Button):
    entry = None
    
    def __init__(self, entry):
        super(SetDirectoryPathButton, self).__init__()
        self.entry = entry
        self.set_label("...")
        self.connect("button_press_event", self.onActivate)
        
    def onActivate(self, button, e):
        dialog = gtk.FileChooserDialog (title = "Choose Directory", parent = self.get_toplevel(), action = gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK), backend = None)
        result = dialog.run()
        if result == gtk.RESPONSE_OK:
            if dialog.get_filename() is not None:
                if len(dialog.get_filename()) > 0:
                    self.entry.set_text(dialog.get_filename())
        dialog.destroy()
    
class SetValuesButton(gtk.Button):
    menu = None
    
    def __init__(self, entry, values):
        super(SetValuesButton, self).__init__()
        self.menu = ValueMenu(entry, False, values)
        self.set_label("<")
        self.connect("button_press_event", self.onActivate)
        
    def onActivate(self, button, e):
        self.menu.popup(None, None, None, e.button, e.time)
    
class AddValuesButton(gtk.Button):
    menu = None
    
    def __init__(self, entry, values):
        super(AddValuesButton, self).__init__()
        self.menu = ValueMenu(entry, True, values)
        self.set_label("+")
        self.connect("button_press_event", self.onActivate)
        
    def onActivate(self, button, e):
        self.menu.popup(None, None, None, e.button, e.time)
