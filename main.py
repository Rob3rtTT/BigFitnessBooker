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
        self.classes = {}
        self.get_class_id(self.response)
        self.get_class_names()
        self.get_class_dates()
            
        
        
    # def parse_response(self, response):
    #     class_ids = self.get_class_id()
    
    def get_class_id(self, response):
        pattern = r'id="upfcl-class-name-(\d+)"'
        for match in re.finditer(pattern, response):
            match = match.group(1)
            self.classes[match]={}            
        return self.classes
    
    def get_class_names(self):
        for class_id in self.classes.keys():
            _pattern = fr'<div class="upfcl-class-room" id="upfcl-class-room-{class_id}">([^<]+)</div>'
            for line in re.finditer(_pattern, self.response):
                self.classes[class_id]["name"] = line.group(1)
    
    def get_class_dates(self):
        for class_id in self.classes.keys():
            _pattern = r'<div class="upfcl-class-date" id="upfcl-class-date-{0}" style="display:none">(\d+\.\d+\.\d+)</div>'.format(class_id)
            for line in re.finditer(_pattern, self.response):
                self.classes[class_id]["date"] = line.group(1)
                
        # print(self.response)
        print(self.classes)
                
Booker()
        
        