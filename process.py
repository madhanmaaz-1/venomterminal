from filehandler import Filehandler
from utils import Utils
import os
from colorama import Fore
import time

fileHandler = Filehandler()
utils = Utils()


class Process:
    def __init__(self):
        utils.venom()
        utils.configOneTime()
        self.configJson = fileHandler.getJson('bin/config.json')
        self.pkg = fileHandler.getJson('bin/pkg/'+self.configJson['pkg'])
        self.username = self.configJson['username']
        self.pkgArray = os.listdir(fileHandler.getRealPath('bin/pkg'))

    def execute(self, command):
        try:
            os.system(self.pkg[command][0])
        except:
            os.system(command)

    def co(self):
        print("{}{:<20} {:<30} {:<30} {}".format(Fore.GREEN,
              "Commands", "Execute", "Description", utils.resetColor()))

        index = 0
        for i in self.pkg:
            print("{:<20} {:<30} {:<30}".format(
                i, self.pkg[i][0], self.pkg[i][1].capitalize()))
            index += 1

        print(f"\nCurrent pkg    : {Fore.GREEN}{self.configJson['pkg'].upper()}{utils.resetColor()}")
        print(f"Total commands : {Fore.CYAN}{index}{utils.resetColor()}\n")

    def addco(self):
        print(f"\nCurrent pkg : {Fore.GREEN}{self.configJson['pkg'].upper()}{utils.resetColor()}")
        while True:
            try:
                command = [
                    input('Enter command name        : '),
                    input('Enter command             : '),
                    input('Enter command description : ')]
                
                self.pkg[command[0]] = [command[1], command[2]]

                fileHandler.writeJson([self.pkg], 'bin/pkg/'+self.configJson['pkg'])
                utils.vbsComplete(f'{command[0]} command added.')
                print("\nAdd anothor command or Ctrl + c to back")
            except:
                print('\n')
                break


    def rmco(self):
        self.co()

        while True:
            try:
                command = input('Enter command to remove : ')
                del self.pkg[command]
                fileHandler.writeJson([self.pkg], 'bin/pkg/'+self.configJson['pkg'])
                utils.vbsComplete(f"{command} command removed.")
                print('Remove anothor command or Ctrl + c to back')
            except:
                utils.vbsError('Command Error')
                print('\n')
                break

    def showPkg(self):
        print(f"""
{Fore.RED}VENOM PKG MANAGER{utils.resetColor()}
Current pkg : {Fore.GREEN}{self.configJson['pkg'].upper()}{utils.resetColor()}
        """)   
        
        print("{}{:<5} {:<25}{}".format(
            Fore.BLUE ,'PKG NO.', 'PKGS', utils.resetColor()))
        
        pkgIndex = 1
        for i in self.pkgArray:
            print("{:<7} {:<25}".format(pkgIndex, i))
            pkgIndex += 1

        print('\nTotal pkgs: {}{}{}'.format(Fore.CYAN, len(self.pkgArray), utils.resetColor()))
        

    def cngPkg(self):
        self.showPkg()

        while True:
            try:
                pkgNo = input('Enter pkg no : ')
                if int(pkgNo) <= len(self.pkgArray):
                        self.configJson['pkg'] = self.pkgArray[int(pkgNo) - 1]
                        fileHandler.writeJson(
                            [self.configJson], 'bin/config.json')
                        print(f'{Fore.GREEN}package was changed to {Fore.RED}{self.pkgArray[int(pkgNo) - 1]} {utils.resetColor()} restart your terminal')
                        utils.vbsComplete('pkg was changed')
                        print('sleeping in 3 sec.')
                        time.sleep(3)
                        exit()
                else:
                    utils.vbsError('Pkg not found')
                    continue
            except Exception as err:
                utils.vbsError(f"Error {err}")
    
    def edtCo(self):
        print('Opening your editor.')
        os.startfile(fileHandler.getRealPath(f"bin\\pkg\\{self.configJson['pkg']}"))
        time.sleep(3)
        os.system('cls')

    def pkgDir(self):
        print('Opening pkg dir')
        os.startfile(fileHandler.getRealPath(f'bin/pkg'))
    

    def showHelp(self):
        helpFile = fileHandler.getJson('bin/help.json')
        print("Inbuild Commands")
        print("{}{:<15} {:<35}{}".format(Fore.GREEN, "Commands", "Description", utils.resetColor()))
        for i in helpFile:
            print("{:<15} {:<35}".format(i, helpFile[i].capitalize()))
        