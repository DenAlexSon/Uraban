mutable_list = ['яблоко','груша','виноград']
mutable_list[1] = ['абрикос']
print(mutable_list)


immutable_var = 1,2,3,4,True,'sos'
print(immutable_var)
print('кортеж относится к неизменяемому типу данных, мы можем использовать его, когда необходимо «запретить» менять значения элементов списка')
immutable_var[1]=21
