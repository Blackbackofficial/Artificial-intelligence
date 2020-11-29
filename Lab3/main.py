import pandas as pd


recomendations = pd.DataFrame()
df = pd.read_excel('Book.xlsx')
df = df.astype(str)
df = df.set_index('Тема').T
df.to_excel('DataSet.xlsx')
df = pd.read_excel('DataSet.xlsx', index_col=0)
recList = list()

for row in df:
    print(row)
    k = 0  # Количество похожих объектов
    corrMatr = df.corrwith(df[row])
    corrMatr = pd.DataFrame(corrMatr)
    tempMatr = corrMatr
    tempMatr = tempMatr.drop([row], axis=0)
    while k != 3:
        name = tempMatr.idxmax().item()
        value = tempMatr[0][tempMatr.idxmax().item()]
        recList.append([row, name, value])
        tempMatr = tempMatr.drop([tempMatr.idxmax().item()], axis=0)
        k += 1
recomendations = recomendations.append(recList, ignore_index=True)
recomendations.to_excel('result.xlsx')
