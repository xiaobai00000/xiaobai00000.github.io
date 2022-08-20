class Food:#F要大写。Food作为一类
	def __init__(self,like,hate):#物件object
		self.like = like#属性attribute
		self.hate = hate
a = Food('orange','apple')#填入变量
print(a.hate)

#结果：apple
