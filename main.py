import os, glob, sys

if __name__ == "__main__":
    count = 0
    # This loop walk through the folder and pick all the folder that ends by ".ui"
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.ui'):
                # Here is the compilation step
                partitionName = file.partition('.')
                fileName = partitionName[0]
                newFileName = "Ui_" + fileName + ".py"
                command = "pyuic6 " + file + " -o " + newFileName
                returnedValue = os.system(command)
                # Error management
                if returnedValue == 1:
                    sys.exit("An error has been raised")
                else:
                    count += 1
    print(str(count) + " files have been compile")
