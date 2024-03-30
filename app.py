from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/result',methods = ['POST', 'GET'])
def result():
    output = request.form.to_dict()
    PlainText = output['PlainText']
    key = output['key']
    radio = request.form['radio']
    newKey=""
    newPT=""
    blocks = []
    for char in key:
        if (char not in newKey) and char !='':
            newKey=newKey+char

    alphabet1 = ['x', 'z', 'y', 'w', 'v', 'u', 't', 's',
                'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k',
                'j', 'i','h', 'g', 'f', 'e', 'd', 'c',
                'b', 'a']

    alphabet2 = 'abcdefghiklmnopqrstuvwxyz'  
    i=0
    j=1
    demo=""
    
    while i < len(PlainText):
        while j < len(PlainText):
            if PlainText[i] == PlainText[j]:
                for new in alphabet1:
                    if PlainText[i] != new:
                        newPT = newPT+PlainText[i]+new
                        i+=1
                        j+=1
                        break
            else:
                demo = PlainText[j]
                break
        newPT = newPT+PlainText[i]+demo
        demo = ""
        j+=2
        i+=2
    if len(newPT) % 2 != 0:
        for new in alphabet1:
            if PlainText[-1] != new:
                newPT = newPT+new
                break

    i = 1
    j = 0
    for char1 in newPT[::2]:
        for char2 in newPT[i:i+1]:
            blocks.append([char1, char2,'demo'])    
        i+=2

    newMatrix = [['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', '']]
    m = 0                                  
    for i in range(5):
        for j in range(5):
            for char in newKey[m:]:                                                                 
                if (char == 'i' or char == 'j'):
                    newMatrix[i][j] = 'i'
                    m+=1                          
                    break
                elif char != 'i' and char != 'j':
                    newMatrix[i][j] = char                                                                                            
                    m+=1                          
                    break
    n=0
    for i in range(5):
        for j in range(5):
            if newMatrix[i][j] != '':                          
                continue
            else:
                for char in alphabet2[n:]:   
                    if alphabet2[n:n+1] not in newKey:
                        newMatrix[i][j] = alphabet2[n:n+1]
                        n+=1
                        break
                    else:
                        n+=1
    CypherText = ""
    CypherChar = []
    
    for block in blocks:
        global row1
        global row2
        global col1
        global col2
        for i in range(5):
            for j in range(5):
                if newMatrix[i][j] == block[0]:
                    row1,col1 = i,j
                    break
            else:
                continue
            break

        for a in range(5):
            for b in range(5):
                if newMatrix[a][b] == block[1]:
                    row2,col2 = a,b
                    break
            else:
                continue
            break
            
        if radio ==  'en':  
            if row1 == row2:
                if col1 == 4:
                    CypherText = CypherText+newMatrix[row1][0]
                    c1 = newMatrix[row1][0]
                    CypherText = CypherText+newMatrix[row1][col2+1]
                    c2 = newMatrix[row1][col2+1]

                elif col2 == 4:
                    CypherText = CypherText+newMatrix[row1][col1+1]
                    c1 = newMatrix[row1][col1+1]
                    CypherText = CypherText+newMatrix[row1][0]
                    c2 = newMatrix[row1][0]
                else:
                    CypherText = CypherText+newMatrix[row1][col1+1]
                    c1 = newMatrix[row1][col1+1]
                    CypherText = CypherText+newMatrix[row1][col2+1]
                    c2 = newMatrix[row1][col2+1]
                CypherChar.append([c1, c2,'row'])
            elif col1 == col2:
                if row1 == 4:
                    CypherText = CypherText+newMatrix[0][col1]
                    c1 = newMatrix[0][col1]
                    CypherText = CypherText+newMatrix[row2+1][col2]
                    c2 = newMatrix[row2+1][col2]
                elif row2 == 4:
                        CypherText = CypherText+newMatrix[row1+1][col1]
                        c1 = newMatrix[row1+1][col1]
                        CypherText = CypherText+newMatrix[0][col2]
                        c2 = newMatrix[0][col2]
                else:
                    CypherText = CypherText+newMatrix[row1+1][col1]
                    c1 = newMatrix[row1+1][col1]
                    CypherText = CypherText+newMatrix[row2+1][col2]
                    c2 = newMatrix[row2+1][col2]
                CypherChar.append([c1, c2,'col'])
            else:
                CypherText = CypherText+newMatrix[row1][col2]
                c1 = newMatrix[row1][col2]
                CypherText = CypherText+newMatrix[row2][col1]
                c2 = newMatrix[row2][col1]
                CypherChar.append([c1, c2,'dig'])
        else:
            if row1 == row2:
                if col1 == 0:
                    CypherText = CypherText+newMatrix[row1][4]
                    c1 = newMatrix[row1][4]
                    CypherText = CypherText+newMatrix[row1][col2-1]
                    c2 = newMatrix[row1][col2-1]

                elif col2 == 0:
                    CypherText = CypherText+newMatrix[row1][col1-1]
                    c1 = newMatrix[row1][col1-1]
                    CypherText = CypherText+newMatrix[row1][4]
                    c2 = newMatrix[row1][4]
                else:
                    CypherText = CypherText+newMatrix[row1][col1-1]
                    c1 = newMatrix[row1][col1-1]
                    CypherText = CypherText+newMatrix[row1][col2-1]
                    c2 = newMatrix[row1][col2-1]
                CypherChar.append([c1, c2,'row'])
            elif col1 == col2:
                if row1 == 0:
                    CypherText = CypherText+newMatrix[4][col1]
                    c1 = newMatrix[4][col1]
                    CypherText = CypherText+newMatrix[row2-1][col2]
                    c2 = newMatrix[row2-1][col2]
                elif row2 == 0:
                        CypherText = CypherText+newMatrix[row1-1][col1]
                        c1 = newMatrix[row1-1][col1]
                        CypherText = CypherText+newMatrix[4][col2]
                        c2 = newMatrix[4][col2]
                else:
                    CypherText = CypherText+newMatrix[row1-1][col1]
                    c1 = newMatrix[row1-1][col1]
                    CypherText = CypherText+newMatrix[row2-1][col2]
                    c2 = newMatrix[row2-1][col2]
                CypherChar.append([c1, c2,'col'])
            else:
                CypherText = CypherText+newMatrix[row1][col2]
                c1 = newMatrix[row1][col2]
                CypherText = CypherText+newMatrix[row2][col1]
                c2 = newMatrix[row2][col1]
                CypherChar.append([c1, c2,'dig'])
    c ='col'
    r ='row'
    d = 'dig'
    enn = 'en'
    return render_template("result.html",e=enn,p=newPT.upper() ,rad = radio,k=newKey.upper(),PT=PlainText,mn=newMatrix,charPT=blocks,charCT=CypherChar,zip = zip(blocks,CypherChar),CT=CypherText.upper(),col =c, row =r, dig = d)

if __name__ == "__main__":
    app.run(debug=True,port=5001)