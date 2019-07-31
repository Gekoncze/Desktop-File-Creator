from DesktopFileCreatorStorage import Storage

def replaceFirst(s, old, new):
    i = s.find(old)
    if(i == -1): return
    return s[0:i] + new + s[i+len(old):]

class Options(Storage):
    def __init__(self):
        super(Options, self).__init__(3)
        
    def createDefaultValue(self):
        return ""

    def toString(self):
        content = ""
        for key in self.keys():
            if key == "":
                line = "[Desktop Entry]"
            else:
                line = "[Desktop Action " + key + "]"
                
            content = content + line + "\n"
            group = self[key]
            
            for key in group.keys():
                if key == "":
                    brackets = ""
                else:
                    brackets = "[" + key + "]"
                    
                options = group[key]
                
                for key in options.keys():
                    value = options[key]
                    content = content + key + brackets + "=" + value + "\n"
                    
            content = content + "\n"
        return content
        
    def fromString(self, content):
        self.clear()
        lines = content.split("\n")
        group = None
        i = 0
        try:
            for line in lines:
                i += 1
                line = line.strip()
                if len(line) == 0: continue  # skip empty lines
                if line.startswith("#"): continue  # skip comments
                
                if line == "[Desktop Entry]":
                    group = self[""]
                elif line.startswith("[Desktop Action ") and line.endswith("]"):
                    key = line[len("[Desktop Action "):-len("]")]
                    group = self[key]
                elif "[" in line and "]" in line and "=" in line:
                    if group == None: raise Exception("Missing '[Desktop Entry]'.")
                    line = replaceFirst(replaceFirst(line, "[", "="), "]", "=")
                    tokens = list(filter(None, line.split("=")))
                    if len(tokens) != 3: raise Exception("Unsupported line format.")
                    key = tokens[0]
                    locale = tokens[1]
                    value = tokens[2]
                    group[locale][key] = value
                elif "=" in line:
                    if group == None: raise Exception("Missing '[Desktop Entry]'.")
                    tokens = list(filter(None, line.split("=")))
                    if len(tokens) != 2: raise Exception("Unsupported line format.")
                    key = tokens[0]
                    value = tokens[1]
                    group[""][key] = value
                else:
                    raise Exception("Unsupported line format.")
        except Exception as e:
            self.clear()
            raise Exception("Error at line " + str(i) + ": " + e.message)
                
class State(object):
    def __init__(self):
        self.actions = []
        self.locales = []
        self.options = Options()
