import configparser
import winreg
import subprocess
import os.path

import test_lib

if __name__ == "__main__":

    destDir =os.path.abspath(os.path.join(test_lib.GetCurrentProjectRootDir(), "Saved\\ProjectUtils\\SplitedPaksTemp\\"))
    for root, dirs, files in os.walk(destDir):
        for filename in files:
            filepath = os.path.join(root, filename)
            print(filepath)
            test_lib.ListFilesInPak(filepath)
            print('\n')