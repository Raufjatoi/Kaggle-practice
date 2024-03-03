import pandas as p 
series = p.Series([1,2,3,4,5,6])
#print(series)
recipe = p.Series(['2  cups' , '2 packs' , '15 mins'],
                   index=['water','noodles 🍜','heat'],
                   name='cookin noodles')
print(recipe)
recipe.to_csv('recipe.csv')