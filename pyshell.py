import os
import webbrowser
import urllib.request

workingDir = os.getcwd()

def parse(x):
    
    global workingDir
    args = x.split(" ")
    command = args[0]
    command = command.lower()

    if (len(command) < 1):
        return

    if (command == "help"):
        print('')
        print("help: shows all available commands")
        print("echo (string): prints a string")
        print("cd (directory): changes the working directory")
        print("wd: prints the working directory")
        print("touch (filename): creates a file in the current working directory")
        print("mkdir (directory name): creates a direcectory in the current working directory")
        print("download (url, filepath): downloads a file from the internet")
        print("ls: shows all subfiles and subfolders in the current working directory")
        print("read (filepath): reads all lines in a file")
        print("comm (filepath1, filepath2): compares two files")
        print("exit: closes pyshell")
        print('')
        return
    
    if (command == "echo"):
        try:
            print(args[1])
            return
        except:
            print("usage: echo (string)")
            return

    if (command == "cd"):
        try:
            workingDir = args[1]
            workingDir = workingDir.replace("\\", "/")
            return
        except:
            print("usage: cd (directory)")

    if (command == "wd"):
        print(workingDir)
        return

    if (command == "touch"):
        try:
            finalDir = os.path.join(workingDir, args[1])
            file = open(finalDir, "x")
            file.close()
            return
        except:
            print("usage: touch (filename)")
            return

    if (command == "mkdir"):
        try:
            finalDir = os.path.join(workingDir, args[1])
            os.mkdir(finalDir)
            return
        except:
            print("usage: touchdir (directory name)")
            return

    if (command == "download"):
        try:
            url = args[1]
            filepath = args[2]
            filename, headers = urllib.request.urlretrieve(url, filename = filepath)
            return
        except:
            print("usage: download (url, path)")
            return

    if (command == "ls"):
        try:
            fList = os.listdir(workingDir)
            i = 0
            while (i < len(fList)):
                print(fList[i])
                i += 1
            return
        except:
            return

    if (command == "read"):
        try:
            filepath = os.path.join(workingDir, args[1])
            f = open(filepath, "r")
            print(f.read())
            return
        except:
            print("usage: read (filepath)")
            return

    if (command == "comm"):
        try:
            filepath1 = os.path.join(workingDir, args[1])
            filepath2 = os.path.join(workingDir, args[2])
            f1 = open(filepath1, "r")
            f2 = open(filepath2, "r")
            rawcontents1 = f1.read()
            rawcontents2 = f2.read()
            contents1 = []
            contents2 = []

            a = 0
            while (a < len(rawcontents1)):
                teststr = rawcontents1[a].strip()
                if (teststr != ""):
                    contents1.append(rawcontents1[a])
                a += 1
            
            b = 0
            while (b < len(rawcontents2)):
                teststr = rawcontents2[b].strip()
                if (teststr != ""):
                    contents2.append(rawcontents2[b])
                b += 1

            max = 0
            if (len(contents1) > len(contents2)):
                max = len(contents2)
            else:
                max = len(contents1)
            i = 0
            while (i < max):
                if (contents1[i] != contents2[i]):
                    j = i + 1
                    print("line: ", j, ", " + contents1[i], " != ", contents2[i])
                i+=1
            return
        except:
            print("usage: comm (filepath1, filepath2)")
            return
    
    if (command == "exit"):
        exit()

    else:
        print("unknown command: " + command)
        return

def commandLoop():
    command = input(workingDir + ">")
    parse(command)
    commandLoop()

def init():
    print("                  _          _ _ ")
    print("                 | |        | | |")
    print("  _ __  _   _ ___| |__   ___| | |")
    print(" | '_ \| | | / __| '_ \ / _ \ | |")
    print(" | |_) | |_| \__ \ | | |  __/ | |")
    print(" | .__/ \__, |___/_| |_|\___|_|_|")
    print(" | |     __/ |                   ")
    print(" |_|    |___/                    \n")
    print("'help' for help\n")

init()
commandLoop()
