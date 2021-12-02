def negateSimpleClause(clause):
    if clause[0] == '-':
        return clause[1:]
    return '-' + clause

def negateComplexClause(clause):
    claArr = clause.split(' ')
    negated = []
    for literal in claArr:
        if(literal == 'OR'):
            negated.append('AND')
        elif(literal == 'AND'):
            negated.append('OR')
        else:
            negated.append(negateSimpleClause(literal))
    return ' '.join(negated)
