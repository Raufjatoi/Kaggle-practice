import pandas as pd # pd is kida alias u can use p or anythin ya like 
import numpy as np 
 
 #np.arrange(0,20).reshape(5,4)

 ## Dataframe

info = pd.DataFrame(data=np.arrange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],column=['colum1','colum2','colum3','colum4'])
#print(info.info())
# indexing 
#use iloc and loc

#its not workin here so i gona use jupyter