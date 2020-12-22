from os import remove

import pandas as pd


def start():
    df = pd.read_excel('Book.xlsx')
    df = df.astype(str)
    df = df.set_index('Тема').T
    df.to_excel('DataSet.xlsx')
    df = pd.read_excel('DataSet.xlsx', index_col=0)
    recList = list()

    print('Введите назание понятия:')
    text = input()

    for row in df:
        k = 0
        corrMat = df.corrwith(df[row])
        corrMat = pd.DataFrame(corrMat)
        tempMat = corrMat
        tempMat = tempMat.drop([row], axis=0)
        while k != 1:
            name = tempMat.idxmax().item()
            value = tempMat[0][tempMat.idxmax().item()]
            recList.append([row, name, value])
            tempMat = tempMat.drop([tempMat.idxmax().item()], axis=0)
            k += 1
    remove('DataSet.xlsx')

    output = list()
    for element in recList:
        if text == element[0]:
            output.append(element)

    print('Возможно вам было бы интересны такие темы как:')
    counter = 0
    for element in output:
        counter += 1
        print('{}) '.format(counter) + element[1])


if __name__ == '__main__':
    start()
