class LolAccount:
    
    name = ''
    passWord =''
    lvl = 1
    mainChampion = ''

    def __init__(self, name, passWord, lvl, mainChampion): #contrutor em python
        self.name = name 
        self.passWord = passWord
        self.lvl = lvl
        self.mainChampion = mainChampion
        print ('Object Created!')
    

    def getMainChampion(self):
        return self.mainChampion

if __name__=='__main__':
    acc1 = LolAccount('4bsol','2121',358,'Lee sin')    #Criando objeto
    print('His mainChampion is: ', acc1.getMainChampion())  #Chamando método

