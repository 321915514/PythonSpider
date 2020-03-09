import re


def input_number():
    while True:
        break_flag = False
        s = str(input('请输入你要计算的内容：'))
        if re.search('[A-z]', s):
            print('输入有误，请重新输入\n')
            break_flag = True
        else:
            re.sub(' ', '', s)
            break
    return s


s = input_number()


def jiajianchengchu(s):
    if re.search('\*', s):
        ret = (re.search('\d+\.?\d*\*\d+\.?\d*', s).group())
        x, y = re.split('\*', ret)
        num = str(float(x) * float(y))
        s = s.replace(s, num)
    elif re.search('/', s):
        ret = ((re.search('\d+\.?\d*[*/]\d+\.?\d*', s)).group())
        x, y = re.split('/', ret)
        if float(x) >= float(y):
            num = str(float(x) / float(y))
            s = s.replace(s, num)
        else:
            num = str(float(y) / float(x))
            s = s.replace(s, num)

    elif re.search('\+', s):
        ret = ((re.search('\d+\.?\d*\+\d+\.?\d*', s)).group())
        x, y = re.split('\+', ret)
        num = str(float(x) + float(y))
        s = s.replace(ret, num)

    elif re.search('-', s):
        if s.index('-') > 0:
            # x,y=((re.findall('\d+',s)))
            # num=str(float(x)+float(y))
            # s=s.replace(num)
            ret = ((re.search('\d+\.?\d*[\-]\d+\.?\d*', s)).group())
            x, y = re.split('-', ret)
            num = str(float(x) - float(y))
            s = s.replace(ret, num)
        else:
            if s.rindex('-') > 0:
                ret = ((re.search('\d+\.?\d*[\-]\d+\.?\d*', s)).group())
                ret = re.findall('\d+', ret)
                x, y = ret
                num = str(-(float(x) + float(y)))
                s = s.replace(ret, num)
            else:
                return s
    else:
        s = re.search('\d+', s).group()
    return s


def cheak_in(s):
    s = re.sub('\*\*', '*', s)
    s = re.sub('\+-', '-', s)
    s = re.sub('-\+', '-', s)
    s = re.sub('\+\+', '+', s)
    s = re.sub('--', '+', s)
    return s


def cheak(s):
    s = cheak_in(s)
    # str_ = re.search('\([^()]+\)', s).group()
    while re.search('\(', s):
        # str_=cheak_in(s)
        str_ = re.search('\([^()]+\)', s).group()
        str_2 = jiajianchengchu(str_)
        s = s.replace(str_, str_2)
    else:
        while re.search('[\\\+|-]', s):
            s = cheak_in(s)
            str_2 = jiajianchengchu(s)
            s = str_2
            print(str_2)


cheak(s)
