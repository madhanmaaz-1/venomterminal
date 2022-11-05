from process import Process
from filehandler import Filehandler
from utils import Utils
from colorama import Fore

process = Process()
fileHandler = Filehandler()
utils = Utils()

while True:
    utils.resetColor()
    try:
        
        userInput = input("{}(VENOM@{})>{} ".format(Fore.GREEN ,process.username.capitalize(), utils.resetColor()))

        if userInput == 'exit':
            break
        elif userInput == '':
            continue
        elif userInput == 'venom':
            utils.venom()
        elif userInput == 'co':
            process.co()
        elif userInput == 'addco':
            process.addco()
        elif userInput == 'rmco':
            process.rmco()
        elif userInput == 'pkg':
            process.showPkg()
        elif userInput == 'cngpkg':
            process.cngPkg()
        elif userInput == 'edtco':
            process.edtCo()
        elif userInput == 'pkgdir':
            process.pkgDir()
        elif userInput == 'help':
            process.showHelp()
        else:
            process.execute(userInput)

    except:
        break