password = 'a123456'
x=2

while True :
	ans = input('請輸入密碼:')
	if ans == password :
		print('登入成功')
		break
	if ans != password :
		print('"密碼錯誤 還有',x,'次機會')
		x=x-1
		if x == 0 :
			break