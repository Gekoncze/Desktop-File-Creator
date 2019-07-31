from DesktopFileCreatorButtons import *

class OptionHelper:
    def __init__(self, category, localizable, actionable, buttonFactory, order):
        self.category = category
        self.localizable = localizable
        self.actionable = actionable
        self.buttonFactory = buttonFactory
        self.order = order

class Info:
    name = "Desktop File Creator"
    version = "0.1.0"

class Categories:
    main = "Main"
    app = "Application"
    link = "Link"
    menu = "Menu"
    other = "Other"
    
    categories = [main, app, link, menu, other]

class Config:
    defaultHelper = OptionHelper(Categories.other, False, False, None, 1000)
    
    helpers = dict()
    
    helpers["Name"] = OptionHelper(Categories.main, True, True, None, 1)
    helpers["GenericName"] = OptionHelper(Categories.main, True, False, None, 2)
    helpers["Comment"] = OptionHelper(Categories.main, True, False, None, 3)
    helpers["Icon"] = OptionHelper(Categories.main, False, True, FilePathButton, 4)
    helpers["Type"] = OptionHelper(Categories.main, False, False, TypesButton, 5)
    
    helpers["Exec"] = OptionHelper(Categories.app, False, True, FilePathButton, 1)
    helpers["TryExec"] = OptionHelper(Categories.app, False, False, FilePathButton, 2)
    helpers["Path"] = OptionHelper(Categories.app, False, False, DirectoryPathButton, 3)
    helpers["Terminal"] = OptionHelper(Categories.app, False, False, BooleanButton, 4)
    helpers["StartupNotify"] = OptionHelper(Categories.app, False, False, BooleanButton, 5)
    helpers["StartupWMClass"] = OptionHelper(Categories.app, False, False, None, 6)
    helpers["DBusActivatable"] = OptionHelper(Categories.app, False, False, BooleanButton, 7)
    helpers["Actions"] = OptionHelper(Categories.app, False, False, None, 8)
    
    helpers["URL"] = OptionHelper(Categories.link, False, False, None, 1)

    helpers["Categories"] = OptionHelper(Categories.menu, False, False, CategoriesButton, 1)
    helpers["Keywords"] = OptionHelper(Categories.menu, True, False, None, 2)
    helpers["NoDisplay"] = OptionHelper(Categories.menu, False, False, BooleanButton, 3)
    
    helpers["MimeType"] = OptionHelper(Categories.other, False, False, None, 1)
    helpers["OnlyShowIn"] = OptionHelper(Categories.other, False, False, DesktopEnvironmentButton, 2)
    helpers["NotShowIn"] = OptionHelper(Categories.other, False, False, DesktopEnvironmentButton, 3)
    helpers["Implements"] = OptionHelper(Categories.other, False, False, None, 4)
    helpers["Hidden"] = OptionHelper(Categories.other, False, False, BooleanButton, 5)
    
