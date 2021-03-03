def notas(*num, sit=False):
    n = []
    turma = {}
    turma['Total'] = len(num)
    turma['maior'] = max(num)
    turma['menor'] = min(num)
    turma['media'] = sum(num) / len(num)
    if sit == True:
        if turma['media'] >= 7:
            turma['situação'] = 'Boa'
        elif turma['media'] >= 5:
            turma['situação'] = 'Regular'
        else:
            turma['situação'] = 'Ruim'
    return turma


resp = notas(6,5,9,8,9,sit = True)
print(resp)
