from   sklearn.tree   import  DecisionTreeClassifier  #   decisionTree classifier only
#   this  is  for  apple  and orange
#   here  smooth is for apple and bumpy is for orange
features=[[100,0],[120,0],[130,1],[150,1]]
##  here  0 means  smooth  and  1  means  bumpy
#  now answers  accordingly
label=["apple","apple","orange","orange"]
#   calling  DecisionTree classifier
clf=DecisionTreeClassifier()

#  now time for training   data
trained=clf.fit(features,label)
#  now predicting
output=trained.predict([[133,0]])
print(output)