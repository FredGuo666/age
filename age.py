drving = input('请问你开过车吗？')
if drving != '有' and '没有':
	print('只能输入 有/没有')	
	raise SystemExit

age = input('请问你的年龄是?')
age = int(age)
if drving == '有':
	if age >= 18:
		print('你通过测验了')
	else:
		print('你没有通过测验') 
elif drving == '没有':
	if age >= 18:
		print('抓紧时间快去考驾照吧')
	else:
		print('很好，再过几年就能考驾照了')
	