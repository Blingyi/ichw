__author__ = "Tanghaoyi"
__pkuid__  = "1800011775"
__email__  = "1800011775@pku.edu.cn"
from urllib.request import urlopen
currency_from = str(input())#现在所拥有类型
currency_to = str(input())#要转化的类型
amount_from = str(input())#转化的金额
def up(x): #选择大写字符串，并将其转化成为字典；x是一个集合，要大写的字符串类型
    b = ''
    for i in range(len(x)) :
        if str(x[i:i+4]) == 'true'or str(x[i:i+5])=='false':
            b = b+x[i].upper()
        else:
            b = b+x[i]
    return b
    pass

def exchange(currency_from, currency_to, amount_from):#输出所需要转化的汇率
   
    doc=urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    result=eval(up(jstr))["to"].split()[0]
    return(float(result))
    pass

def test_up():#测试up函数
    assert(up('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')==
           '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : True, "error" : "" }')

def test_exchange():#测试exchange函数
    assert(exchange('USD','EUR','2.5')==2.1589225)

def testAll() :#测试all
    test_up()
    test_exchange()
    print("All tests passed")

def main():
    testAll()
    print(exchange(currency_from, currency_to, amount_from))
if __name__ == '__main__':
    main()
