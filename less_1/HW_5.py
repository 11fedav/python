revenue = int(input('Какая выручка у фирмы: '))
costs = int(input('Какие издержки у фирмы: '))

if revenue > costs:
    print('Фирма работает с прибылью')
else:
    print('Фирма работает с убытком')

profit = revenue - costs
print('Прибыль составила: ', profit)

employee = int(input('Какое количество сотрудников в фирме: '))
prempl = profit / employee
print('Прибыль в расчёте на одного сотрудника составила: ', prempl)