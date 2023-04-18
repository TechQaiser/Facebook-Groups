import os
path = 'data/split.txt'
if os.path.exists(path):
    os.remove(path)
while True:
	put = input("Paste Your Data Here : ")
	if put in ['',' ']:
		exit('done process is stopped')
	print(put.split('|')[0])
	open(path,'a',encoding='utf-8').write(put.split('|')[0]+'\n')
