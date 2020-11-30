import pandas as pd


def start():
    df = pd.read_excel('Book.xlsx')
    df = df.astype(str)
    df = df.set_index('Тема').T
    df.to_excel('DataSet.xlsx')
    df = pd.read_excel('DataSet.xlsx', index_col=0)
    recList = list()

    print('Введите назание понятия и предложу вам похожие:')
    text = input()
    print('На сколько широкий список интересов вы хотели? Введите число :')
    width = int(input())

    for row in df:
        k = 0
        corrMatr = df.corrwith(df[row])
        corrMatr = pd.DataFrame(corrMatr)
        tempMatr = corrMatr
        tempMatr = tempMatr.drop([row], axis=0)
        while k != width:
            name = tempMatr.idxmax().item()
            value = tempMatr[0][tempMatr.idxmax().item()]
            recList.append([row, name, value])
            tempMatr = tempMatr.drop([tempMatr.idxmax().item()], axis=0)
            k += 1

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
