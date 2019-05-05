import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/text/').content
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    str1 = 'hello world'
    print str1.upper();
    print str1.replace('world', 'nowcoder')
    str2 = '\n\rhello world \r\n'
    print str2
    print 1, str2.lstrip()
    print 2, str2.rsplit()
    print 3, str2.startswith('hel')
    print 4, str2.endswith('l')
    print 5, str1 + str2;
    print 6, len(str2)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, str1.split(' ')
    print 9, str1.find('l')


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5 | 3, 5 & 3, 5 ^ 3


def demo_buidinfunction():
    x = 2
    y = 3.3
    print x, y, type(x), type(y)
    print 1, max(2, 1), min(3, 5)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x + 3')
    print 7, chr(97), ord('a')
    print 8, divmod(11, 3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10

    score = 65
    # for (int i=0; i<10; i++)
    # break, continue, pass
    for i in range(0, 10):
        if i == 0:
            pass
        if i < 5:
            continue
        # print 4, i
        if i == 6:
            break
        print 4, i


def demo_list():
    lista = [1, 2, 3]  # vector Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 14
    tuplea = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print listaa


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {1: 1, 2: 4, 3: 9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value :', key, value
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](1, 2)
    print 5, dictb.get('-')(15, 3)
    dictb['*'] = 'x'
    print 6, dictb
    dicta.pop(3)  # 3 is key
    print 7, dicta
    del dicta[1]
    print 8, dicta


def demo_set():
    list = [1, 2, 3];
    seta = set(list)
    setb = set((2, 3, 4))
    print 1, seta
    # seta.add(4)
    # print 2, seta
    print 3, seta.intersection(setb), seta & setb
    print 4, seta.union(setb), seta | setb
    print 5, seta - setb
    seta.add('x')
    print 6, seta
    print len(seta)
    print seta.isdisjoint(set((1, 2)))


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group


class Guest(User):
    type = 'GUEST'

    def __init__(self, name, uid):
        User.__init__(self, name, uid)

    def __repr__(self):
        return 'im guest ' + self.name + ' ' + str(self.uid)


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('g1', 201)
        # raise ValueError('error')


def demo_exception():
    try:
        print 2 / 1
        # print 2 / 0
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print 'error:', e
    finally:
        print 'clean up'


def demo_random():
    # random.seed(1)
    print 1, random.random()  # 0-1
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print 5, a


def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)

    str = 'a@163.com;b@gmail.coom;c@qq.com;e@163.com;z@qq.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(str)

    str = '<html><h>title</h><body></body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(str)
    p4 = re.compile('<h>([^<]+)</h>')
    print 5, p4.findall(str)

    str = 'xxx2016-16-11yy'
    p5 = re.compile('\d\d\d\d-\d\d-\d\d')
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print 6, p5.findall(str)


if __name__ == '__main__':
    user1 = User('u1', 1)
    print user1
    admin1 = Admin('a1', 101, 'g1')
    print admin1

    print create_user('USERX')

    print 'hello world'
    # comment
    # demo_string()
    # demo_operation()
    # demo_buidinfunction()
    # demo_controlflow()\
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_exception()
    # demo_random()
    demo_re()
