class restaurant():
    def __init__(self,idRes,nameRes):
        self.idRes = idRes
        self.nameRes = nameRes


class section():
    def __init__(self,idRes,idSec,nameSec):
        self.idRes = idRes
        self.idSec = idSec
        self.nameSec = nameSec

class element():
    def __init__(self,idElement,idSec,nameEle,priceEle,descEle):
        self.idElement = idElement
        self.idSec = idSec
        self.nameEle = nameEle
        self.priceEle = priceEle
        self.descEle = descEle

