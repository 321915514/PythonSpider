'''r=open('text','r',encoding='utf8')
print(r.read())
r.close()'''
# w=open('text1','r',encoding='utf8')
# print(w.write('hello world\n'))
# print(w.write('alex\n'))
# print(w.readline().strip())
# for i in w.readlines():
# print(i)
# w.close()
# 最优方法
# import time
# for i in range(30):
#   print('*',end='')
#  flush=True
#   time.sleep(0.2)
# w.close()
# 两个方法。seek调整光标位置。tell打印光标位置。flush将缓冲区的文件存到磁盘。
r = open('text', 'r', encoding='utf8')
w = open('text3', 'w', encoding='utf8')
count = 0
for i in r:
    count += 1
    if count == 4:
        i = ''.join((i.strip(), 'hello world\n'))
    w.write(i)
r.close()
w.close()
