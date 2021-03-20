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

class invoice():
    def __init__(self,idInv,nameCli,nitCli,addressCli,tip):
        self.idInv = idInv
        self.nameCli = nameCli
        self.nitCli = nitCli
        self.addressCli = addressCli 
        self.tip = tip

class detail():
    def __init__(self,idDet,idInv,cant,idElement):
        self.idDet = idDet
        self.idInv = idInv
        self.cant = cant
        self.idElement = idElement
