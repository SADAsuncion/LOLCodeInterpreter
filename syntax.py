import keywords

lexemes = keywords.main()
success = 1

str = '''
I HAS A var1
I HAS A var2
I HAS A var3 ITZ 123
I HAS A var4 ITZ
KTHXBYE
'''
# print(str.splitlines())

comparison = ['BOTH SAEM', 'DIFFRINT']
varidents = []
hasHai = -1
hasKthxbye = -1
hasWazzup = -1
hasBuhbye = -1
hasVarDec = 0
lines = lexemes.splitlines()

for h in range(0, len(lines)):
    lexeme = keywords.lex(lexemes.splitlines()[h])
    if ['BTW', 'Comment Identifier'] in lexeme:
        lexeme.pop(lexeme.index(['BTW', 'Comment Identifier'])+1)
        lexeme.pop(lexeme.index(['BTW', 'Comment Identifier']))
    for i in range(0, len(lexeme)):
        ## PROGRAM BLOCK SYNTAX - HAI
        if lexeme[i][0] == 'HAI' and hasHai == -1 and hasKthxbye == -1:
            hasHai = 0
            break
        else:
                if lexeme[i][0] == 'HAI' and hasHai > -1:
                    print(f'>> SyntaxError in line {h+1} near <HAI>: \n\tAlready has HAI; it must be declared once')
                    success = 0
                    break
                elif lexeme[i][0] == 'HAI' and hasKthxbye > -1:
                    print(f'>> SyntaxError in line {h+1} near <HAI>: \n\HAI must be declared before KTHXBYE')
                    success = 0
                    break
        if hasHai == 0:
            ## VARIABLE BLOCK SYNTAX - WAZZUP
            if lexeme[i][0] == 'WAZZUP' and hasWazzup == -1 and hasBuhbye == -1:
                hasWazzup = 0
                break
            else:
                if lexeme[i][0] == 'WAZZUP' and hasWazzup > -1:
                    print(f'>> SyntaxError in line {h+1} near <WAZZUP>: \n\tAlready has WAZZUP; it must be declared once')
                    success = 0
                    break
                elif lexeme[i][0] == 'WAZZUP' and hasBuhbye > -1:
                    print(f'>> SyntaxError in line {h+1} near <WAZZUP>: \n\tWAZZUP must be declared before BUHBYE')
                    success = 0
                    break
            ## VARIABLE DECLARATION SYNTAX
            if lexeme[i][0] == 'I HAS A' and hasWazzup == 0:
                if len(lexeme) < 2 or lexeme[i+1][1] != 'Variable Identifier':
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tI HAS A must have a variable identifier')
                    success = 0
                    break
                elif len(lexeme) > 2:
                    if lexeme[i+2][0] != 'ITZ':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'ITZ' keyword?")
                        success = 0
                        break
                    elif len(lexeme) < 4 or (lexeme[i+3][1] != 'Literal' and lexeme[i+3][1] != 'Variable Identifier'):
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\tITZ must have a literal or variable identifier')
                        success = 0
                        break
                hasVarDec = 1
                varidents.append(lexeme[i][0])
                break
            else:
                if lexeme[i][0] == 'I HAS A' and hasWazzup != -1:
                    print(f'>> SyntaxError in line {h+1} near <I HAS A>: \n\tI HAS A statements must be inside WAZZUP and BUHBYE')
                    success = 0
                    break
                elif lexeme[i][0] != 'I HAS A' and lexeme[i][0] != 'BUHBYE' and lexeme[i][0] != 'KTHXBYE' and hasWazzup == 0 and hasBuhbye == -1: 
                    print(f'>> SyntaxError in line {h+1} in <WAZZUP> block: \n\tonly I HAS A statements can be inside WAZZUP and BUHBYE')
                    success = 0
                    break
            ## VARIABLE BLOCK SYNTAX - BUHBYE
            if lexeme[i][0] == 'BUHBYE' and hasWazzup == 0:
                hasBuhbye = 0
                hasWazzup = 1
                break
            else:
                if lexeme[i][0] == 'BUHBYE' and hasWazzup == -1 and hasBuhbye == -1:
                    print(f'>> SyntaxError in line {h+1} near <BUHBYE>: \n\BUHBYE must be declared after WAZZUP')
                    success = 0
                    break
                elif lexeme[i][0] == 'BUHBYE' and hasWazzup == 0 and hasBuhbye == 1:
                    print(f'>> SyntaxError in line {h+1} near <BUHBYE>: \n\tAlready has BUHBYE; it must be declared once')
                    success = 0
                    break
            
            ## COMPARISON SYNTAX - BOTH SAEM
            if lexeme[i][0] == 'BOTH SAEM':
                if len(lexeme) != 4 and len(lexeme) != 7:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH SAEM <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                    success = 0
                    break
                elif lexeme[i+1][0].isnumeric() == False or lexeme[i+1][0].isnumeric() == False:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                    success = 0
                    break
                elif len(lexeme) == 4:
                    if lexeme[i+2][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+3][0].isnumeric() == False or lexeme[i+3][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tBOTH SAEM only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                elif len(lexeme) == 7:
                    if lexeme[i+2][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                        success = 0
                        break
                    elif lexeme[i+4][0].isnumeric() == False or lexeme[i+4][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                    elif lexeme[i+5][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+6][0].isnumeric() == False or lexeme[i+6][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                else:
                    break
            ## COMPARISON SYNTAX - DIFFRINT
            if lexeme[i][0] == 'DIFFRINT':
                if len(lexeme) != 4 and len(lexeme) != 7:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tDIFFRINT <value> [[AN BIGGR OF|SMALLR OF] <value>] AN <value>')
                    success = 0
                    break
                elif lexeme[i+1][0].isnumeric() == False or lexeme[i+1][0].isnumeric() == False:
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                    success = 0
                    break
                elif len(lexeme) == 4:
                    if lexeme[i+2][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+3][0].isnumeric() == False or lexeme[i+3][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tDIFFRINT only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                elif len(lexeme) == 7:
                    if lexeme[i+2][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+1][0]}>: \n\t{lexeme[i+2][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+3][0] != 'SMALLR OF' and lexeme[i+3][0] != 'BIGGR OF':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+2][0]}>: \n\t{lexeme[i+3][0]} is recognized incorrectly. Perhaps you need a 'SMALLR OF' or 'BIGGR OF' keyword?")
                        success = 0
                        break
                    elif lexeme[i+4][0].isnumeric() == False or lexeme[i+4][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                    elif lexeme[i+5][0] != 'AN':
                        print(f">> SyntaxError in line {h+1} near <{lexeme[i+4][0]}>: \n\t{lexeme[i+5][0]} is recognized incorrectly. Perhaps you need an 'AN' keyword?")
                        success = 0
                        break
                    elif lexeme[i+6][0].isnumeric() == False or lexeme[i+6][0].isnumeric() == False:
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tSMALLR OF and BIGGR OF only accepts NUMBR or NUMBAR type')
                        success = 0
                        break
                else:
                    break
            ##BOOLEAN SYNTAX - BOTH OF
            if lexeme[i][0] == "BOTH OF":
                if len(lexeme) > 4 or len(lexeme) <= 3:
                    success = 0
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                    break
                elif len(lexeme) == 4:
                    if lexeme[i+1][0] != 'WIN':
                        if lexeme[i+1][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    elif lexeme[i+1][0] != 'FAIL':
                        if lexeme[i+1][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    
                    if lexeme[i+2][0] != 'AN':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                        break
                
                    if lexeme[i+3][0] != 'WIN':
                        if lexeme[i+3][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                            break
                        break
                    elif lexeme[i+3][0] != 'FAIL':
                        if lexeme[i+3][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                            break
                        break
            ##BOOLEAN SYNTAX - EITHER OF
            if lexeme[i][0] == "EITHER OF":
                if len(lexeme) > 4 or len(lexeme) <= 3:
                    success = 0
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                    break
                elif len(lexeme) == 4:
                    if lexeme[i+1][0] != 'WIN':
                        if lexeme[i+1][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    elif lexeme[i+1][0] != 'FAIL':
                        if lexeme[i+1][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    
                    if lexeme[i+2][0] != 'AN':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                        break
                
                    if lexeme[i+3][0] != 'WIN':
                        if lexeme[i+3][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                            break
                        break
                    elif lexeme[i+3][0] != 'FAIL':
                        if lexeme[i+3][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                            break
                        break
            
            ##BOOLEAN SYNTAX - WON OF
            if lexeme[i][0] == "WON OF":
                if len(lexeme) > 4 or len(lexeme) <= 3:
                    success = 0
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tBOTH OF [WIN|FAIL] AN [WIN|FAIL]')
                    break
                elif len(lexeme) == 4:
                    if lexeme[i+1][0] != 'WIN':
                        if lexeme[i+1][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    elif lexeme[i+1][0] != 'FAIL':
                        if lexeme[i+1][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    
                    if lexeme[i+2][0] != 'AN':
                        success = 0
                        print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tThere is a need for AN to indicate "and".')
                        break
                
                    if lexeme[i+3][0] != 'WIN':
                        if lexeme[i+3][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                            break
                        break
                    elif lexeme[i+3][0] != 'FAIL':
                        if lexeme[i+3][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\t Operands of BOTH OF must be either WIN OR FAIL.')
                            break
                        break
            
            ##BOOLEAN SYNTAX - NOT
            if lexeme[i][0] == "NOT":
                if len(lexeme) > 3 or len(lexeme) < 2: 
                    success = 0
                    print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tIncorrect number of parameters, see correct syntax. \n\tNOT [WIN|FAIL]')
                    break
                elif len(lexeme) == 2:
                    if lexeme[i+1][0] != 'WIN':
                        if lexeme[i+1][0] != 'FAIL':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
                    elif lexeme[i+1][0] != 'FAIL':
                        if lexeme[i+1][0] != 'WIN':
                            success = 0
                            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tOperands of BOTH OF must be either WIN OR FAIL.')
                            break
        else:
            print(f'>> SyntaxError in line {h+1} near <{lexeme[i][0]}>: \n\tStatements must be inside HAI and KTHXBYE')
            success = 0
            break

        ## PROGRAM BLOCK SYNTAX - KTHXBYE
        if lexeme[i][0] == 'KTHXBYE' and hasHai == 0:
                hasKthxbye = 0
                hasHai = 1
                break
        else:
            if lexeme[i][0] == 'KTHXBYE' and hasHai == -1 and hasKthxbye == -1:
                print(f'>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tKTHXBYE must be declared after HAI')
                success = 0
                break
            elif lexeme[i][0] == 'KTHXBYE' and hasHai == 0 and hasKthxbye == 1:
                print(f'>> SyntaxError in line {h+1} near <KTHXBYE>: \n\tAlready has KTHXBYE; it must be declared once')
                success = 0
                break

if hasHai == 0 and hasKthxbye == -1:
    print(f'>> SyntaxError in line {h+1} in <HAI>: \n\tHAI must be enclosed with KTHXBYE')

if hasWazzup == 0 and hasBuhbye == -1:
    print(f'>> SyntaxError in line {h+1} in <WAZZUP>: \n\tWAZZUP must be enclosed with BUHBYE')

if success == 1:
    print('>> No syntax errors.')
        