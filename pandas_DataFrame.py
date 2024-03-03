import pandas as p
data = p.DataFrame({'Yes': [20,40] , 'No': [100,90]})
#print(data)
sen = p.DataFrame({'Arslan':['I d k'], 'Adil':['I K']})
#print(sen)
sen_with_index = p.DataFrame({'Mud':['see index','A'], 'Ahsan':['see index','B']},
                             index=['Good','Grade vice 😉'])
print(sen_with_index)