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

def run(arguments):
    type = arguments['type']
    method = arguments['method']
    fileIn = arguments['filein']
    fileOut = arguments['fileout']
    rate = arguments['rate']
    attribute = arguments['attribute']

    if type == 'listmissingdata':
        if fileIn is None:
            printError('Missing arguments')
            return

        print('Danh sách cột bị thiếu dữ liệu: ', end = '')
        print(lc.listMissingDataColumn(fileIn))
    elif type == 'countmissingdata':
        if fileIn is None:
            printError('Missing arguments')
            return

        print('Số dòng bị thiếu dữ liệu: ', end = '')
        print(cr.countMissingDataRow(fileIn))
    elif type == 'fillmissingdata':
        if fileIn is None or method is None or fileOut is None:
            printError('Missing arguments')
            return

        fill = fd(fileIn)
        fill.fillDataFile(method, fileOut)
    elif type == 'eraserow':
        if fileIn is None or rate is None or fileOut is None:
            printError('Missing arguments')
            return

        er.eraseRow(fileIn, float(rate), fileOut)
    elif type == 'erasecolumn':
        if fileIn is None or rate is None or fileOut is None:
            printError('Missing arguments')
            return

        ec.eraseColumn(fileIn, float(rate), fileOut)
    elif type == 'eraseduplicaterow':
        if fileIn is None or fileOut is None:
            printError('Missing arguments')
            return

        ed.ExcludeDuplicate(fileIn, fileOut)
    elif type == 'standardize':
        if method is None or fileOut is None or fileIn is None or attribute is None:
            printError('Missing arguments')
            return

        if method == 'zscore':
            sZScore.StandardizeZScore(fileIn, fileOut, attribute)
        elif method == 'minmax':
            sMinMax.StandardizeMinMax(fileIn, fileOut, attribute)
        else:
            printError(f'Do not recognize method {method}')
    elif type == 'expression':
        if fileIn is None or fileOut is None:
            return

        ca.CalculateAttribute(fileIn, fileOut)
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

    arguments = vars(ap.parse_args())

    run(arguments)

