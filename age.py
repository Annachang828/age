driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('請你輸入有or沒有')

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('不可能吧')
elif driving == '沒有':
	if age >= 18:
		print('去考駕照壓')
	else:
		print('再過幾年就可以考了 再等等')
else:
	print('請你輸入有or沒有')