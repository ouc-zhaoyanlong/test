from father import Father
from mother import Mother
class Child(Father,Mother):
	def __init__(self,money,faceValue):
		'''
		多继承时，调用父类构造方法的格式：父类名.__init__(self,[,参数列表])
		单继承时，调用父类构造方法的格式：super.__init__(self,[,参数列表])
		'''
		Father.__init__(self,money)
		Mother.__init__(self,faceValue)