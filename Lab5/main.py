import pandas as pd


def start():
    recomendations = pd.DataFrame()
    df = pd.read_excel('Book.xlsx')
    df = df.astype(str)
    df = df.set_index('Тема').T
    df.to_excel('DataSet.xlsx')

    recList = []

    print('Введите год принятия закона:')
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
    df.to_excel('result.xlsx')

    df = pd.read_excel('result.xlsx')
    df = df.astype(str)
    df = df.set_index('Тема').T
    df.to_excel('DataSet.xlsx')
    df = pd.read_excel('DataSet.xlsx', index_col=0)


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
    recomendations = recomendations.append(recList, ignore_index=True)
    recomendations.to_excel('resultref.xlsx')

    output = list()
    # for element in recList:
    #     if text == element[0]:
    #         output.append(element)

    print('Возможно вам было бы интересны такие темы как:')
    counter = 0
    for element in output:
        counter += 1
        print('{}) '.format(counter) + element[1])


if __name__ == '__main__':
    start()
