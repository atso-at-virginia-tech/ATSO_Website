output = ''
parseType = input("y: clipboard, n: html, blank: clipboard: ")
print("\n")

if(parseType == '' or parseType == 'y'):
    parseType = True
else:
    parseType = False

with open('./input.txt', 'r') as f:
    lines = f.readlines()

    f.close()

    for line in lines:
        spaceCount = 0
        for c in line:
            if(c == '\n'):
                if(not parseType):
                    output += ('<br>')
                else:
                    output += '\n'

                spaceCount = 0
            elif(c == ' '):
                spaceCount += 1

                if spaceCount == 4:                    
                    # output += ('\t')
                    if(not parseType):
                        output += ('&emsp;&emsp;')
                    else:
                        output += '\t'

                    spaceCount = 0
            else:
                if spaceCount > 0:
                    output += (' ')
                    spaceCount = 0
                output += (c)

print(output)