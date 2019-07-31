import pygtk
pygtk.require('2.0')
import gtk
import pango

print("Using pygtk " + str(gtk.pygtk_version))
print("Using gtk " + str(gtk.gtk_version))

from DesktopFileCreatorConfig import Info
from DesktopFileCreatorConfig import Config
from DesktopFileCreatorConfig import Categories
from DesktopFileCreatorState import State

class OptionWidget:
    def __init__(self, key, helper):
        self.key = key
        self.helper = helper
        
        self.label = gtk.Label()
        self.label.set_text(key)
        
        self.entry = gtk.Entry()
        self.entry.set_text("")
        
        self.button = None
        if(helper.buttonFactory is not None): self.button = helper.buttonFactory(self.entry)

def optionsToHelpers(options):
    for actionKey in options.keys():
        action = options[actionKey]
        for localeKey in action.keys():
            locale = group[localeKey]
            for optionKey in locale.keys():
                if not optionKey in Config.helpers:
                    Config.helpers[optionKey] = Config.defaultHelper
    return Config.helpers
                    
def helpersToWidgets(helpers):
    optionWidgets = dict()
    for key in helpers.keys():
        optionWidgets[key] = OptionWidget(key, helpers[key])
    return optionWidgets
        
def filterWidgets(widgets):
    filteredWidgets = dict()
    for category in Categories.categories:
        filteredWidgets[category] = list()
    
    for key in widgets.keys():
        widget = widgets[key]
        filteredWidgets[widget.helper.category].append(widget)
        
    return filteredWidgets
        
def optionsToWidgets(options, widgets):
    for key in options.keys():
        widgets[key].entry.set_text(options[key])
    
def widgetsToOptions(widgets, options):
    for key in widgets:
        content = widgets[key].entry.get_text().strip()
        if len(content) > 0:
            options[key] = content
        else:
            options[key] = None
                
class OptionsGrid(gtk.VBox):
    def __init__(self, filteredWidgets):
        super(OptionsGrid, self).__init__()
        
        self.set_spacing(4)
        self.set_homogeneous(False)
        
        for widget in filteredWidgets:
            hbox = gtk.HBox()
            hbox.set_spacing(4)
            hbox.set_homogeneous(False)
            hbox.pack_start(widget.label, False, False)
            hbox.pack_start(widget.entry, True, True)
            if widget.button is not None: hbox.pack_start(widget.button, False, False)
            self.pack_start(hbox, False, False)
            
class OptionsFilter(gtk.ScrolledWindow):
    def __init__(self, filteredWidgets):
        super(OptionsFilter, self).__init__()
        self.grid = OptionsGrid(filteredWidgets)
        self.set_policy(gtk.POLICY_ALWAYS, gtk.POLICY_ALWAYS)
        self.set_size_request(512, 256)
        self.add_with_viewport(self.grid)
            
class OptionsContainer(gtk.Notebook):
    def __init__(self, options):
        super(OptionsContainer, self).__init__()
        self.widgets = helpersToWidgets(optionsToHelpers(options))
        filteredWidgets = filterWidgets(self.widgets)
        for category in Categories.categories:
            self.append_page(OptionsFilter(filteredWidgets[category]), gtk.Label(category))
            
class GroupComboBox(gtk.HBox):
    def __init__(self, groups):
        super(GroupComboBox, self).__init__()
        self.comboBox = gtk.combo_box_new_text()
        for groupKey in groups.keys():
            self.comboBox.append_text(groupKey)
        self.comboBox.set_active(0)
    
    def getSelectedGroupKey(self):
        return self.comboBox.get_active_text()
    
class ActionComboBox(gtk.HBox):
    def __init__(self, actions):
        super(ActionComboBox, self).__init__()
        self.actions = actions
        self.set_spacing(4)
        self.label = gtk.Label("Action")
        self.comboBox = gtk.combo_box_new_text()
        self.comboBox.append_text("[Desktop Entry]")
        self.comboBox.set_active(0)
        for action in actions:
            self.comboBox.append_text("[Desktop Action " + action + "]")
        self.pack_start(self.label, False, False)
        self.pack_start(self.comboBox, True, True)
            
    def getSelectedAction(self):
        index = self.comboBox.get_active()
        if index <= 0: return ""
        return self.actions[index - 1]
            
class LocaleComboBox(gtk.HBox):
    def __init__(self, locales):
        super(LocaleComboBox, self).__init__()
        self.locales = locales
        self.set_spacing(4)
        self.label = gtk.Label("Locale")
        self.comboBox = gtk.combo_box_new_text()
        self.comboBox.append_text("<default>")
        self.comboBox.set_active(0)
        for locale in locales:
            self.comboBox.append_text(locale)
        self.pack_start(self.label, False, False)
        self.pack_start(self.comboBox, True, True)
            
    def getSelectedLocale(self):
        index = self.comboBox.get_active()
        if index <= 0: return ""
        return self.locales[index - 1]
    
class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.data = State()
        
        self.connect("destroy", gtk.main_quit)
        self.set_title(Info.name + " " + Info.version)
        self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DIALOG)
        self.set_border_width(8)
        
        self.actionComboBox = ActionComboBox(self.data.actions)
        self.localeComboBox = LocaleComboBox(self.data.locales)
        self.optionsContainer = OptionsContainer(self.data.options)

        self.loadButton = gtk.Button()
        self.loadButton.set_label("Load Desktop File")
        self.loadButton.connect('button_press_event', self.load)

        self.saveButton = gtk.Button()
        self.saveButton.set_label("Save Desktop File")
        self.saveButton.connect('button_press_event', self.save)

        hbox = gtk.HBox()
        hbox.pack_start(self.loadButton, False, False)
        hbox.pack_end(self.saveButton, False, False)

        vbox = gtk.VBox()
        vbox.set_spacing(8)
        vbox.pack_start(self.actionComboBox, False, False)
        vbox.pack_start(self.localeComboBox, False, False)
        vbox.pack_start(self.optionsContainer, True, True)
        vbox.pack_start(hbox, False, False)
        
        self.add(vbox)
        
    def run(self):
        self.show_all()
        gtk.main()
    
    def load(self, widget, e):
        dialog = gtk.FileChooserDialog (title = "Open File", parent = self.get_toplevel(), action = gtk.FILE_CHOOSER_ACTION_OPEN, buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK), backend = None)
        result = dialog.run()
        filename = dialog.get_filename()
        dialog.destroy()
        if result == gtk.RESPONSE_OK:
            if filename is not None:
                if len(filename) > 0:
                    self.doLoad(filename)
        
    def doLoad(self, filename):
        try:
            file = open(filename, "r")
            content = file.read()
            file.close()
            self.data.options.fromString(content)
            optionsToWidgets(self.data.options[""][""], self.optionsContainer.widgets)
        except Exception as e:
            self.showErrorMessage(str(e))
        
    def save(self, widget, e):
        dialog = gtk.FileChooserDialog (title = "Save File", parent = self.get_toplevel(), action = gtk.FILE_CHOOSER_ACTION_SAVE, buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK), backend = None)
        result = dialog.run()
        filename = dialog.get_filename()
        dialog.destroy()
        if result == gtk.RESPONSE_OK:
            if filename is not None:
                if len(filename) > 0:
                    self.doSave(filename)
        
    def doSave(self, filename):
        try:
            widgetsToOptions(self.optionsContainer.widgets, self.data.options[""][""])
            content = self.data.options.toString()
            file = open(filename, "w")
            file.write(content)
            file.close()
        except Exception as e:
            self.showErrorMessage(str(e))
        
    def showErrorMessage(self, message):
        dialog = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, message)
        dialog.run()
        dialog.destroy()
