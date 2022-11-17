import re

from model.Hashmap import SymbolTable
from model.Pif import ProgramInternalForm
from model.Specifications import operators, separators, reservedWords


# operators = ['+' '-' '*' '/' '==' '!=' '=' '<' '<='  '>=' 'or' 'and' '!' '%']
class Scanner:

    def isIdentifier(self, token):
        return re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', token) is not None

    def isConstant(self, token):
        return re.match('^(0|[+-]?[1-9][0-9]*)$', token) is not None or \
               re.match('^\'.\'$', token) is not None or \
               re.match('^\".*\"$', token) is not None

    # split dupa spatii, separatori, operatori
    # ? ( x % i == 1 ) {ok=false;}
    def getToken(self, line: str):
        initialTokens = re.split(" +", line.strip())
        tokens = []
        for token in initialTokens:
            tokenSplitBySeparators = re.split(self.getSeparatorRegex(), token)
            for tokenSplit in tokenSplitBySeparators:
                tokens += [x for x in re.split(self.getOperatorRegex(), tokenSplit) if x != '']
        return tokens

    def getSeparatorRegex(self):
        separators.sort(key=len, reverse=True)
        returnString = "("
        for separator in separators:
            returnString += re.escape(separator) + "|"
        return returnString[:-1] + ")"

    def getOperatorRegex(self):
        operators.sort(key=len, reverse=True)
        returnString = "("
        for operator in operators:
            returnString += re.escape(operator) + "|"
        return returnString[:-1] + ")"

    def scan(self):
        fileName = input("Insert file name: ")

        symbolTable = SymbolTable()
        pif = ProgramInternalForm()

        with open(fileName, 'r') as file:
            lineNo = 0
            for line in file:
                lineNo += 1
                for token in self.getToken(line):
                    if token in separators + operators + reservedWords:
                        pif.add(token, -1)
                    elif self.isIdentifier(token):
                        id = symbolTable.getOrAdd(token)
                        pif.add("id", id)
                    elif self.isConstant(token):
                        id = symbolTable.getOrAdd(token)
                        pif.add('const', id)
                    else:
                        raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

        with open("Pif.out", 'w') as file:
            file.write('Program Internal Form: \n' + str(pif) )
        with open("ST.out", 'w') as file:
            file.write('Symbol Table: \n' + str(symbolTable))
        print("Lexically correct")