import pygtk
pygtk.require('2.0')
import gtk

from DesktopFileCreatorAbstractButtons import SetDirectoryPathButton
from DesktopFileCreatorAbstractButtons import SetFilePathButton
from DesktopFileCreatorAbstractButtons import SetValuesButton
from DesktopFileCreatorAbstractButtons import AddValuesButton

class FilePathButton(SetFilePathButton):
    def __init__(self, entry):
        super(FilePathButton, self).__init__(entry)
        
class DirectoryPathButton(SetDirectoryPathButton):
    def __init__(self, entry):
        super(DirectoryPathButton, self).__init__(entry)

class CategoriesButton(AddValuesButton):
    values = [
        ["AudioVideo", ["Audio", "Video", "Midi", "Mixer", "Sequencer", "Tuner", "TV", "AudioVideoEditing", "Player", "Recorder", "Music"]],
        ["Development", ["Building", "Debugger", "IDE", "GUIDesigner", "Profiling", "RevisionControl", "Translation", "Database", "WebDevelopment"]],
        ["Education", ["Art", "Languages", "History", "Humanities", "Literature", "Math", "NumericalAnalysis", "Spirituality", "Sports", "ParallelComputing"]],
        ["Game", ["ActionGame", "AdventureGame", "ArcadeGame", "BoardGame", "BlocksGame", "CardGame", "KidsGame", "LogicGame", "RolePlaying", "Shooter", "Simulation", "SportsGame", "StrategyGame", "Art", "Emulator"]],
        ["Graphics", ["2DGraphics", "VectorGraphics", "RasterGraphics", "3DGraphics", "OCR", "Photography", "Viewer", "ImageProcessing"]],
        ["Network", ["Email", "Dialup", "InstantMessaging", "Chat", "IRCClient", "Feed", "FileTransfer", "HamRadio", "News", "P2P", "RemoteAccess", "Telephony", "VideoConference", "WebBrowser"]],
        ["Office", ["Calendar", "ContactManagement", "Dictionary", "Chart", "Email", "Finance", "FlowChart", "PDA", "ProjectManagement", "Presentation", "Spreadsheet", "WordProcessor", "Scanning", "Photography", "Publishing", "DataVisualization"]],
        ["Science", ["Art", "Construction", "ArtificialIntelligence", "Astronomy", "Biology", "Chemistry", "ComputerScience", "DataVisualization", "Economy", "Electricity", "Geography", "Geology", "Geoscience", "Math", "MedicalSoftware", "Physics", "Robotics", "Electronics", "Engineering"]],
        ["Settings", ["DesktopSettings", "HardwareSettings"]],
        ["System", ["PackageManager", "Emulator", "FileTools", "Printing", "FileManager", "TerminalEmulator", "Filesystem", "Monitor", "Security", "Core"]],
        ["Utility", ["TextTools", "TelephonyTools", "DiscBurning", "Maps", "Archiving", "Compression", "FileTools", "Accessibility", "Calculator", "Clock", "TextEditor", "Documentation"]]
    ]
    
    def __init__(self, entry):
        super(CategoriesButton, self).__init__(entry, self.values)

class TypesButton(SetValuesButton):
    values = ["Application", "Link", "Directory"]
    
    def __init__(self, entry):
        super(TypesButton, self).__init__(entry, self.values)

class BooleanButton(SetValuesButton):
    values = ["false", "true"]
    
    def __init__(self, entry):
        super(BooleanButton, self).__init__(entry, self.values)

class DesktopEnvironmentButton(AddValuesButton):
    values = ["GNOME", "KDE", "LXDE", "LXQt", "MATE", "Razor", "ROX", "TDE", "Unity", "XFCE", "EDE", "Cinnamon", "Pantheon", "Old"]
    
    def __init__(self, entry):
        super(DesktopEnvironmentButton, self).__init__(entry, self.values)
    
class InterfaceButton(AddValuesButton):
    values = ["org.freedesktop.DBus.Properties", "org.freedesktop.DBus.Introspectable", "org.freedesktop.DBus.ObjectManager"]
    
    def __init__(self, entry):
        super(InterfaceButton, self).__init__(entry, self.values)
