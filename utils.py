from filehandler import Filehandler
from colorama import Fore, Style
import os

fileHandler = Filehandler()

class Utils:
    def __init__(self):
        pass
    
    def resetColor(self):
        return Style.RESET_ALL

    def configOneTime(self):
        
        if os.path.exists(fileHandler.getRealPath('bin/config.json')) == False:
            env = f"""
@echo off
cd {fileHandler.getRealPath('bin')}/../
venom"""

            with open(fileHandler.getRealPath('bin/venom.bat'), 'w') as envFile:
                envFile.write(env)
            
            os.startfile(fileHandler.getRealPath('venom.html'))
            username = input('Enter your name : ')
            data = [{"username": username, "pkg": "inbuild.json"}]
            fileHandler.writeJson(data, 'bin/config.json')
    

    def vbsError(self, data):
        errTxt = f"""x = MsgBox("{data}", 16+0, "Error")"""
        fileHandler.vbsWrite(errTxt, 'bin/vbs/error.vbs')
        os.startfile(fileHandler.getRealPath('bin/vbs/error.vbs'))

    def vbsComplete(self, data):
        comTxt = f"""x = MsgBox("{data}", 64+0, "Complete")"""
        fileHandler.vbsWrite(comTxt, 'bin/vbs/complete.vbs')
        os.startfile(fileHandler.getRealPath('bin/vbs/complete.vbs'))

    def venom(self):
        os.system('ping google.com')
        a = f"""{Fore.CYAN}
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                                            {Fore.RED}Designed By Madhan v1.{self.resetColor()}"""
        print(a)