Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var = '1'
>>> print type(var)
<type 'str'>
>>> new_var = int(var) + 1
>>> print new_var
2
>>> var = 1
>>> page_num = 1
>>> print "第", page_num, "页"
第 1 页
>>> print type(page_num)
<type 'int'>
>>> print "第" + str(page_num) + "页"
第1页
>>> import random
>>> random.Random()
<random.Random object at 0x02298FA0>
>>> random.choice("['a', 'b', 'c']")
','
>>> random.choice("['a', 'b', 'c']")
' '
>>> random.choice("['a', 'b', 'c']")
'a'
>>> test_list = ['a', 'b', 'c']
>>> random.choice(test_list)
'c'
>>> random.choice("['a', 'b', 'c']")
','
>>> random.choice(['a', 'b', 'c'])
'a'
>>> random.choice(['a', 'b', 'c'])
'b'
>>> list1 = ['physics', 'chemistry', 1997, 2000];
>>> list1[0]
'physics'
>>> list1[0:2]
['physics', 'chemistry']
>>> list1[1:3]
['chemistry', 1997]
>>> list2 = [1, 2, 3, 4, 5 ];
>>> list1 + list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
>>> list1 * 2
['physics', 'chemistry', 1997, 2000, 'physics', 'chemistry', 1997, 2000]
>>> list2 * 3
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> 3 in [1, 2, 3]
True
>>> if 3 in [1, 2, 3]:
	print OK

	

Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print OK
NameError: name 'OK' is not defined
>>> if 3 in [1, 2, 3]:
	print "OK"

	
OK
>>> list = []
>>> list.append("a")
>>> list
['a']
>>> list = ['physics', 'chemistry', 1997, 2000];
>>> list[2]
1997
>>> list[2] = 2001
>>> list
['physics', 'chemistry', 2001, 2000]
>>> del list[2]
>>> list
['physics', 'chemistry', 2000]
>>> list1
['physics', 'chemistry', 1997, 2000]
>>> list2
[1, 2, 3, 4, 5]
>>> cmp(list1, list2)
1
>>> list1 = [2,3,4,5,6]
>>> cmp(list1, list2)
1
>>> list1 = [0,1]
>>> cmp(list1, list2)
-1
>>> list1 = [789, 'zzz']
>>> cmp(list1, list2)
1
>>> list1 = [456, 'aaa']
>>> cmp(list1, list2)
1
>>> len(list1)
2
>>> list2 = [1, 2, 3, 4, 5 ]
>>> max(list2)
5
>>> list2
[1, 2, 3, 4, 5]
>>> list2.reverse()
>>> list2
[5, 4, 3, 2, 1]
>>> 
