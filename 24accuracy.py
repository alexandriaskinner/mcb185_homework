# 24accuracy.py by Alexandria Skinner

def accuracy_F1(TP, TN, FP, FN):
	A  = (TP+TN) / (TP+TN+FP+FN)    #Accuracy
	p  = TP / (TP+FP)               #precision - to calculate F1
	r  = TP / (TP+FN)               #recall - to calculate F1
	F1 = 2*p*r / (p+r)              #F1
	return A, F1

print(accuracy_F1(3, 6, 1, 3))
print(accuracy_F1(9, 6, 3, 1))
print(accuracy_F1(29, 31, 2, 8))
