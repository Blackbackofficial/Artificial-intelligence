from os import remove
import pandas as pd
import xlrd
import xlwt


def start():
    recList = []

    print('Введите век принятия закона:')
    Year = int(input())
    print('Введите колличество аргуменов:')
    Arg = int(input())
    print('Введите степень точности, те 10^(-9) => 9:')
    Accuracy = int(input())
    print('Введите уровень на дереве:')
    Level = input()
    print('Популярный? Введите да/нет:')
    popular = input()
    print('Введите назание закона:')
    Law = input()
    Law = str_to_int(Law)
    result = []
    inter = [result]

    result.append(Year)
    result.append(Arg)
    result.append(Accuracy)
    result.append(Level)
    result.append(popular)
    if result[4] == 'да':
        result[4] = 1
    elif result[4] == 'нет':
        result[4] = 0
    else:
        result[4] = 0
    result.append(Law)

    df = pd.read_excel('Book.xlsx', index_col=0)
    col = pd.DataFrame(inter, index=['Yours'],
                       columns=['Век', 'Аргументы', 'Точность', 'Уровень', 'Популярность', 'Закон'])
    df = df.append(col)
    df.to_excel('result.xls')

    rb = xlrd.open_workbook('result.xls')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    vals[0][0] = 'Тема'

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')

    for el in range(6):
        i = 0
        for rec in vals:
            ws.write(i, el, rec[el])
            i += 1
    wb.save('result.xls')

    df = pd.read_excel('result.xls')
    df = df.astype(str)
    df = df.set_index('Тема').T
    df.to_excel('result.xls')
    df = pd.read_excel('result.xls', index_col=0)

    for row in df:
        k = 0
        corrMat = df.corrwith(df[row])
        corrMat = pd.DataFrame(corrMat)
        tempMat = corrMat
        tempMat = tempMat.drop([row], axis=0)
        while k != 2:
            name = tempMat.idxmax().item()
            value = tempMat[0][tempMat.idxmax().item()]
            recList.append([row, name, value])
            tempMat = tempMat.drop([tempMat.idxmax().item()], axis=0)
            k += 1
    remove('result.xls')

    text = 'Yours'
    output = list()
    for element in recList:
        if text == element[0]:
            output.append(element)

    print('Мы нашли похожие по вашему запросу:')
    counter = 0
    for element in output:
        counter += 1
        print('{}) '.format(counter) + element[1])


def str_to_int(Law):
    if Law.__contains__('Закон'):
        Law = 3
    if Law.__contains__('Понятие'):
        Law = 1
    if Law.__contains__('теория'):
        Law = 2
    if Law.__contains__('Гипотиза'):
        Law = 4
    if Law.__contains__('излучение'):
        Law = 5
    else:
        Law = 0
    return Law


if __name__ == '__main__':
    start()
