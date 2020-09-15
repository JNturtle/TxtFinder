import re

class TXTFINDER():
    def __init__(self, path):
        self.content = ""
        self.path = path
        self.rows = []
        self.reload(path)
        if 0 :
            try:
                with open(path, "r") as f:
                    self.content = f.read()
                f.close()
                self.rows = self.content.split("\n")
            except:
                print("『錯誤』：無法讀取" + path +"的內容！")

    def prefixExclude(self, pattern, txtLen = 0):
        p = re.compile(pattern)
        for row in self.rows:
            pos = re.search(p, row)
            if pos:
                #print(row[pos.start() + txtLen:])
                return row[pos.start() + txtLen:]
        return ""
         
    def reload(self, path = ""):
        if path: self.path = path
        try:
            with open(path, "r") as f:
                self.content = f.read()
            f.close()
            self.rows = self.content.split("\n")
        except:
            print("『錯誤』：無法讀取" + path +"的內容！")
        return None

    pass
