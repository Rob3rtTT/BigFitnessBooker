import requests, re

# r = requests.get("https://bigfitness.upfit.live/class-schedule.php?clubid=1001&type=1&template=3&lang=ro&notify=true")

# with open('output.txt', "w") as f:
#     f.write(r.text)

class Booker():
    def __init__(self) -> None:
        self.url = """https://bigfitness.upfit.live/class-schedule.php?clubid=1001&type=1&template=3&lang=ro&notify=true"""
        self.response = requests.get(self.url).text
        # with open('./output.txt', 'r') as f:
        #     self.response = f.read()
        self._classes = {}
        self.get_class_id()
        self.get_class_names()
        self.get_class_dates()
    
    def get_class_id(self):
        pattern = r'id="upfcl-class-name-(\d+)"'
        for match in re.finditer(pattern, self.response):
            match = match.group(1)
            self._classes[match]={}            
        return self._classes
    
    def get_class_names(self):
        for class_id in self._classes.keys():
            _pattern = fr'<div class="upfcl-class-room" id="upfcl-class-room-{class_id}">([^<]+)</div>'
            for line in re.finditer(_pattern, self.response):
                self._classes[class_id]["name"] = line.group(1)
    
    def get_class_dates(self):
        for class_id in self._classes.keys():
            _pattern = r'<div class="upfcl-class-date" id="upfcl-class-date-{0}" style="display:none">(\d+\.\d+\.\d+)</div>'.format(class_id)
            for line in re.finditer(_pattern, self.response):
                self._classes[class_id]["date"] = line.group(1)
         
    @property       
    def classes(self):
        return self._classes
    
    @property
    def class_ids(self):
        class_ids = [_id for _id in self._classes().keys()]
        return class_ids
    
    @property
    def class_names(self):
        class_ids = [self._classes[_id] for _id in self.class_ids()]
        return class_ids
    
    def class_name(self, cid):
        return self.classes[cid]["name"]
        
# b = Booker()
# print(b.classes)
        