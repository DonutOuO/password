password = 'a123456'
x=3

while x > 0 :
	x = x - 1
	ans = input('請輸入密碼:')
	if ans == password :
		print('登入成功')
		break
	else :
		print('密碼錯誤')
		if x > 0:
			print('還有',x,'次機會')
		else:
			print('鎖帳號 恭喜')