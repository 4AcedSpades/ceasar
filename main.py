import util

filePath = ''

if __name__ == "__main__":
    while True:
        util.mainMenuPrintout()
        choice = util.MainMenu()
        if choice == 1:                       
            filePath = util.createFile(filePath)               
            alphabet = util.getAlpha(filePath)                 
            shift = util.getShift(filePath)                    
            message = util.createMsg(filePath, alphabet, shift)
            util.returntomenu()   

        elif choice == 2:                     
            filePath, reply, alphabet, shift = util.readMsg(filePath)                                                         
            util.replyMsg(filePath=filePath, reply=reply, alphabet=alphabet, shift=shift)
            util.returntomenu()    
        elif choice == 3:                     
            exit()                                 
        else:                                      
            print("Please provide a valid choice.")