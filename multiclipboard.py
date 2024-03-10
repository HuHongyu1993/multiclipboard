from tkinter import *
import json

root = Tk()
root.title('multiclipboard')
root.state('zoomed')

widthList = [16, 32, 64, 120, 4, 32]
heightList = [2, 4, 8, 16, 32, 16]
cols = len(widthList)
rows = len(heightList)
idText = [[0 for c in range(cols)] for r in range(rows)]

for r in range(rows):
    for c in range(cols):
        idText[r][c] = Text(root, name=f'text_{r}_{c}', width=widthList[c], height=heightList[r],
                            undo=True, wrap=WORD)
        idText[r][c].grid(row=r, column=c)

text_09AF = idText[3][4]
text_09AF.insert(INSERT, '\n'.join(list('%X' % i for i in range(16))))

text_0099 = idText[4][4]
text_0099.insert(INSERT, '\n'.join(list('%02d' % i for i in range(100))))

try:
    fin = open('load.json', 'r')
    data = json.loads(fin.read())
    fin.close()
except:
    data = {}
for i in data:
    idText[int(i[0])][int(i[1])].insert(INSERT, data[i])

root.mainloop()
