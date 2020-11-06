import File as file
from ExcludeDuplicate import ExcludeDuplicate as ed
from StandardizeMinMax import StandardizeMinMax as sMinMax
from StandardizeZScore import StandardizeZScore as sZScore
from ListMissingDataColumn import ListMissingDataColumn as lc
from FillMissingData import FillMissingData as fd
from EraseColumn import EraseColumn as ec
from EraseRow import EraseRow as er
from CountMissingDataRow import CountMissingDataRow as cr
from CalculateAttribute import CalculateAttribute as ca
import argparse

def printError(str):
    print(str + '\n')

def run(args):
    type = args['-type']
    method = args['-method']
    fileIn = args['-filein']
    fileOut = args['-fileout']
    rate = args['-rate']
    attribute = args['-attribute']

    if type == 'fillmissingdata':
        if fileIn is None or method is None or fileOut is None:
            printError('Missing args')
            return

        fill = fd(fileIn)
        fill.fillDataFile(method, fileOut)
    elif type == 'eraserow':
        if fileIn is None or rate is None or fileOut is None:
            printError('Missing args')
            return

        er.eraseRow(fileIn, float(rate), fileOut)
    elif type == 'erasecolumn':
        if fileIn is None or rate is None or fileOut is None:
            printError('Missing args')
            return

        ec.eraseColumn(fileIn, rate, fileOut)
    elif type == 'eraseduplicaterow':
        if fileIn is None or fileOut is None:
            printError('Missing args')
            return

        ed.ExcludeDuplicate(fileIn, fileOut)
    elif type == 'standardize':
        if method is None or fileOut is None or fileIn is None:
            printError('Missing args')
            return

        if method == 'zscore':
            sZScore.StandardizeZScore(fileIn, fileOut)
        elif method == 'minmax':
            sMinMax.StandardizeMinMax(fileIn, fileOut)
        else:
            printError(f'Do not recognize method {method}')
    elif type == 'cau8':
        pass
    else:
        printError(f'Do not recognize type {type}')
        return

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument('-type')
    ap.add_argument('-method')

    ap.add_argument('-rate')

    ap.add_argument('-fileout')
    ap.add_argument('-filein')

    ap.add_argument('-attribute')

    args = argparse.ArgumentParser()

    # print(args)

    run(args)

# import argparse

# ap = argparse.ArgumentParser()

# ap.add_argument("-n", "--name")

# ap.add_argument("-a", "--age")

# ap.add_argument("-s", "--sex")

# args = vars(ap.parse_args())

# # if args["name"] is not None:
# #     print(args["name"])

# # if args["age"] is not None:
# #     print(args["age"])

# # if args["sex"] is not None:
# #     print(args["sex"])

# print(args["name"])
# print(args["age"])
# print(args["sex"])
