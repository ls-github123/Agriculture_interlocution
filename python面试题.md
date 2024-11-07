#### python中的基本数据类型

~~~
可变对象是指可以修改其值的对象，Python中参数的传递都是“引用传递”，不是“值传递”
可变对象的内存地址可能会改变，而不可变对象的内存地址永远不会改变；
对“可变对象”进行“写操作”，直接作用于原对象本身。
对“不可变对象”进行“写操作”，会产生一个新的“对象空间”，并用新的值填充这块空间（起到其他语言的“值传递”效果，但不是“值传递”）。。
传递参数是可变对象（如：字典、列表、自定义的其他可变对象等），实际传递的还是对象的引用。在函数体中不创建新的对象拷贝，而是可以直接修改所传递的对象。
传递参数是不可变对象（例如：int、float、字符串、元组、布尔值等），实际传递的还是对象的引用，早“赋值操作”时，由于不可变对象无法修改，系统会创建一个新的对象。

可变：字典、列表、集合
不可变：数字、元组、字符串

查找速度:
set>dict>list
~~~

#### 深拷贝和浅拷贝的区别

~~~
浅拷贝使用的是copy.copy,主要是地址的拷贝，只拷贝第一层，第一层改变的时候不会改变，内层改变才会改变。深拷贝是值的拷贝，不会随着原数据的变化而变化

import copy
list = [[1, 2], 'feng', 66]
a = copy.copy(list)
b = copy.deepcopy(list)


# list[1]=4

# print(a)
# print(b)
#输出结果
# [[1, 2], 'feng', 66]
# [[1, 2], 'feng', 66]

list[0][0] = 8
print(a)
print(b)
#输出结果
# [[8, 2], 'feng', 66]
# [[1, 2], 'feng', 66]


import copy
list = ['feng',[1,2], 66]
a = copy.copy(list)
b = copy.deepcopy(list)

print(id(list[0]))
print(id(a[0]))
print(id(b[0]))
print(id(list[1]))
print(id(a[1]))
print(id(b[1]))
#输出结果
# 4306918640
# 4306918640
# 4306918640
# 4307415552
# 4307415552
# 4307500992

~~~

#### 元组和列表的区别

~~~
可变性：元组是不可变的，一旦创建就不能修改，而列表是可变的，可以添加、删除和修改元素。

使用场景：元组适合用于存储一组不可变的数据，如坐标、颜色等，而列表适合用于存储一组可变的数据，如动态添加的任务列表、用户列表等。

性能：由于元组是不可变的，所以在某些场景下，它的性能比列表更好，如作为字典的键或者作为函数的参数等。

总之，元组和列表都是 Python 中的序列类型，二者的主要区别在于可变性和使用场景。如果需要存储一组不可变的数据，就应该使用元组；如果需要存储一组可变的数据，就应该使用列表。

元组是使用数组来实现的，它们的元素在内存中是连续存储的。由于元素是不可变的，因此它们的地址是固定的，使得元组比列表更加高效。

在 Python 中，列表是使用动态数组来实现的。动态数组是一种可以自动扩展大小的数组，它可以动态地分配内存来存储数据。当创建一个列表时，Python 会在内存中分配一块连续的内存，用来存储列表中的元素。与元组不同的是，列表中的元素是可变的，因此它们的值可以被修改。当列表中的元素数量超过了数组的大小时，Python 会自动分配更多的内存来扩展数组的大小，以容纳更多的元素。

列表的实现还包括一些额外的数据结构，如长度和指针。长度是列表中元素的数量，指针用于跟踪列表中元素的位置。当添加或删除元素时，指针会被更新，以便正确地定位元素的位置。

总之，列表是使用动态数组来实现的，它们的元素在内存中是连续存储的。由于元素是可变的，因此列表的实现还包括一些额外的数据结构，如长度和指针。与元组相比，列表的访问速度稍慢，但可以动态地添加、删除和修改元素。

元组中添加了静态资源缓存，在执行析构函数(往往用来做“清理善后” 的工作)时，不仅对象本身没有被回收，底层的指针也会缓存，再次分配就会快。
~~~

#### 元组常用方法

##### 1.count方法：统计元素在元组中出现的次数

```python
tup1 = ('apple', 'banana', 'cherry', 'apple')
print(tup1.count('apple'))  # 2
```

##### 2.index方法：返回元素在元组中的索引位置

```python
tup1 = ('apple', 'banana', 'cherry', 'apple')
print(tup1.index('banana'))  # 1
```

##### 3.len方法：返回元组中元素的个数

```python
tup1 = ('apple', 'banana', 'cherry', 'apple')
print(len(tup1))  # 4
```

##### 4.元组解包：将元组中的每个元素赋值给一个变量

```python
tup1 = ('apple', 'banana', 'cherry')
a, b, c = tup1
print(a)  # 'apple'
print(b)  # 'banana'
print(c)  # 'cherry'
```

##### 5.比较运算符：用于比较两个元组的大小（从第一个元素开始比较，若相同则继续往下比较）

```python
tup1 = ('apple', 'banana', 'cherry')
tup2 = ('apple', 'banana', 'orange')
tup3 = ('apple', 'banana', 'cherry')
print(tup1 > tup2)  # False
print(tup1 == tup3)  # True
print(tup1 < tup2)  # True
```

##### 6.合并运算符：用于连接两个元组

```python
tup1 = ('apple', 'banana', 'cherry')
tup2 = ('orange', 'lemon', 'pear')
tup3 = tup1 + tup2
print(tup3)  # ('apple', 'banana', 'cherry', 'orange', 'lemon', 'pear')
```

##### 7.in运算符：用于判断元素是否在元组中

```python
tup1 = ('apple', 'banana', 'cherry')
print('apple' in tup1)  # True
print('orange' in tup1)  # False
```

### 为什么元组是不可变的

~~~
主要是为了保证数据的安全性和一致性。元组一旦创建，它的元素就不能更改。这是因为元组中的每个元素的内存地址在创建后就固定下来，与元素的值绑定在一起。如果元组中的某个元素是一个可变对象，如列表或字典，那么这个可变对象的值虽然可以改变，但是元组本身的引用不会改变，因此元组本身仍然是不可变的。通常不可变类型在创建时间上优于对应的可变类型
~~~



#### 字符串常用方法

- capitalize()。将字符串的第一个字母转换为大写，其他字母保持不变。1

- lower()。将字符串中的所有字母转换为小写。
- upper()。将字符串中的所有字母转换为大写。
- replace()。将字符串中的某个子串替换为另一个子串。
- split()。将字符串分割为多个子串，并返回一个列表。
- len()。获取字符串长度。23

- +。字符串拼接。245

- 索引。获取字符串中的字符。23456

- 切片。获取字符串的子串。
- find()。查找子串在字符串中第一次出现的位置。46

- index()。查找子串在字符串中第一次出现的位置。
- count()。统计字符串中的某个元素出现的次数。6

- format()。字符串格式化。45

- in。判断字符串中是否包含指定字符。

Find和Index有什么区别

~~~
1. 返回值的类型

Index函数返回的是一个整数，表示子字符串在字符串中第一次出现的位置。如果子字符串不存在，Index函数会抛出ValueError异常。

Find函数返回的也是一个整数，表示子字符串在字符串中第一次出现的位置。如果子字符串不存在，Find函数会返回-1。

2. 处理速度

从处理速度上来看，Index函数比Find函数要快一些。这是因为Index函数在查找子字符串时，会先使用快速匹配算法进行一次匹配，如果匹配成功，则直接返回匹配位置。而Find函数则是使用朴素的匹配算法，需要逐个字符地匹配，速度较慢。

3. 索引值的可变性

在Python中，字符串是不可变的对象。这意味着一旦创建了一个字符串，就无法对其进行修改。因此，如果我们使用Index或Find函数查找一个子字符串的位置，那么返回的索引值是不可变的。如果我们想要修改字符串，就需要创建一个新的字符串。例如，如果我们想要在字符串中替换某个子字符串，就需要使用replace函数。

4. 区分大小写和不区分大小写

在默认情况下，Index和Find函数都是区分大小写的。这意味着如果我们在字符串中查找一个子字符串，必须确保大小写完全匹配才能找到。如果我们想要不区分大小写地查找子字符串，就需要使用lower函数将字符串转换为小写，然后再进行查找。

5. 可以查找多个子字符串

在Python中，我们可以使用Index和Find函数查找一个子字符串的位置。但是，如果我们想要查找多个子字符串的位置，就需要使用其他函数，比如re模块中的findall函数。这个函数可以查找所有匹配的子字符串，并将它们的位置返回为一个列表。

6. 应用场景的不同

Index和Find函数在应用场景上也有所不同。一般来说，如果我们知道要查找的子字符串一定会在字符串中出现，就可以使用Index函数。如果我们不确定子字符串是否存在，可以使用Find函数，因为它不会抛出异常。如果我们需要查找多个子字符串的位置，就需要使用其他函数，比如re模块中的findall函数。
~~~

#### 列表常用方法

##### 添加的方法 append、extend、insert

**注意：**extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中

append： 方法在列表ls最后(末尾)添加一个元素object

~~~
例子：
    [1, 2, 3, 4, 5, 6, 12]
    ls.append([1,"a"]) #添加列表
    print(ls)
    结果：[1, 2, 3, 4, 5, 6, 12, [1, 'a']]

~~~

insert：在列表第index位置，添加元素object。

~~~
  ls = [1,2,"a",["a",5,8]]
  ls.insert(3,"b")#在列表ls下标为3的位置插入元素 "b"
  print(ls)
  [1, 2, 'a', 'b',  ['a', 5, 8]]
~~~

extend ：在列表ls末尾添加一个列表iterable

~~~
ls = [1,2,"a",[4,5,"a"]]
lt = [1,"abc","b",[1,2]]
ls.extend(lt) #返回值为空，将列表lt的元素添加到列表ls末尾。
print(ls)
# [1, 2, 'a', [4, 5, 'a'], 1, 'abc', 'b', [1, 2]]
~~~

##### 查找:index

Index:列表ls中第一次出现元素value的位置

~~~
ls.index(value, start, stop) -> integer 返回一个整数
ls = [1,2,3,"a",3,5,"a",5,[1,7,"b"]]
print(ls.index("a"))
#结果：3
~~~



##### 删除的方法：clear、pop、remove

clear删除列表中的所有元素

~~~
ls = [1,2,3,"4",5,"a"]
ls.clear()
print(ls)
[]
~~~

pop:将列表中第index项元素取出，并从列表ls中删除该元素。若果省略index,则默认删除列表最后(末尾)一个元素，并返回该元素

~~~
ls.pop(index) -> item 返回删除的项
 
ls = [1,2,"a","y",[1,2,3],"b"]
ls.pop(0)#取出下标为0的元素，并从列表ls中删除。
1
print(ls)
[2, 'a', 'y', [1, 2, 3], 'b']
ls.pop() #默认取出列表ls最后一个元素，并删除。
'b'
print(ls)
[2, 'a', 'y', [1, 2, 3]
~~~

remove:将列表ls中出现的第一个元素value删除

~~~
ls.remove(value) -> None 返回值为空

参数：value -- 要删除的元素。
ls1 = [1,2,"a",3,1,1,55,"a,1"]
ls2 = [1,2,"a",3,1,1,55,"a,1"]
ls1.remove(1) #删除ls1中第一次出现的元素 1
ls2.remove("a") ##删除ls2中第一次出现的元素 "a"
print(ls1.remove(1)) #返回值为空

~~~

其它方法：

copy()： 生成一个新列表，复制ls中的所有元素

Count(): 统计列表中value元素出现的次数

Reverse():将列表ls中的元素反转

Sort():将原列表ls中的元素进行排序，意味着改变原来的列表，而不是返回一个列表

~~~
语法：ls.sort([key=None][,reverse=False])--无返回值，但是会对列表中的元素进行排序。
参数：
key-- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
reverse-- 可选参数，是否反向排序，默认为False。
ls = [1,3,7,2,4,5,6]
ls.sort()
print(ls)
[1, 2, 3, 4, 5, 6, 7]#原来的列表发生了改变
~~~

#### 字典常用方法

get(key,default)根据键获取对应的值，如果不存在，可以返回一个默认值

keys返回字典中所有的键

Values:返回字典中所有的值

items返回字典中所有的键值对

pop删除并返回指定键对应的值，如果不存在，可以返回一个默认值

popitem随机删除并返回字典中的一对键值对

clear 删除所有

Update(dict2)将字典dict2的键值对添加到当前字典中，如果键重复，用新的值替换旧的

Setdefault(key,default) 获取key对应的值，如果键不存在，则在字典中添加一个新的键值对，并返回默认值。

#### 17.字典底层实现，如果解决hash冲突？

~~~
python中的字典底层依靠哈希表(hash table)实现
解决哈希冲突的方法一般有：开放定址法、拉链法

开放定址法是从发生冲突的单元起，依次判断下一个单元是否为空，当达到最后一个单元时，再从表首依次判断。直到碰到空闲的单元或者探查完全部单元为止。

拉链法是将哈希值相同的元素构成一个同义词的单链表，并将单链表的头指针存放在哈希表的第i个单元中，查找、插入和删除主要在同义词链表中进行。链表法适用于经常进行插入和删除的情况。
~~~

#### 集合常用方法

~~~
集合set是一种无序的、唯一的的元素集，与数学中集合的概念类似，可对其进行交、并、差、补等逻辑运算。不支持索引、切片等序列操作，但仍支持成员关系运算符in-not in、推导式等操作。在特定的场合中可以体现出非常优秀的执行效率。

frozenset冻结集合，即不可变集合。frozenset的元素是固定的，一旦创建后就无法增加、删除和修改。其最大的优点是使用hash算法实现，所以执行速度快，而且frozenset可以作为dict字典的Key，也可以成为其他集合的元素。

集合内置方法完整列表

方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
~~~

#### 集合和列表的区别

~~~
集合具有以下特点：
1、无序；

2、可以用set()函数或者方括号{}创建，元素之间用逗号”,”分隔；

3、不可索引，不可切片；

4、不可以有重复元素。

列表具有以下特点：

1、有序；

2、可以用list()函数或者方括号[]创建，元素之间用逗号’,‘’分隔；

3、使用索引来访问元素，可切片；

4、可以有重复元素。
~~~



#### python中的内置函数

| 内置函数                                                     |                                                              |                                                              |                                                              |                                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [abs()](https://www.runoob.com/python/func-number-abs.html)  | [divmod()](https://www.runoob.com/python/python-func-divmod.html) | [input()](https://www.runoob.com/python/python-func-input.html) | [open()](https://www.runoob.com/python/python-func-open.html) | [staticmethod()](https://www.runoob.com/python/python-func-staticmethod.html) |
| [all()](https://www.runoob.com/python/python-func-all.html)  | [enumerate()](https://www.runoob.com/python/python-func-enumerate.html) | [int()](https://www.runoob.com/python/python-func-int.html)  | [ord()](https://www.runoob.com/python/python-func-ord.html)  | [str()](https://www.runoob.com/python/python-func-str.html)  |
| [any()](https://www.runoob.com/python/python-func-any.html)  | [eval()](https://www.runoob.com/python/python-func-eval.html) | [isinstance()](https://www.runoob.com/python/python-func-isinstance.html) | [pow()](https://www.runoob.com/python/func-number-pow.html)  | [sum()](https://www.runoob.com/python/python-func-sum.html)  |
| [basestring()](https://www.runoob.com/python/python-func-basestring.html) | [execfile()](https://www.runoob.com/python/python-func-execfile.html) | [issubclass()](https://www.runoob.com/python/python-func-issubclass.html) | [print()](https://www.runoob.com/python/python-func-print.html) | [super()](https://www.runoob.com/python/python-func-super.html) |
| [bin()](https://www.runoob.com/python/python-func-bin.html)  | [file()](https://www.runoob.com/python/python-func-file.html) | [iter()](https://www.runoob.com/python/python-func-iter.html) | [property()](https://www.runoob.com/python/python-func-property.html) | [tuple()](https://www.runoob.com/python/att-tuple-tuple.html) |
| [bool()](https://www.runoob.com/python/python-func-bool.html) | [filter()](https://www.runoob.com/python/python-func-filter.html) | [len()](https://www.runoob.com/python/att-string-len.html)   | [range()](https://www.runoob.com/python/python-func-range.html) | [type()](https://www.runoob.com/python/python-func-type.html) |
| [bytearray()](https://www.runoob.com/python/python-func-bytearray.html) | [float()](https://www.runoob.com/python/python-func-float.html) | [list()](https://www.runoob.com/python/att-list-list.html)   | [raw_input()](https://www.runoob.com/python/python-func-raw_input.html) | [unichr()](https://www.runoob.com/python/python-func-unichr.html) |
| [callable()](https://www.runoob.com/python/python-func-callable.html) | [format()](https://www.runoob.com/python/att-string-format.html) | [locals()](https://www.runoob.com/python/python-func-locals.html) | [reduce()](https://www.runoob.com/python/python-func-reduce.html) | unicode()                                                    |
| [chr()](https://www.runoob.com/python/python-func-chr.html)  | [frozenset()](https://www.runoob.com/python/python-func-frozenset.html) | [long()](https://www.runoob.com/python/python-func-long.html) | [reload()](https://www.runoob.com/python/python-func-reload.html) | [vars()](https://www.runoob.com/python/python-func-vars.html) |
| [classmethod()](https://www.runoob.com/python/python-func-classmethod.html) | [getattr()](https://www.runoob.com/python/python-func-getattr.html) | [map()](https://www.runoob.com/python/python-func-map.html)  | [repr()](https://www.runoob.com/python/python-func-repr.html) | [xrange()](https://www.runoob.com/python/python-func-xrange.html) |
| [cmp()](https://www.runoob.com/python/func-number-cmp.html)  | [globals()](https://www.runoob.com/python/python-func-globals.html) | [max()](https://www.runoob.com/python/func-number-max.html)  | [reverse()](https://www.runoob.com/python/att-list-reverse.html) | [zip()](https://www.runoob.com/python/python-func-zip.html)  |
| [compile()](https://www.runoob.com/python/python-func-compile.html) | [hasattr()](https://www.runoob.com/python/python-func-hasattr.html) | [memoryview()](https://www.runoob.com/python/python-func-memoryview.html) | [round()](https://www.runoob.com/python/func-number-round.html) | [__import__()](https://www.runoob.com/python/python-func-__import__.html) |
| [complex()](https://www.runoob.com/python/python-func-complex.html) | [hash()](https://www.runoob.com/python/python-func-hash.html) | [min()](https://www.runoob.com/python/func-number-min.html)  | [set()](https://www.runoob.com/python/python-func-set.html)  |                                                              |
| [delattr()](https://www.runoob.com/python/python-func-delattr.html) | [help()](https://www.runoob.com/python/python-func-help.html) | [next()](https://www.runoob.com/python/python-func-next.html) | [setattr()](https://www.runoob.com/python/python-func-setattr.html) |                                                              |
| [dict()](https://www.runoob.com/python/python-func-dict.html) | [hex()](https://www.runoob.com/python/python-func-hex.html)  | object()                                                     | [slice()](https://www.runoob.com/python/python-func-slice.html) |                                                              |
| [dir()](https://www.runoob.com/python/python-func-dir.html)  | [id()](https://www.runoob.com/python/python-func-id.html)    | [oct()](https://www.runoob.com/python/python-func-oct.html)  | [sorted()](https://www.runoob.com/python/python-func-sorted.html) | [exec 内置表达式](https://www.runoob.com/python/python-func-exec.html) |

#### python中的内置模块及常用方法

~~~
time模块、random生成随机数、json序列化处理、logging日志模块、re正则表达式、math数学处理、base64加密、uuid生成唯一值
~~~

#### 系统模块有哪些

~~~
OS文件处理
os.path.abspath #绝对路径
os.path.exists #判断文件是否存在
os.path.getsize #判断文件大小
os.path.join #路径拼接
os.path.split #分隔文件路径

Sys
sys.argv()	在Python脚本传参使用	
sys.exit()	系统退出	
sys.getdefaultencoding()	获取系统默认编码	
sys.getfilesystemencoding()	获取文件编码	
sys.getrecursionlimit()	获取系统默认递归的最大层数	
sys.setrecursionlimit(num)	设置递归的最大层数	
sys.getrefcount()	获取对象的引用计数的数量
~~~

#### 1. 什么是生成器，next和send有什么区别？

~~~
在Python中，一边循环一边计算的机制，称为生成器：generator。使用了 yield 的函数被称为生成器（generator）。生成器仅仅保存了一套生成数值的算法，并且没有让这个算法现在就开始执行，而是什么时候调它，它什么时候开始计算一个新的值，并返回。生成器是一种特殊的迭代器，能够在遍历时暂停和继续执行，使用yield定义的函数不会执行，返回一个生成器对象。迭代时遇到yield会暂停并返回yield后面的值，保存当前的状态，下次迭代从上次暂停的地方继续执行，直到再次遇到yield,优势是内存占用少，节约资源。应用场景是遍历文件或网络数据流、CPU密集型计算、图像处理等。生成器可以逐个读取大文件，并且不必将整个文件加载到内存中，避免了内存消耗和IO操作的额外开销。


当我们创建一个生成器时，第一次调用只能用next()或者 send(None)来启动生成器

实际上next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。

next和send都是调用yield生成值的函数，next是直接调用，send是先覆盖上一个yield返回值后再调用下一个yield生成值。

斐波那契数列实现

import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
生成器实现大文件读取

def myreadlines(f,newline):
    buf=""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline):]
        chunk =f.read(4096*10)
        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk
 
with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)
​

~~~

#### 列表生成式与生成器

~~~
# 列表生成式
list_1 = [x * x for x in range(10)]
# 生成器
# 把列表生成式的中括号[]改成小括号()，就成了生成器
list_generator = (x * x for x in range(10))
~~~

#### 迭代器和可迭代对象

迭代是访问集合元素的一种方式

迭代器是一个可以记住遍历位置的对象。迭代器对象从第一个元素开始访问，直到所有的元素被访问结束。迭代器只能往前不会后退。

可迭代对象是能用for循环遍历的对象

#### iter和next执行流程

~~~
1、先调用iter()，得到可迭代对象的迭代器
2、调用next()，将上一步得到的迭代器 进行取值
3、将上一步取出来的值赋值给变量
4、重复执行，所有数据都获取完毕后，会在下一次调用next的时候产生Stopiteration异常。只不过 for循环中自带了异常处理，当它遇到Stopiteration异常的时候，会自动结束for循环
~~~

#### 2. 什么是迭代器？

~~~
迭代器是一个可以记住遍历位置的对象，因此不会像列表那样一次性全部生成，而是可以等到用的时候才生成，因此节省了大量的内存资源。迭代器对象从集合中的第一个元素开始访问，直到所有的元素被访问完。迭代器有两个方法：iter（）和next（）方法。

迭代器的优点:省内存.它是一种通过延时创建的方式生成一个序列,只有在需要的时候才被创建.

迭代器对象从集合的第一个元素开始访问,直到所有的元素被访问结束,只能往前不能后退

# 自定义一个迭代器,求斐波那契序列
# encoding:utf-8
​
from itertools import islice
from collections import Iterator,Iterable
​
class Fib(object):
    def __init__(self):
        self.prev = 0
        self.curr = 1
​
    def __iter__(self):
        return self
​
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
​
# 迭代器对象
f = Fib()
print(isinstance(f,Iterator)) # true
L = list(islice(f,0,10)) # islice对可迭代对象进行切片
print(L)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
~~~

#### 3. 说一下进程、线程和协程以及他们的区别？

##### 什么是进程（multiprocessing）及合适的场景

```python
进程是操作系统分配资源的基本单位，每个进程都有自己的内存空间和系统资源，进程之间不能共享内存，需要通过 IPC（进程间通信）的方式进行通信。适合CPU密集型场景

并行计算：对于需要进行大量计算的任务，使用多进程可以将计算分配到多个 CPU 核心上，提高计算速度。比如图像处理、数据分析等。

网络编程：Python 进程可以同时处理多个网络请求，实现高并发的网络编程。比如 Web 服务器、消息队列等。

爬虫：Python 进程可以同时处理多个网页的爬取和解析，实现高效的爬虫程序。

任务调度：Python 进程可以用来实现任务调度系统，比如定时任务、异步任务等。

分布式计算：Python 进程可以用来实现分布式计算系统，将任务分配到多个节点上执行，提高计算效率。比如 Hadoop、Spark 等。

总之，Python 进程适合处理需要并行计算、高并发网络编程、爬虫、任务调度和分布式计算等场景。使用多进程可以充分利用多核 CPU 的能力，提高程序的性能和可靠性。

读取文件计算案例：
import multiprocessing
import pandas as pd

# 定义一个简单的任务函数，接受一个文件名并返回分析结果
def task(filename):
    # 读取 CSV 文件并进行简单的数据分析
    data = pd.read_csv(filename)
    result = {
        'filename': filename,
        'rows': len(data),
        'columns': len(data.columns),
        'mean': data.mean(),
        'std': data.std(),
    }
    return result

if __name__ == '__main__':
    # 创建一个进程池，最多同时运行 4 个进程
    pool = multiprocessing.Pool(processes=4)

    # 提交任务到进程池，每个进程会执行 task 函数
    filenames = ['data1.csv', 'data2.csv', 'data3.csv', 'data4.csv']
    results = [pool.apply_async(task, args=(filename,)) for filename in filenames]

    # 等待所有进程执行完毕，并获取结果
    output = [r.get() for r in results]

    # 输出结果
    for result in output:
        print(result)
```

##### 什么是线程（**threading**）

```python
是程序执行的最小单元，一个进程可以有一个或多个线程，同一进程中的多个线程将共享该进程中的全部系统资源，进程和线程都有五种状态，初始态、执行状态、等待（阻塞）状态、就绪状态和终止状态。适合IO密集型案例

多线程爬取案例：
import threading
import requests
from bs4 import BeautifulSoup

# 定义一个简单的爬虫任务函数，接受一个 URL 和一个列表作为参数
def crawl(url, links):
    # 发送 HTTP 请求并解析响应
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 解析页面中的链接并添加到列表中
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)

if __name__ == '__main__':
    # 创建一个空的链接列表
    links = []

    # 创建 4 个线程，每个线程爬取一个网页并解析其中的链接
    urls = ['http://example.com', 'http://example.net', 'http://example.org', 'http://example.edu']
    threads = [threading.Thread(target=crawl, args=(url, links)) for url in urls]

    # 启动所有线程
    for thread in threads:
        thread.start()

    # 等待所有线程执行完毕
    for thread in threads:
        thread.join()

    # 输出结果
    print(links)
```

##### 进程 VS 线程

```
进程是资源的分配和调度的独立单元。进程拥有完整的虚拟地址空间，当发生进程切换时，不同的进程拥有不同的虚拟地址空间。而同一进程的多个线程是可以共享同一地址空间

线程是CPU调度的基本单元，一个进程包含若干线程。

线程比进程小，基本上不拥有系统资源。线程的创建和销毁所需要的时间比进程小很多

由于线程之间能够共享地址空间，因此，需要考虑同步和互斥操作

一个线程的意外终止会影像整个进程的正常运行，但是一个进程的意外终止不会影像其他的进程的运行。因此，多进程程序安全性更高。

多进程程序安全性高，进程切换开销大，效率低；多线程程序维护成本高，线程切换开销小，效率高
```

##### 什么是协程（asyncio）

```python
协程（Coroutine，又称微线程）是一种比线程更加轻量级的存在，协程不是被操作系统内核所管理，而完全是由程序所控制。

协程可以比作子程序，但执行过程中，子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。协程之间的切换不需要涉及任何系统调用或任何阻塞调用

协程只在一个线程中执行，是子程序之间的切换，发生在用户态上。而且，线程的阻塞状态是由操作系统内核来完成，发生在内核态上，因此协程相比线程节省线程创建和切换的开销

协程中不存在同时写变量冲突，因此，也就不需要用来守卫关键区块的同步性原语，比如互斥锁、信号量等，并且不需要来自操作系统的支持。

协程适用于IO阻塞且需要大量并发的场景，当发生IO阻塞，由协程的调度器进行调度，通过将数据流yield掉，并且记录当前栈上的数据，阻塞完后立刻再通过线程恢复栈，并把阻塞的结果放到这个线程上去运行。

Python 协程实现简单的生产者-消费者模型的案例，它使用了 asyncio 模块来创建协程，生产者协程会生成随机数并将它们放入一个队列中，消费者协程会从队列中取出随机数并打印出来。

import asyncio
import random

# 定义一个生产者协程，接受一个队列作为参数
async def producer(queue):
    while True:
        # 生成一个随机数并放入队列中
        value = random.randint(0, 100)
        await queue.put(value)
        print(f'Produced {value}')
        # 等待一段时间
        await asyncio.sleep(1)

# 定义一个消费者协程，接受一个队列作为参数
async def consumer(queue):
    while True:
        # 从队列中取出一个随机数并打印出来
        value = await queue.get()
        print(f'Consumed {value}')
        # 等待一段时间
        await asyncio.sleep(1)

if __name__ == '__main__':
    # 创建一个事件循环
    loop = asyncio.get_event_loop()

    # 创建一个队列并启动生产者和消费者协程
    queue = asyncio.Queue()
    loop.create_task(producer(queue))
    loop.create_task(consumer(queue))

    # 运行事件循环
    loop.run_forever()
在这个例子中，我们首先定义了一个生产者协程和一个消费者协程，它们都接受一个队列作为参数。生产者协程会不断生成随机数并放入队列中，消费者协程会不断从队列中取出随机数并打印出来。然后我们使用 asyncio.Queue 创建了一个队列，并使用 loop.create_task 启动了生产者和消费者协程。最后，我们使用 loop.run_forever 运行事件循环，使协程能够不断地运行。

需要注意的是，协程是一种轻量级的线程，可以在单线程中实现并发。在协程编程中，我们可以使用 async/await 关键字来定义异步函数，并使用 asyncio 模块来创建协程和事件循环。同时，由于协程共享进程内存，可能会存在协程安全问题，因此在协程编程中应该注意避免竞争条件和死锁等问题。
```

##### 常见的应用场景

```
CPU密集型:程序需要占用CPU进行大量的运算和数据处理；

I/O密集型:程序中需要频繁的进行I/O操作；例如网络中socket数据传输和读取等；

CPU密集+I/O密集：以上两种的结合

CPU密集型 多进程的性能 > 多线程的性能。

针对I/O密集型的程序，协程的执行效率更高，因为它是程序自身所控制的，这样将节省线程创建和切换所带来的开销。
```

#### 4. 什么是GIL锁？

~~~
GIL来源于Python设计之初的考虑，为了数据安全(由于内存管理机制中采用引用计数)所做的决定。某个线程想要执行，必须先拿到 GIL。因此，可以把 GIL 看作是“通行证”,并且在一个 Python进程中，GIL 只有一个,拿不到通行证的线程,就不允许进入 CPU 执行。
​
Cpython解释器在内存管理中采用引用计数，当对象的引用次数为0时，会将对象当作垃圾进行回收。设想这样一种场景：
​
一个进程中含有两个线程，分别为线程0和线程1，两个线程全都引用对象a。当两个线程同时对a发生引用（并未修改，不需要使用同步性原语），就会发生同时修改对象a的引用计数器，造成计数器引用少于实质性的引用，当进行垃圾回收时，造成错误异常。因此，需要一把全局锁（即为GIL）来保证对象引用计数的正确性和安全性。

~~~

#### 5. 写出10个linux常用命令？

~~~
1、top：查看内存/显示系统当前进程信息

2、df -h：查看磁盘储存状况 (如果出现磁盘报警和实际有出入，可能因为文件操作符或者文件句柄未释放导致)

3、iotop：查看IO读写（yum install iotop安装）

4、iotop -o：直接查看比较高的磁盘读写程序

5、netstat -tunlp | grep 端口号：查看端口号占用情况（1）

6、lsof -i:端口号：查看端口号占用情况（2）

7、uptime：查看报告系统运行时长及平均负载

8、ps aux：查看进程

9、 free 查看内存交换区



ps：查看进程，ps aux 或者 ps -elf，常和管道符一起使用，查看某个进程或者它的数量；
netstat：查看端口，netstat -lnp用于打印当前系统启动了哪些端口，netstat -an用于打印网络连接状况；
top 以全屏交互式的界面显示进程排名，及时跟踪包括CPU、内存等系统资源占用情况，默认情况下每三秒刷新一次，其作用基本类似于Windows系统中的任务管理器
chmod 改变文件的权限  
chmod -R xyz  文件或文件夹名 比如 755表示该文件所有者对该文件具有读、写、执行权限，该文件所有者所在组用户及其他用户对该文件具有读和执行权限。

date 查看当前时间
shutdown 关机

cd 变换目录
pwd 显示当前所在目录
mkdir 建立新目录
rm 目录或文件名
rm -rf  -r或-R：递归处理，将指定目录下的所有文件与子目录一并处理；-f：强制删除文件或目录；
ls 档案与目录的显示
ls -l
cp 复制档案或目录
mv 移动档案与目录
cat 由第一行开始显示档案内容
tac 从最后一行开始显示
more 一页一页的显示档案内容
less 与 more 类似，但是比 more 更好的是，他可以往前翻页
touch 修改档案时间或新建档案
which 寻找【执行挡】 which 文件名  which -a 文件名目录和文件都显示
whereis 文件名 寻找特定档案
find 寻找特定档案
gzip，zcat 压缩文件和读取压缩文件
tar -zpcv -f 文件名 压缩文件和读取压缩文件
ps aux 查看进程

压缩命令：命令格式：tar  -zcvf   压缩文件名.tar.gz   被压缩文件名

解压缩命令：命令格式：tar  -zxvf   压缩文件名.tar.gz


1、打开文件，或者是新建文件
统一命令为：vim file_name
​
2、移动光标：
a、以字符为单位移动
在命令模式中使用 h、j、k、l 这 4 个字符控制方向，分别表示向左、向下、向上、向左。
b、以单词为单位移动
w：移动光标到下一个单词的单词首
b：移动光标到上一个单词的单词首
e：移动光标到下一个单词的单词尾
c、移动到行尾或者行首
​
3、插入
常用的插入命令：
i：在当前光标所在位置插入随后输入的文本，光标后的文本相应向右移动
I：在光标所在行的行首插入随后输入的文本，行首是该行的第一个非空白字符，相当于光标移动到行首执行i命令
a：在当前光标所在位置之后插入随后输入的文本
A：在光标所在行的行尾插入随后输入的文本，相当于光标移动到行尾再执行a命令
o：在光标所在行的下面插入新的一行。光标停在空行首，等待输入文本
O：在光标所在行的上面插入新的一行。光标停在空行的行首，等待输入文本
​
4、编辑
査找指定字符串
首先在命令模式下输入：/char #char为需要查找的字符，在查找的过程中还以使用$^等进行匹配
然后enter键就可以了，然后使用n，N进行下一个或者上一个查找
​
5、替换字符
​
r 替换当前光标的单个字符
R 从当前光标开始替换，esc退出
替换范围内的字符串：:替换起始处，替换结束处s/源字符串/替换的字符串/g。
替换整篇文档的字符串：:%s/源字符串/替换的字符串/g（如果不加g，则只替换每行第一个找到的字符串）。
​
6、删除，复制，粘贴
x ：删除当前光标字符
dd： 删除当前光标行
还可以使用命令：:1,$d #表示从第一行到最后一行删除，
ndd ，表示删除当前光标接下来的n行， 例如5dd
dG ： 表示删除光标到最后一行
yy：为复制
p：为粘贴
u：为撤销上一步的操作
~~~

#### linux怎么启动定时任务

```
1.首先安装cron服务
sudo apt-get install cron
2.启动与关闭cron服务
service cron start //启动服务
service cron stop //关闭服务
service cron restart //重启服务
service cron reload //重新载入配置
service cron status //查看crontab服务状态
```

#### linux怎么查看端口

```
netstat - atulnp会显示所有端口和所有对应的程序，用grep管道可以过滤出想要的字段

    -a ：all，表示列出所有的连接，服务监听，Socket资料
    -t ：tcp，列出tcp协议的服务
    -u ：udp，列出udp协议的服务
    -n ：port number， 用端口号来显示
    -l ：listening，列出当前监听服务
    -p ：program，列出服务程序的PID
```

#### linux查看进程

```
  ps -l  查看登录有关的进程信息；
  ps -aux  查询[内存](https://so.csdn.net/so/search?q=内存&spm=1001.2101.3001.7020)中进程信息；
  ps -aux | [grep](https://so.csdn.net/so/search?q=grep&spm=1001.2101.3001.7020) ***  查询***进程的详细信息；
  top  查看内存中进程的动态信息；
  kill  pid  杀死进程。
  kill -9强制立即执行

终止linux进程

kill[参数][进程号]杀死进程
```

#### 查看磁盘占用率

~~~
1、df命令

　　df命令全称为disk-free，用于查看Linux系统中的可用和已经使用的磁盘空间，一般有以下几个常用选项：

　　df -h：以可读的格式显示磁盘空间(否则默认显示单位是字节，不直观);

　　df -a：包含全部的文件系统；

　　df -T：显示磁盘使用情况以及每个块的文件系统类型(如xfs、ext2、ext3、btrfs等);

　　df -i：显示已使用和空闲的inode。

　　2、du命令

　　du命令全称为disk useage的缩写，以默认千字节大小显示文件、文件夹等磁盘使用情况，一般有以下几个常用选项：

　　du -h：以可读的格式显示所有目录和子目录的磁盘使用情况；

　　du -a：显示所有文件的磁盘使用情况；

　　du -s：仅显示总计，只列出最后加总的值；

　　3、ls -al命令

　　ls命令大家再熟悉不过了吧，使用ls -al命令可以列出特定目录的全部内容及其大小。

　　4、stat命令

　　stat命令后面可以直接跟上文件或目录，用于显示文件/目录或文件系统的大小和其他统计信息。

　　5、fdisk -l命令

　　fdisk -l：可以显示磁盘大小以及磁盘分区信息。
~~~



#### 6. 写一个线程安全的单例模式？

~~~
class Myredis:
  ....
  
  
r = Myredis()
  
  from utils.myredis imsaaport r
  r = r.
  r.
~~~



~~~
import time
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
    	  if cls._instance:
    	     return cls._instance
        with cls._lock:
                cls._instance = super().__new__(cls)
                 return cls._instance
       

if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(id(obj1))
    print(id(obj2))
~~~

#### 7.写一个工厂模式

1.1新建基类抽象类login.py

~~~python
import abc
class Login(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_url(self):
        pass 

    @abc.abstractclassmethod
    def call_back(self):
        pass 
    
~~~

1.2新建三方登录类weibo.py

~~~python
from views.tlogin.login import Login
class Weibo(Login):
    def __init__(self) -> None:
        self.client='23423'
        self.redirect_uri = 'http://'

    def get_url(self):
        return 'weibo url'

    def call_back(self):
        return 'ok'
~~~

1.3新建工厂类loginFactory.py

~~~
from views.tlogin.weibo import Weibo
from views.tlogin.ding import Ding

class LoginFactory:
    def get_sclass(self,type):
        if type == "weibo":
            return Weibo()
        else:
            return Ding()
~~~

1.4调用

~~~
@indexblue.route('/three_login')
def three_login():
    type = request.args.get("type")
    factory =LoginFactory()
    cls = factory.get_sclass(type)
    return cls.get_url()
~~~

     ~~~
rbac
位运算

用户表
角色表
id  name  pomistion
1  ...     11

资源表
id name      pomistion
1  添加用户     1 
2   顶起要      2
               4 
               8
               16
               32
               
               vue  ids = 1,2,3
               
              list =  ids.split(",")
              t = 0
              for i in list:
                   t = t | i 
                   
               update roles set pomistion = t where id =1
                
     ~~~

#### 说一下python中的继承？

~~~
当我们需要构建一个类，而这个类有部分属性或方法在其他类里面已经存在了，那么我们就可以从其它类里面继承我们所要的功能，被继承的类叫父类，继承的类叫子类。python支持单继承和多继承，多继承中最为核心的问题是如何寻找父类，如果父类之间的方法属性不冲突，那么继承的时候就可以将父类的属性和方法全部继承，如果继承的多个父类方法属性正好名字一样，则会优先选择最先被继承的方法，即从左到右依次检索。python3中，类被创建时会自动创建方法解析顺序mro，object是所有类的父类，运行mro()方法可以查看继承顺序，Python中的super()方法设计目的是用来解决多重继承时父类的查找问题，super()的好处就是可以避免直接使用父类的名字.主要用于多重继承。
~~~

#### 8.说一个python中的反射？

~~~
就是把一个对象类型拆解。可以使用字符串的形式去访问和修改对象。
反射有四个方法：hasattr、getattr、setattr、delattr

#动态导入模块
比如有一个comms模块，里面有三个方法
def login():
  print("这是一个登陆页面！")

def logout():
  print("这是一个退出页面！")

def home():
  print("这是网站主页面！")
  
#我们想通过用户输入的字符串调用方法
import commons

def run():
  inp = input("请输入您想访问页面的url： ").strip()
  if inp == "login":
    commons.login()
  elif inp == "logout":
    commons.logout()
  elif inp == "home":
    commons.home()
  else:
    print("404")

if __name__ == '__main__':
  run()
  
  
#通过反射实现
def run():
  inp = input("请输入您想访问页面的url： ").strip()
  modules, func = inp.split("/")
  obj = __import__("lib." + modules)   #注意字符串的拼接
  if hasattr(obj, func):
    func = getattr(obj, func)
    func()
  else:
    print("404")
 
if __name__ == '__main__':
  run()
  
  
 class Person(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("%s正在交谈"%self.name)

p = Person('abc')
inp = input("请输入您想访问页面的url： ").strip()

def abc(self):
        print("%s正在交333333谈"%self.name)

if hasattr(p,inp):
    t = getattr(p,inp)
    t()
else:
    setattr(p,'findall',abc)   # 将abc函数添加到对象中p中，并命名为talk
    p.findall(p) 
~~~

#### range和xrange的区别

~~~
1.range 是生成一个列表
2.xrange用法与range完全相同,不同的是生成的不是一个list对象,而是一个生成器
3.在生成很大的数字序列时候,用xrange会比range性能优很多,因为不需要一上来就开辟一块很大的内存空间
~~~

#### 9.python中的自省

~~~
Python中比较常见的自省（introspection）机制(函数用法)有： dir()，type(), hasattr(), isinstance()，通过这些函数，我们能够在程序运行时得知对象的类型，判断对象是否存在某个属性，访问对象的属性。
~~~

#### 10.python如何做内存管理的

~~~
Python垃圾回收主要以引用计数为主，标记-清除、分代回收为辅。

引用计数法的原理是每个对象维护一个ob_ref，用来记录当前对象被引用的次数，也就是来追踪到底有多少引用指向了这个对象，当对象被创建，被引用，作为参数传递，或者作为一个元素存在容器中的时候，该对象的引用计数器+1，当指向该对象的内存的引用计数器为0的时候，该内存将会被Python虚拟机销毁，缺点是维护引用计数消耗资源，无法解决循环引用的问题。为了解决这个问题引入了标记清除，它是一种基于追踪回收技术实现的垃圾回收算法。它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，第二阶段是把那些没有标记的对象『非活动对象』进行回收。那么GC又是如何判断哪些是活动对象哪些是非活动对象的呢？对象之间通过引用（指针）连在一起，构成一个有向图，对象构成这个有向图的节点，而引用关系构成这个有向图的边。从根对象出发，沿着有向边遍历对象，可达的对象标记为活动对象，不可达的对象就是要被清除的非活动对象。分代回收是一种以空间换时间的操作方式，Python将内存根据对象的存活时间划分为不同的集合，每个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、老年代（第2代），他们对应的是3个链表，它们的垃圾收集频率与对象的存活时间的增大而减小。新创建的对象都会分配在年轻代，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到中年代去，依此类推，老年代中的对象是存活时间最久的对象，甚至是存活于整个系统的生命周期内。同时，分代回收是建立在标记清除技术基础之上。分代回收同样作为Python的辅助垃圾收集技术处理那些容器对象.

~~~

#### 如何判断一个Object被收回了

~~~
使用sys.getrefcount()来获取对象的引用计数，引用计数为0表示该对象已经被收回了
~~~



#### 11.lambda表达式的作用

~~~
lambda 定义了一个匿名函数,在调用时被求值。lambda 并不会带来程序运行效率的提高，只会使代码更简洁。
g=lambda x:x*2
print(g(1))
~~~

#### 12. 四大高阶函数

~~~python
在 Python 中，高阶函数是指可以接受函数作为参数或返回函数作为结果的函数。四大高阶函数是指 map、filter、reduce 和 sorted，它们都是 Python 内置的高阶函数，可以方便地进行列表、字典、集合等数据结构的处理。

map 函数：对列表中的每个元素应用一个函数，并返回一个新的列表。
例如，将一个列表中的每个元素进行平方并返回一个新的列表：

lst = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, lst))
print(squares)  # [1, 4, 9, 16, 25]
filter 函数：对列表中的每个元素应用一个函数，并返回一个由符合条件的元素组成的新列表。
例如，过滤出一个列表中所有的偶数：

lst = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, lst))
print(evens)  # [2, 4]
reduce 函数：对列表中的元素应用一个函数，并返回一个单一的值。
例如，计算一个列表中所有元素的乘积：

from functools import reduce

lst = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, lst)
print(product)  # 120
sorted 函数：对列表中的元素进行排序并返回一个新的列表。
例如，对一个列表中的元素进行升序排序：

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_lst = sorted(lst)
print(sorted_lst)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
以上就是四大高阶函数的介绍，它们都是 Python 中非常常用的函数，可以大大简化代码的编写。
~~~

#### 13.with上下文管理

~~~
with是一种上下文管理协议，目的在于从流程图中把 try,except 和finally 关键字和资源分配释放相关代码统统去掉，简化try….except….finlally的处理流程。with通过enter方法初始化，然后在exit中做善后以及处理异常。所以使用with处理的对象必须有enter()和exit()这两个方法。打开文件时一般建议使用with语句，因为这样能够确保打开的文件描述符在程序执行离开时with语句的上下文后自动关闭. 当执行流程进入with语句上下文时，python会调用__enter__获取资源，离开with上下文时，python会调用__exit__释放资源。
~~~

#### 14.面向对象的三大特性？

~~~
面向对象的三大特性是指：封装、继承和多态。

封装
隐藏对象的属性和实现细节，只对外提供必要的方法。相当于将"细节封装起来",只对外暴露“相关调用方法”。通过私有属性、私有方法的方式实现封装。比如我们项目中pymsql,redis,jwt等封装，还有短信接口、支付接口等。

继承
继承可以让子类具有父类的特性，提高了代码的重用性。

多态(鸭子类型)
不同的对象，调用相同的方法，产生不同的执行结果，增加代码的灵活度。多态的存在有两个必要条件：继承、方法重写。

class AliPay:
    def order_pay(self):
        print('支付宝支付')

class Weixin:
    def order_pay(self):
        print('微信支付')


def order_pay(pclass):
    pclass.order_pay()

a = AliPay()
w = Weixin()

order_pay(a)
order_pay(w)
~~~

#### 15.新式类与旧式（经典）类

~~~
新式类与旧式（经典）类
　　object是python为所有对象提供的基类，提供了一些内置属性和方法，可以使用dir函数查看。

新式类：以 object 为基类的类，推荐使用
经典类：不以 object 为基类的类，不推荐使用

在 Python 3.x 中定义类时，如果没有指定父类，会 默认使用 object 作为该类的 基类 —— Python 3.x 中定义的类都是 新式类

在 Python 2.x 中定义类时，如果没有指定父类，则不会以 object 作为 基类
~~~

#### 15.Python实例方法、类方法、静态方法的区别与作用

~~~
实例方法
    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    调用：只能由实例对象调用。

类方法
    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
    调用：实例对象和类对象都可以调用。

静态方法
    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    调用：实例对象和类对象都可以调用。

~~~

#### 16.简述面向对象中__new__和__init__区别？

~~~
__init__ 方法通常用在初始化一个类实例的时候，__new__方法用于创建对象并返回对象，当返回对象时会自动调用__init__方法进行初始化。所以是先执行new后执行init。__new__方法是静态方法，而__init__是实例方法。
~~~

#### 18.http和https有什么区别？

~~~
 1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。

 2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。

 3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

　4、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
~~~

18.网络七层协议

http在应用层，ip协议在网络层，tcp在传输层。

<img src='images/1.png'>

#### 18.tcp/udp的区别是什么

~~~
1、TCP面向连接（如打电话要先拨号建立连接）;UDP是无连接的，即发送数据之前不需要建立连接
2、TCP提供可靠的服务。也就是说，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达;UDP尽最大努力交付，即不保   证可靠交付
3、TCP面向字节流，实际上是TCP把数据看成一连串无结构的字节流;UDP是面向报文的
  UDP没有拥塞控制，因此网络出现拥塞不会使源主机的发送速率降低（对实时应用很有用，如IP电话，实时视频会议等）
4、每一条TCP连接只能是点到点的;UDP支持一对一，一对多，多对一和多对多的交互通信
5、TCP首部开销20字节;UDP的首部开销小，只有8个字节
6、TCP的逻辑通信信道是全双工的可靠信道，UDP则是不可靠信道
~~~

#### 19.说一下三握四挥

~~~
第一次握手
　　A的TCP进程创建TCB（传输控制块），然后向B发出连接请求报文段。段首部中的 同步位SYN=1，同时选择一个初始序列号seq=x；（SYN报文段不能携带数据，但需要消耗一个序列号）这时客户端A进入到 SYN-SENT（同步已发送）状态。

第二次握手
　　B收到连接请求报文段，如果同意建立连接，则向A发送确认。在确认报文段中 同步位SYN=1、确认位ACK=1、确认号ack=x+1（对接收的序列号seq=x的报文段进行确认，并期望接收的下一个报文段的序号seq=x+1），同时也为自己选择一个初始序列号seq=y，这时服务器B进入 SYN-RCVID 状态。

　　注：该报文段是ACK报文段的同时也是SYN报文段，所以该报文段也不能携带数据。

第三次握手
　　A收到B的确认以后，再向B发出确认。确认报文 ACK=1、确认号ack=y+1（对接收的序列号seq=y的报文段进行确认，并期望接收的下一个报文段的序号seq=y+1）。这时A进入到 ESTAB-LISHED 状态。当B接收到A的确认后，也进入 ESTAB-LISHED 状态。连接建立完成

　　注：ACK报文段可以携带数据，但如果不携带数据则不消耗序列号，在这种情况下，下一个报文段的序号不变，seq仍是x+1。
　　
　　
　　第一次挥手：A先发送连接释放报文段，段首部的终止控制位FIN=1，序号seq=u（等于A前面发送数据的最后一个序号加1）；然后A进入 FIN-WAIT-1（终止等待1）状态，等待B的确认。A
　　注：FIN报文段即使不携带数据也要消耗一个序列。

第二次挥手：B收到A的连接释放报文段后，立刻发出确认报文段，确认号ack=u+1，序号seq=v（等于B前面发送数据的最后一个序号加1）；然后B进入CLOSE-WAIT（关闭等待）状态。
　　注：TCP服务器这时会通知高层应用进程，从A到B这个方向的连接就断开了，这时TCP连接处于半关闭（half-close）状态；但B到A这个方向的连接并没有断，B任然可以向A发送数据。

第三次挥手：A收到B的确认报文段后进入到 FIN-WAIT-2（终止等待2）状态，继续等待B发出连接释放报文段；若B已经没有数据要发送，B就会向A发送连接释放报文段，段首部的终止控制位 FIN=1，序号seq=w（半关闭状态可能又发送了一些数据），确认号ack=u+1，这时B进入LAST-ACK（最后确认）状态，等待A的确认。
　　特别注意：确认号ack没有变，仍然为上次发送过的确认号u+1。

第四次挥手：A收到B的连接释放报文段并发出确认，确认段中 确认位ACK=1，确认号ack=w+1，序号seq=u+1；然后A进入到TIME-WAIT（时间等待）状态。当B再接收到该确认段后，B就进入CLOSED状态。
　　注：处于TIME-WAIT状态的A必须等待2MSL时间后，才会进入CLOSED状态。MSL（Maximum Segment Lifetime）最长报文段寿命，RFC 793 建议设为两分钟，对于现在的网络，MSL=2分钟可能太长了一些，我们可根据具体情况使用更小的MSL值。
~~~

#### 2.为什么建立连接三次，断开连接四次？

~~~
因为建立连接时，服务器的确认 ACK 和请求同步 SYN 可以放在一个报文里，而断开连接时，服务器可能还有数据要传送，因此，必须先发一个客户端断开连接请求的确认 ACK，以免客户端超时重传，待服务器的数据传送完毕后，再发送一个请求断开连接的报文段。
断开时次数比连接多一次，是因为连接过程，通信只需要处理「连接」，而断开过程，通信需要处理「数据+连接」。
~~~

#### 21.http是什么组成的？

~~~
HTTP 请求的组成
         状态行、请求头、消息主体三部分组成。
HTTP 响应的组成
         状态行、响应头、响应正文
~~~

#### 21.git常用命令有哪些？

~~~
查看所有分支   git branch  -a

创建分支  git  branch 分支名

切换  git checkout 分支名  git  checkout master

如果是多人开发的话 需要把远程master上的代码pull下来：git pull origin master

合并某分支到当前分支  git merge  分支名

删除分支  git branch -d  分支名

项目拉取  git pull

将工作目录添加到缓存区  git add ./*

将缓存区内容添加到本地仓库  git commit -m 'message'

推送 git push origin  分支名


~~~

#### 22.git如何解决冲突

~~~
首先通过命令git fetch获取远程仓库最新的修改，然后执行命令git merge将本地的操作结果（实际上就是一个commit）与远程仓库的修改（远程仓库最新的commit）进行合并，如果在合并的过程没有发生冲突，那么Git会生成一个新的commit，并自动提交。但是，合并并非总是成功的，因为合并的不同提交可能是同时修改了同一个文件相同区域的内容，这样就会导致冲突。冲突发生后合并操作会终止，在本地解决冲突后，除非放弃此次合并，需要更新暂存区，再提交，最终完成合并过程。


~~~

#### 23.常用的状态码

~~~
1-199：信息提示。请求已被接受，需要进一步处理。

200-299：成功。请求已被接受，处理。

300-399：重定向。最常见的重定向就是304，本地已缓存返回内容，所以浏览器直接从本地取内容而不是从服务器重新拉去。

400-499：客户端错误。最常见的是404，服务器没有找到内容，说明你请求的url不对，服务器上并没有对应的内容。

500-599：服务器错误。代表服务器在处理请求过程中有错误或异常状态发生。

常见的请求状态码：

200：请求已成功，请求所需要的请求头和相应数据随此请求返回。202：服务器已接受请求，但是尚未处理。301：永久移动

302：临时移动

304：get请求，且该请求已被允许，但是所请求的内容和上次请求的内容并没有发生改变，服务器返回该状态码，浏览器抓取已上次请求的已缓存的文件。

400：由于包含语法错误，该请求不能被服务器理解。

401：当前请求需要用户认证，该响应必须包含一个适用于被请求资源的WWW-Authenticate信息头用以询问用户信息。

403：服务器已经理解请求，但是拒绝了它。

404：请求失败，请求所需要的资源在服务器上并为被发现。

500：服务器遇到了一个未曾预料的情况。

503：由于临时的服务器维护或过载，服务器当前无法处理请求。
~~~

#### 24.**kwargs跟**args区别

~~~
*args 的返回值是一个元组，准确的说是将传入的参数中不确定的参数以元组的形式保存下来
**kwargs的返回值是一个字典，即，传参时必须以确定的键值对来传入，及以键值对保存下来
同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
~~~

#### 25.python中的锁

GIL全局解释器锁

~~~
在同一个进程中只要有一个线程获取了全局解释器（cpu）的使用权限，其他的线程就必须等待该线程的全局解释器（cpu）使用完才能使用全局解释器（cpu）,多个线程之间不会相互影响在同一个进程下也只有一个线程使用cpu

全局解释器锁的好处

　　　　　　避免了大量的加锁解锁的好处

　　　　　　使数据更加安全，解决多线程间的数据完整性和状态同步

全局解释器的缺点
　　　　　　多核处理器退化成单核处理器，只能并发不能并行
　　　　　　
~~~

死锁

~~~
两个或两个以上的线程或进程在执行程序的过程中，因争夺资源而相互等待的一个现象，就会造成死锁。在多线程程序中，死锁问题很大一部分是由于线程同时获取多个锁造成的。

例如：一个线程获取了第一个锁，然后在获取第二个锁的 时候发生阻塞，那么这个线程就可能阻塞其他线程的执行，从而导致整个程序假死。

解决死锁问题的一种方案是为程序中的每一个锁分配一个唯一的id，然后只允许按照升序规则来使用多个锁（银行家算法）。还有添加超时时间。
~~~

#### 26.什么是信号量

~~~
在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁
？
　　　　同进程的一样，semaphore管理一个内置的计数器，每当调用acquire()时内置函数-1，每当调用release()时内置函数+1。
　　　计数器不能为0，当计数器为0时acquire（）将阻塞线程，直到其他线程调用release（）。
~~~

### mysql相关

#### 1. mysql常用的存储引擎有哪些？

```
(1) MyISAM:

   它不支持事务，也不支持外键，尤其是访问速度快，对事务完整性没有要求或者以SELECT、INSERT为主的应用基本都可以使用这个引擎来创建表
   
(2) InnoDB:

　 InnoDB存储引擎提供了具有提交、回滚和崩溃恢复能力的事务安全。但是对比MyISAM的存储引擎，InnoDB写的处理效率差一些并且会占用更多的磁盘空间以保留数据和索引。
```

#### 2. mysql索引存储方式有哪些？

什么是索引？

```
在mysql中,索引是一种特殊的数据库结构,由数据表中的一列或多列组合而成,可以用来快速查询数据表中有某一特定值的记录。通过索引,查询数据时不用读完记录的所有信息,而只是查询索引列即可，索引是帮助Mysql高效获取数据且以排好序的数据结构，直观的说，索引就类似书的目录页，没有目录（即索引）我们就要一页一页的找，有了目录（索引）我们就可以按照目录中标记的页数去相应的页数去查找
```

为什么要使用索引

<img src="images/image-20230221073520660.png">

<img src="images/image-20230221073817072.png">

索引的数据结构

1.每个节点最多有两个子树，所以二叉树不存在度大于2的节点（结点的度：结点拥有的 子树的数目。），可以没有子树或者一个子树。
2.左子树和右子树有顺序，次序不能任意颠倒。
3、二叉树支持动态的插⼊和查找，保证操作在O(height)时间

<img src="images/image-20230221074636847.png">

**红黑树**

红黑树：当单边的节点大于3时候，就会自动调整，这样可以解决二叉树的弊端；红黑树也叫平衡二叉树；

<img src="images/image-20230221074909410.png">

**B-Tree 存储的**

B-Tree 的存储，数字为key，data为对应的数据。若data中的数据过大，则一个节点能放的数据量越小，这样就会造成树的高度比较大了（比红黑树高度小点）

<img src="images/image-20230221075542867.png">

B+tree存储

非叶子节点不存储data，只存储索引（冗余），可以放更多索引；
叶子节点包含所有索引字段，即所有的data元素存储在叶子节点上；
叶子节点使用指针连接，提高区间访问的性能；
从左到右一次递增;

<img src="images/image-20230221075650092.png">



#### 3.为什么MYSQL要用B+ 树而不用B树

```
优化点1：  B-Tree的所有节点都存储了 data 元素， B+Tree的非叶子节点不存储 data元素，则 B+Tree 的一个非叶子节点可以存储更多的索引；

 优化点2： B+Tree在叶子节点之间增加了指针连接；对 select * from t where col2 > 20 的范围查找有很好的支持；

MySQL 对 B+Tree 做了优化，叶子节点使用的是双向指针；
```

#### 4.mysql索引类型有哪些？

```
联合全索引最左原则

(1) 普通索引
普通索引是 MySQL 中最基本的索引类型，它没有任何限制，唯一任务就是加快系统对数据的访问速度。
普通索引允许在定义索引的列中插入重复值和空值。

创建普通索引时，通常使用的关键字是 INDEX 或 KEY。
例 1
下面在 tb_student 表中的 id 字段上建立名为 index_id 的索引。
CREATE INDEX index_id ON tb_student(id);

(2) 唯一索引
唯一索引与普通索引类似，不同的是创建唯一性索引的目的不是为了提高访问速度，而是为了避免数据出现重复。
唯一索引列的值必须唯一，允许有空值。如果是组合索引，则列值的组合必须唯一。

创建唯一索引通常使用 UNIQUE 关键字。
例 2
下面在 tb_student 表中的 id 字段上建立名为 index_id 的索引，SQL 语句如下：
CREATE UNIQUE INDEX index_id ON tb_student(id);

(3) 主键索引
顾名思义，主键索引就是专门为主键字段创建的索引，也属于索引的一种。
主键索引是一种特殊的唯一索引，不允许值重复或者值为空。
创建主键索引通常使用 PRIMARY KEY 关键字。不能使用 CREATE INDEX 语句创建主键索引。

(4) 全文索引
全文索引主要用来查找文本中的关键字，只能在 CHAR、VARCHAR 或 TEXT 类型的列上创建。在 MySQL 中只有 MyISAM 存储引擎支持全文索引。
全文索引允许在索引列中插入重复值和空值。
不过对于大容量的数据表，生成全文索引非常消耗时间和硬盘空间。

创建全文索引使用 FULLTEXT 关键字。
例 4
在 tb_student 表中的 info 字段上建立名为 index_info 的全文索引，SQL 语句如下：
CREATE FULLTEXT INDEX index_info ON tb_student(info);

其中，index_info 的存储引擎必须是 MyISAM，info 字段必须是 CHAR、VARCHAR 和 TEXT 等类型。
```

#### 5.聚集索引和非聚集索引

~~~
1)简单概括
聚集索引：就是以主键创建的索引。
非聚集索引：就是以非主键创建的索引(也叫做二级索引)。

2)详细概括

聚集索引
聚集索引表记录的排列顺序和索引的排列顺序一致，所以查询效率快，因为只要找到第一个索引值记录，其余的连续性的记录在物理表中也会连续存放，一起就可以查询到。

缺点：新增比较慢，因为为了保证表中记录的物理顺序和索引顺序一致，在记录插入的时候，会对数据页重新排序。

非聚集索引
索引的逻辑顺序与磁盘上行的物理存储顺序不同，非聚集索引在叶子节点存储的是主键和索引列，当我们使用非聚集索引查询数据时，需要拿到叶子上的主键再去表中查到想要查找的数据。这个过程就是我们所说的回表。

3)聚集索引和非聚集索引的区别

聚集索引在叶子节点存储的是表中的数据。
非聚集索引在叶子节点存储的是主键和索引列。
~~~

#### 5.explain

```
sql性能查询的工具
explain select * from user where namae='zs' and sex=1;

expain出来的信息有10列，分别是id、select_type、table、type、possible_keys、key、key_len、ref、rows、Extra

id:选择标识符
select_type:表示查询的类型。
table:输出结果集的表
partitions:匹配的分区
type:表示表的连接类型
possible_keys:表示查询时，可能使用的索引
key:表示实际使用的索引
key_len:索引字段的长度
ref:列与索引的比较
rows:扫描出的行数(估算的行数)
filtered:按表条件过滤的行百分比
Extra:执行情况的描述和说明

type:对表访问方式，表示MySQL在表中找到所需行的方式，又称“访问类型”。
ALL、index、range、 ref、eq_ref、const、system、NULL（从左到右，性能从差到好）

ALL：Full Table Scan， MySQL将遍历全表以找到匹配的行

index: Full Index Scan，index与ALL区别为index类型只遍历索引树

range:只检索给定范围的行，使用一个索引来选择行

ref: 表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值

const、system: 当MySQL对查询某部分进行优化，并转换为一个常量时，使用这些类型访问。如将主键置于where列表中，MySQL就能将该查询转换为一个常量，system是const类型的特例，当查询的表只有一行的情况下，使用system

NULL: MySQL在优化过程中分解语句，执行时甚至不用访问表或索引，例如从一个索引列里选取最小值可以通过单独索引查找完成。
```

#### 6. 什么情况下索引失效

```
1.有or必全有索引;
2.复合索引未用左列字段;
3.like以%开头;  
4.需要类型转换;
5.where中索引列有运算;
6.where中索引列使用了函数;
7.如果mysql觉得全表扫描更快时（数据少）;
```

#### 7. 什么情况下没必要用索引

```
1.唯一性差;
2.频繁更新的字段不用（更新索引消耗）;
3.where中不用的字段;
4.索引使用<>时，效果一般;
```

####  8.Mysql主重复制原理？主库重库

~~~
在主从同步的过程中，主库会将所有的操作事件记录在 binlog 中，从库通过开启一个 I/O 线程保持与主库的通信，并在一定时间间隔内探测 binlog 日志文件是否发生改变。如果 binlog 日志发生了变化，主库生成一个 binlog dump 线程向从库 I/O 线程传送 binlog。从库上的 I/O 线程将 binlog 复制到自己的 relay log 中。最终由从库中的 SQL 线程读取 relay log 中的事件重放到从库上。


主库binlog日志-》从库I/O 线程->主库生成一个 binlog dump 线程->从库上的 I/O 线程将 binlog 复制到自己的 relay log 中->sql线程
~~~

#### 9.mysq慢日志查询

~~~
开启慢查询日志，查询超过阀值的语句。在mysql安装目录打开my.ini文件在mysqld 下添加

slow_query_log="ON"   是否开启

slow_query_log_file="文件路径（绝对路径）"   log保存位置

log_queries_not_using_indexes="ON"   查找没有设置索引的sql语句

long_query_time=1   阀值每几秒查询一下
~~~



#### 10.Mysql主重什么情况下会导致数据延迟，如何处理

可能产生的原因

~~~
随机重放
Mysql 主库中写 binlog 的操作是顺序写的，之前我们提到过，磁盘的顺序读写速度是很快的。同样的，从库中的 I/O 线程操作日志的速度效率也是很高的。但是别忘了，还有一个 SQL 线程来进行数据重放，而重放的过程是随机写盘的。到这里你应该就明白了吧，某一时刻 relay log 里的数据来不及重放进从库，就会产生主从延迟的情况。

主库并发高
知道了从库中 SQL 线程的重放情况，对于主库并发高导致主从延迟肯定就不难理解了。某一时刻，大量写请求打到主库上，意味着要不断对 binlog 进行写入，此时从库中的 SQL 线程就会应接不暇，自然会产生主从延迟。

锁等待
对于 SQL 单线程来说，当遇到阻塞时就会一直等待，直到执行成功才会继续进行。如果某一时刻从库因为查询产生了锁等待的情况，此时只有当前的操作执行完成后才会进行下面的操作，同理也就产生了主从延迟的情况。
~~~

解决方案

~~~
并行复制
既然 SQL 单线程进行重放时速度有限，那么能不能采用多线程的方式来进行重放呢？MySQL 5.6 版本后，提供了一种并行复制的方式，通过将 SQL 线程转换为多个 work 线程来进行重放，这样就解决了主从延迟的问题。

降低主库并发
你可能会说了，我现在用的低版本的数据库，也没法升版本啊，那我怎么整。对于主库并发高的情况，这种方式你只能通过控制并发来解决延迟了，多用用 Redis。

读主库
对于一些实时性要求比较高的数据从主库中读取
~~~

#### 9.分库

```
数据库的配制16核32G的机器线上每秒请求不要超过2000，这个范围一般不会有太大的压力。单表数据不要超过1000万。

用户已经注册2000万，每天活跃用户数100万！每天单表新增数据量达到50万条！高峰期每秒请求量达到1万，天单表新增50万条数据，
一个月就多1500万条数据，一年下来单表会达到上亿条数据。高峰期请求现在是每秒1万，需要部署20台机器，平均每台机器每秒支撑500请求，
这个还能抗住，没啥大问题。数据库每秒不要超过2000，所以需要用到分库。

首先第一步，就是在上万并发请求的场景下，部署个5台服务器，每台服务器上都部署一个数据库实例。

然后每个数据库实例里，都创建一个一样的库，比如说订单库。

此时在5台服务器上都有一个订单库，名字可以类似为：db_order_01，db_order_02，等等。

然后每个订单库里，都有一个相同的表，比如说订单库里有订单信息表，那么此时5个订单库里都有一个订单信息表。

比如db_order_01库里就有一个tb_order_01表，db_order_02库里就有一个tb_order_02表。

这就实现了一个基本的分库分表的思路，原来的一台数据库服务器变成了5台数据库服务器，原来的一个库变成了5个库，
原来的一张表变成了5个表。你可以根据比如订单id来hash后按5取模，比如每天订单表新增50万数据，此时其中10万条数
据会落入db_order_01库的tb_order_01表，另外10万条数据会落入db_order_02库的tb_order_02表，以此类推。

```

#### 10.分表

```
上述的数据库架构还有一个问题，那就是单表数据量还是过大，现在订单表才分为了5张表，那么如果订单一年有1亿条，每个
表就有2000万条，这也还是太大了。所以要继续分析，把订单表分成1024张，这样1亿数据量的话，分散到每个表里也就才10
万量级的数据量，然后这上千张表分散在5台数据库里就可以了，在写入数据的时候，需要做两次路由，先对订单id hash后对
数据库的数量取模，可以路由到一台数据库上，然后再对那台数据库上的表数量取模，就可以路由到数据库上的一个表里了，
通过这个步骤，就可以让每个表里的数据量非常小，每年1亿数据增长，但是到每个表里才10万条数据增长，这个系统运行10年，
每个表里可能才百万级的数据量。
```

#### 11.读写分离

```
假如说每台数据库服务器承载每秒2000的请求，然后其中400请求是写入，1600请求是查询。

也就是说，增删改的SQL才占到了20%的比例，80%的请求是查询。

此时假如说随着用户量越来越大，假如说又变成每台服务器承载4000请求了。

那么其中800请求是写入，3200请求是查询，如果说你按照目前的情况来扩容，就需要增加一台数据库服务器.

但是此时可能就会涉及到表的迁移，因为需要迁移一部分表到新的数据库服务器上去，是不是很麻烦？

其实完全没必要，数据库一般都支持读写分离，也就是做主从架构。

写入的时候写入主数据库服务器，查询的时候读取从数据库服务器，就可以让一个表的读写请求分开落地到不同的数据库上去执行。
读请求的增长速度远远高于写请求，所以读写分离之后，大部分时候就是扩容从库支撑更高的读请求就可以了。对同一个表，如果你
既写入数据（涉及加锁），还从该表查询数据，可能会牵扯到锁冲突等问题，无论是写性能还是读性能，都会有影响。所以一旦读写分
离之后，对主库的表就仅仅是写入，没任何查询会影响他，对从库的表就仅仅是查询。
```

#### 12.雪花算法

<img src="images/13.png">

```
单台机器实例，通过时间戳保证前41位是唯一的，分布式系统多台机器实例下，通过对每个机器实例分配不同的datacenterId和workerId
避免中间的10位碰撞。最后12位每毫秒从0递增生产ID，再提一次：每毫秒最多生成4096个ID，每秒可达4096000个。理论上，只要CPU计算
能力足够，单机每秒可生产400多万个，实测300w+


#首先安装库
pip3 install pysnowflake
#安装完成后，就可以在本地命令行启动snowflake服务
snowflake_start_server --worker=1

def test():
    #3  4 
    import snowflake.client
    uid = snowflake.client.get_guid()
    #分到哪个库
    database = uid%3
    #分到哪张表
    table = uid%5

    
for i in range(100):
    test()
```

####  11.mysql中的事务

~~~
一个最小的不可再分的工作单元；通常一个事务对应一个完整的业务(例如银行账户转账业务，该业务就是一个最小的工作单元)，必须同时成功或者同时失败

BEGIN 开始一个事务
ROLLBACK 事务回滚
COMMIT 事务确认
~~~

事务的特性

~~~
原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。
~~~

事务的隔离级别

~~~
（1）read_uncommitted（读未提交）

可读取未提交事务的操作数据，最低的隔离级别，一般都没有用的。这种情况会出现脏读。

（2）read_committed（读已提交）

一个事务等另一个事务提交之后才可进行读取，解决了脏读问题，但会出现不可重复读

（3）repeatable_read（可重复读）

读取事务开启的时候不能对数据进行修改，解决了不可重复读问题，但是存在幻读问题；

（4）serializable（序列化）：是最高的事务隔离级别，可以避免脏读、不可重复读与幻读。但是这种事务隔离级别效率低下，比较耗数据库性能，一般不使用；

可以根据需求设置数据库的事务的级别。“读未提交”一般没用，“读已提交”解决脏读但存在不可重复读，“可重复读”解决了脏读和不可重复读，但会出现幻读。串行化读，都可以解决，但是需要注意的是事务级别越高性能越低。
~~~

**高并发情况下，事务可能出现的几种情况：脏读、幻读、不可重复读**

~~~
1、脏读

出现原因：一个事务读取到了缓存中另一个事务未提交的脏数据。

说明：当事务B对data进行了修改但是未提交事务，此时事务A对data进行读取，并使用事务B修改的数据做业务处理。

2、幻读

出现原因：一个事务在读取数据时，另一个事务插入了数据，导致上个事务第二次读取数据时，数据不一致。

说明：data 表有一条数据，事务A对data进行读取， 事务B对data进行数据新增 ，此时事务A读取只有一条数据，而最后实际data是有两条数据，就好象发生了幻觉一样情况成为幻读；

3、不可重复读

出现原因：读取数据的同时可以进行修改;

说明：事务A、事务B同时对data进行访问，事务A对data进行读取，事务B对data进行修改，当事务A第一次对data进行读取完后事务B提交，此时当事务A第二次读取该数据时的数据就与第一次读取的数据不同，这种情况称为不可重复读；
~~~

#### 12.mysql锁

~~~
乐观锁
默认为不会修改，不加锁，操作前判断，提交的时候再判断，以购买车为例，购买时购物车查询库存，生成订单再查询库存，如果两次相同中间没被操作继续执行，如果两次不相同已经被修改，根据情况做下一步操作。

悲观锁
在操作的时候加锁，用select for update;实现

行级锁 
　　行级锁是Mysql中锁定粒度最细的一种锁，表示只针对当前操作的行进行加锁。行级锁能大大减少数据库操作的冲突。其加锁粒度最小，但加锁的开销也最大。

特点
　　开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高。

表级锁
　　表级锁是MySQL中锁定粒度最大的一种锁，表示对当前操作的整张表加锁，它实现简单，资源消耗较少，被大部分MySQL引擎支持。最常使用的MYISAM与INNODB都支持表级锁定。表级锁定分为表共享读锁（共享锁）与表独占写锁（排他锁）。

特点
　　开销小，加锁快；不会出现死锁；锁定粒度大，发出锁冲突的概率最高，并发度最低。
页级锁
　　页级锁是MySQL中锁定粒度介于行级锁和表级锁中间的一种锁。表级锁速度快，但冲突多，行级冲突少，但速度慢。所以取了折衷的页级，一次锁定相邻的一组记录。BDB支持页级锁

特点
　　开销和加锁时间界于表锁和行锁之间；会出现死锁；锁定粒度界于表锁和行锁之间，并发度一般
　　

MyISAM采用表级锁(table-level locking)
InnoDB支持行级锁(row-level locking)和表级锁,默认为行级锁

MyISAM中是不会产生死锁的，因为MyISAM总是一次性获得所需的全部锁，要么全部满足，要么全部等待。而在InnoDB中，锁是逐步获得的，就造成了死锁的可能。

发生死锁后，InnoDB一般都可以检测到，并使一个事务释放锁回退，另一个获取锁完成事务。降低隔离级别

有多种方法可以避免死锁，这里只介绍常见的三种

　　1、如果不同程序会并发存取多个表，尽量约定以相同的顺序访问表，可以大大降低死锁机会。

　　2、在同一个事务中，尽可能做到一次锁定所需要的所有资源，减少死锁产生概率；
~~~

### redis相关

#### 1.redis常用的数据类型

<img src="images/14.png">

```
1. String
常用命令: set,get,incr 等。

String数据结构是简单的key-value类型，value其实不仅可以是String，也可以是数字。 常规key-value缓存应用； 
应用场景 常规计数：微博数，粉丝数等。

2.Hash
常用命令： hget,hset,hgetall 等。

Hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象，后续操作的时候，你可以直接仅仅修改这个对象中的某个字段的值。 比如我们可以Hash数据结构来存储用户信息，商品信息。应用场景购物车

key=JavaUser293847
value={
  “id”: 1,
  “name”: “SnailClimb”,
  “age”: 22,
  “location”: “Wuhan, Hubei”
}

3.List
常用命令: lpush,rpush,lpop,rpop,lrange等

list 就是链表，Redis list 的应用场景非常多，也是Redis最重要的数据结构之一，比如微博的关注列表，粉丝列表，消息列表等功能都可以用Redis的 list 结构来实现。

Redis list 的实现为一个双向链表，即可以支持反向查找和遍历，更方便操作，不过带来了部分额外的内存开销。

另外可以通过 lrange 命令，就是从某个元素开始读取多少个元素，可以基于 list 实现分页查询，这个很棒的一个功能，基于 redis 实现简单的高性能分页，可以做类似微博那种下拉不断分页的东西（一页一页的往下走），性能高。

4.Set
常用命令： sadd,spop,smembers

set 对外提供的功能与list类似是一个列表的功能，特殊之处在于 set 是可以自动排重的。

比如：在微博应用中，可以将一个用户所有的关注人存在一个集合中，将其所有粉丝存在一个集合。Redis可以非常方便的实现如共同关注、共同粉丝、共同喜好等功能。

5.Sorted Set
常用命令： zadd,zrange,zrem,zcard等

和set相比，sorted set增加了一个权重参数score，使得集合中的元素能够按score进行有序排列。

举例： 在直播系统中，实时排行信息包含直播间在线用户列表，各种礼物排行榜，弹幕消息（可以理解为按消息维度的消息排行榜）等信息，适合使用 Redis 中的 SortedSet 结构进行存储。
```

#### 2.redis集群

```
Redis哨兵（Sentinel）模式

哨兵模式工作原理
　　哨兵集群中的每个节点都会启动三个定时任务
第一个定时任务： 每个sentinel节点每隔1s向所有的master、slaver、别的sentinel节点发送一个PING命令，作用：心跳检测
第二个定时任务： 每个sentinel每隔2s都会向master的__sentinel__:hello这个channel中发送自己掌握的集群信息和自己的一些信息（比如host,ip,run id），这个是利用redis的pub/sub功能，每个sentinel节点都会订阅这个channel，也就是说，每个sentinel节点都可以知道别的sentinel节点掌握的集群信息，作用：信息交换，了解别的sentinel的信息和他们对于主节点的判断
第三个定时任务： 每个sentinel节点每隔10s都会向master和slaver发送INFO命令，作用：发现最新的集群拓扑结构

哨兵如何判断master宕机

主观下线
　　这个就是上面介绍的第一个定时任务做的事情，当sentinel节点向master发送一个PING命令，如果超过own-after-milliseconds（默认是30s，这个在sentinel的配置文件中可以自己配置）时间都没有收到有效回复，不好意思，我就认为你挂了，就是说为的主观下线（SDOWN），修改其flags状态为SRI_S_DOWN

客观下线
　　要了解什么是客观下线要先了解几个重要参数：

quorum：如果要认为master客观下线，最少需要主观下线的sentinel节点个数，举例：如果5个sentinel节点，quorum = 2,那只要2个sentinel主观下线，就可以判断master客观下线
majority：如果确定了master客观下线了，就要把其中一个slaver切换成master，做这个事情的并不是整个sentinel集群，而是sentinel集群会选出来一个sentinel节点来做，那怎么选出来的呢，下面会讲，但是有一个原则就是需要大多数节点都同意这个sentinel来做故障转移才可以，这个大多数节点就是这个参数。注意：如果sentinel节点个数5，quorum=2，majority=3，那就是3个节点同意就可以，如果quorum=5，majority=3，这时候majority=3就不管用了，需要5个节点都同意才可以。
configuration epoch：这个其实就是version，类似于中国每个皇帝都要有一个年号一样，每个新的master都要生成一个自己的configuration epoch，就是一个编号


选择领头sentinel的过程
　　到现在为止，已经知道了master客观下线，那就需要一个sentinel来负责故障转移，那到底是哪个sentinel节点来做这件事呢？需要通过选举实现，具体的选举过程如下：
　　
判断客观下线的sentinel节点向其他节点发送SENTINEL is-master-down-by-addr ip port current_epoch runid（注意：这时的runid是自己的run id，每个sentinel节点都有一个自己运行时id）
目标sentinel回复，由于这个选择领头sentinel的过程符合先到先得的原则，举例：sentinel1判断了客观下线，向sentinel2发送了第一步中的命令，sentinel2回复了sentinel1，说选你为领头，这时候sentinel3也向sentinel2发送第一步的命令，sentinel2会直接拒绝回复
当sentinel发现选自己的节点个数超过majority（注意上面写的一种特殊情况quorum>majority）的个数的时候，自己就是领头节点
如果没有一个sentinel达到了majority的数量，等一段时间，重新选举


故障转移过程
　　
在进行选择之前需要先剔除掉一些不满足条件的slaver，这些slaver不会作为变成master的备选

剔除列表中已经下线的从服务
剔除有5s没有回复sentinel的info命令的slaver
剔除与已经下线的主服务连接断开时间超过 down-after-milliseconds*10+master宕机时长的slaver
选主过程
选择优先级最高的节点，通过sentinel配置文件中的replica-priority配置项，这个参数越小，表示优先级越高
如果第一步中的优先级相同，选择offset最大的，offset表示主节点向从节点同步数据的偏移量，越大表示同步的数据越多
如果第二步offset也相同，选择run id较小的


```

#### 3.redis持久化存储

```
快照（snapshotting）持久化（RDB）

Redis可以通过创建快照来获得存储在内存里面的数据在某个时间点上的副本。Redis创建快照之后，可以对快照进行备份，可以将快照复制到其他服务器从而创建具有相同数据的服务器副本（Redis主从结构，主要用来提高Redis性能），还可以将快照留在原地以便重启服务器的时候使用。
两个方法 save阻塞生成快照文件 。
        bgsave通过主进程fork出一个子进程，分配一块父子共享区域。主进程只有在Fork过程中有短暂的阻塞，子进程创建之后，主进程就可以响应客户端了。如何保持数据一致，copy or write.主进程修改数据时写时拷贝，在副本中修改，修改完再更新，保证子进程的数据的一致性。

AOF持久化

与快照持久化相比，AOF持久化 的实时性更好，默认情况下Redis没有开启AOF（append only file）方式的持久化，开启AOF持久化后每执行一条会更改Redis中的数据的命令，Redis就会将该命令写入硬盘中的AOF文件。

三种方式
appendfsync always     #每次有数据修改发生时都会写入AOF文件,这样会严重降低Redis的速度
appendfsync everysec  #每秒钟同步一次，显示地将多个写命令同步到硬盘
appendfsync no      #让操作系统决定何时进行同步
建议采用第二种，让Redis每秒同步一次AOF文件，Redis性能几乎没受到任何影响。而且这样即使出现系统崩溃，用户最多只会丢失一秒之内产生的数据。当硬盘忙于执行写入操作的时候，Redis还会放慢自己的速度以便适应硬盘的最大写入速度。

```

#### 4.redis缓存雪崩

```
缓存同一时间大面积的失效，所以，后面的请求都会落到数据库上，造成数据库短时间内承受大量请求而崩掉。

解决办法：分散过期时间

事前：尽量保证整个 redis 集群的高可用性，发现机器宕机尽快补上。选择合适的内存淘汰策略。
事中：本地ehcache缓存 + hystrix限流&降级，避免MySQL崩掉
事后：利用 redis 持久化机制保存的数据尽快恢复缓存
```

#### 5.redis击穿

```
一般是黑客故意去请求缓存中不存在的数据，导致所有的请求都落到数据库上，造成数据库短时间内承受大量请求而崩掉。

解决办法： 有很多种方法可以有效地解决缓存穿透问题，最常见的则是采用布隆过滤器，将所有可能存在的数据哈希到一个足够大的bitmap中，一个一定不存在的数据会被 这个bitmap拦截掉，从而避免了对底层存储系统的查询压力。别外一种是，如果一个查询返回的数据为空（不管是数 据不存在，还是系统故障），我们仍然把这个空结果进行缓存，但它的过期时间会很短，最长不超过五分钟。
```

#### 布隆过滤器

~~~
位图，每个int都是32个bit位，int[10]就是320个bit,每个bit非0即1初始化都是0
添加数据时，将数据进行hash值到hash值，对应到Bit位，将该bit改为1，hash函数可以对应多个，减少hash碰撞。
查询数据 hash函数计算得到hash值，对应到bit中，如果有一个为0，则说明数据不在bit中，如果都为1，可能在bit中
~~~



#### 6.MySQL里有2000w数据，Redis中只存20w的数据，如何保证Redis中的数据都是热点数据？

```
edis 提供 6种数据淘汰策略：

volatile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰
volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰
volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰
allkeys-lru：当内存不足以容纳新写入数据时，在键空间中，移除最近最少使用的key（这个是最常用的）.
allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰
no-eviction：禁止驱逐数据，也就是说当内存不足以容纳新写入数据时，新写入操作会报错。不建议使用！
```

#### 7.redis过期处理

```
定期删除+惰性删除

定期删除：redis默认是每隔 100ms 就随机抽取一些设置了过期时间的key，检查其是否过期，如果过期就删除。注意这里是随机抽取的。为什么要随机呢？你想一想假如 redis 存了几十万个 key ，每隔100ms就遍历所有的设置过期时间的 key 的话，就会给 CPU 带来很大的负载！

惰性删除 ：定期删除可能会导致很多过期 key 到了时间并没有被删除掉。所以就有了惰性删除。假如你的过期 key，靠定期删除没有被删除掉，还停留在内存里，查询的时候删除
```

#### 8.redis事务处理

```
Redis 通过 MULTI、EXEC、WATCH 等命令来实现事务(transaction)功能。事务提供了一种将多个命令请求打包，然后一次性、按顺序地执行多个命令的机制，并且在事务执行期间，服务器不会中断事务而改去执行其他客户端的命令请求，它会将事务中的所有命令都执行完毕，然后才去处理其他客户端的命令请求。具有原子性（Atomicity)、一致性(Consistency)和隔离性（Isolation），并且当 Redis 运行在某种特定的持久化模式下时，事务也具有持久性（Durability）。
```

#### 9.如何解决 Redis 的并发竞争 Key 问题

```
所谓 Redis 的并发竞争 Key 的问题也就是多个系统同时对一个 key 进行操作，但是最后执行的顺序和我们期望的顺序不同，这样也就导致了结果的不同！

分布式锁setnx。（如果不存在 Redis 的并发竞争 Key 问题，不要使用分布式锁，这样会影响性能）
使用setnx命令方式，同时在redis上创建相同的一个key,国为rediskey不能重复，只要创建成功就获取到锁，没创建成功就等待，为了防止死锁现象要加有效期。

SET KEY VALUE  EX  PX

EX到期时间(以秒为单位)
PX到期时间(以毫秒为单位)

import redis
from flask import Flask



app = Flask(__name__)

# connect redis
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def limit_handler():
    """
    return True: 允许; False: 拒绝
    """
    amount_limit = 100  # 限制数量
    keyname = 'limit'  # redis key name
    incr_amount = 1  # 每次增加数量

    # 判断key是否存在
    if not r.exists(keyname):
        # 为了方便测试，这里设置默认初始值为95
        # setnx可以防止并发时多次设置key
        r.setnx(keyname, 95)

    # 数据插入后再判断是否大于限制数
    if r.incrby(keyname, incr_amount) <= amount_limit:
        return True

    return False


@app.route("/limit")
def v2():
    if limit_handler():
        return '1'
    else:
        return '2'


if __name__ == '__main__':
    app.run(debug=True)
    
    
#用ApacheBench测试-c并发数 -n请求数
ab -c 100 -n 200 http://127.0.0.1:5000/limit

```

#### 10.如何保证缓存与数据库双写时的数据一致性？

```
读的时候，先读缓存，缓存没有的话，就读数据库，然后取出数据后放入缓存，同时返回响应。更新的时候，先更新数据库，然后再删除缓存。为什么是删除缓存，而不是更新缓存？原因很简单，很多时候，在复杂点的缓存场景，缓存不单单是数据库中直接取出来的值。更新或添加后再删除一次缓存，延时双删。
```

11.Redis单线程为什么这么快？

~~~
纯内存操作，每一次操作都很快，没有读写等待。多线程cpu切换反正浪费时间。核心基于非堵塞的io多路复用模型
select poll epoll fd就绪队列

Redis基于socket客户端和服务端，io多路复用器监听多个socket,将socket放入队列，从队列中取出分配处理。
~~~



### django

#### Django生命周期为

~~~
用户请求发起对url的请求→ngnix-> wsgi→django中间件→django（视图url对应函数，模型数据库交互，html模版渲染）→django中间件 → wsgi →nginx 返回
~~~



![image-20220628100211172](/Users/hanxiaobai/Library/Application Support/typora-user-images/image-20220628100211172.png)

#### 自带的中间件

~~~
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', //主要是针对安全访问处理，就是把http请求重定向到https请求
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
~~~

#### 自定义中间件（继承MiddlewareMixin重写五个方法）

~~~
3.1 process_request
执行时间：在视图函数之前，在路由匹配之前
参数：
	request：请求对象，与视图中用到的request参数是同一个对象
返回值：
	None：按照正常的流程走
	HttpResponse：接着倒序执行当前中间件的以及之前执行过的中间件的
	process_response方法，不再执行其它的所有方法

3.2 process_response
执行时间：最后执行
参数：
	request：请求对象，与视图中用到的request参数是同一个对象
	response：响应对象，与视图中返回的response是同一个对象
返回值：
	response：必须返回此对象，按照正常的流程走

3.3 process_view
执行时间：在process_request方法及路由匹配之后，视图之前
参数：
	request：请求对象，与视图中用到的request参数是同一个对象
	view_func：将要执行的视图函数（它是实际的函数对象，而不是函数的名称作为字符串）
	view_args：url路径中将传递给视图的位置参数的元组
	view_kwargs：url路径中将传递给视图的关键值参数的字典
返回值：
	None：按照正常的流程走
	HttpResponse：它之后的中间件的process_view，及视图不执行，执行所有中间件的process_response方法


3.4 process_template_response
此方法必须在视图函数返回的对象有一个render()方法（或者表明该对象是一个TemplateResponse对象或等价方法）时，才被执行

执行时间：视图之后，process_exception之前
参数：
	request：请求对象，与视图中用到的request参数是同一个对象
	response：是TemplateResponse对象（由视图函数或者中间件产生）
返回值：
	response：必须返回此对象，按照正常的流程走


3.5 process_exception
此方法只在视图中触发异常时才被执行.

执行时间：视图之后，process_response之前
参数：
	request：请求对象，与视图中用到的request参数是同一个对象
	exception：视图函数异常产生的Exception对象
返回值：
	None：按照正常的流程走
	HttpResponse对象：不再执行后面的process_exception方法
~~~

#### drf框架

~~~
序列化、分页、限流、过滤、提供有三级视图
~~~

权限

~~~
AllowAny                         # 允许所有用户
IsAuthenticated                  # 仅通过认证的用户
IsAdminUser                      # 仅管理员用户
IsAuthenticatedOrReadOnly        # 认证的用户可以完全操作，否则只能get读取
~~~

认证

~~~
Django rest framework内置的认证类
##路径:rest_framework.authentication

BasicAuthentication  #基于浏览器进行认证，浏览器弹框,可以弹出登录框,username和password形式认证.多用于测试
SessionAuthentication #基于django的session进行认证
RemoteUserAuthentication #基于django admin中的用户进行认证，这也是官网的示例
TokenAuthentication #基于drf内部的token认证
JSONWebTokenAuthentication # 结合django的auth_user表,实现的jwt认证
~~~

### F查询和Q查询

~~~

~~~





### 其他

#### 1. nginx

Nginx 是一个很强大的高性能[Web](https://baike.baidu.com/item/Web/150564)和[反向代理](https://baike.baidu.com/item/反向代理)服务，它具有很多非常优越的特性：

在连接高并发的情况下，Nginx是[Apache](https://baike.baidu.com/item/Apache/6265)服务不错的替代品：Nginx在美国是做虚拟主机生意的老板们经常选择的软件平台之一。能够支持高达 5万 个并发连接数的响应, nginx可以做反向代理，反向代理服务器决定哪台服务器提供服务。返回代理服务器不提供服务器。只是请求的转发。

~~~
1、轮询（默认）
每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。

upstream backserver {
    server 192.168.0.14;
    server 192.168.0.15;
}


2、权重 weight
指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况。

upstream backserver {
    server 192.168.0.14 weight=3;
    server 192.168.0.15 weight=7;
}


3、ip_hash（ IP绑定）
上述方式存在一个问题就是说，在负载均衡系统中，假如用户在某台服务器上登录了，那么该用户第二次请求的时候，因为我们是负载均衡系统，每次请求都会重新定位到服务器集群中的某一个，那么已经登录某一个服务器的用户再重新定位到另一个服务器，其登录信息将会丢失，这样显然是不妥的。

我们可以采用ip_hash指令解决这个问题，如果客户已经访问了某个服务器，当用户再次访问时，会将该请求通过哈希算法，自动定位到该服务器。

每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。

upstream backserver {
    ip_hash;
    server 192.168.0.14:88;
    server 192.168.0.15:80;
}


4、fair（第三方插件）
按后端服务器的响应时间来分配请求，响应时间短的优先分配。

upstream backserver {
    server server1;
    server server2;
    fair;
}


5、url_hash（第三方插件）
按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。

upstream backserver {
    server squid1:3128;
    server squid2:3128;
    hash $request_uri;
    hash_method crc32;
}
~~~

#### 2.celery

Celery 是一个专注于实时处理和任务调度的分布式任务队列,本身不是任务队列, 是管理分布式任务队列的工具.任务队列采用redis中的list或mq实现,有5个常用组件

```
Task
就是任务，有异步任务和定时任务

Beat
定时任务调度器，根据配置定时将任务发送给Broker。

Broker
中间人，接收生产者发来的消息即Task，将任务存入队列。任务的消费者是Worker。

Worker
执行任务的单元，它实时监控消息队列，如果有任务就获取任务并执行它。

Backend
用于存储任务的执行结果。

```

 celery用CELERYBEAT_SCHEDULE实现定时任务。消息失败可以通过self.retry(exc=e,countdown=3,max_retries=5)来设置重试次数和间隔时间。celery默认会开启4个线程来处理任务，参数-c可以开启更多任务线程。执行定时任务时, Celery会通过celerybeat进程来完成。Celerybeat会保持运行, 一旦到了某一定时任务需要执行时, Celerybeat便将其加入到queue中，适用于周期性任务。

#### 3.celery配制

~~~
BROKER_URL = "redis://47.106.106.220:5000/1" 
CELERY_RESULT_BACKEND = "redis://47.106.106.220:5000/2"

#指定队列

CELERY_QUEUES = (
Queue("default",Exchange("default"),routing_key="default"),
Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B") 
)

# 路由
CELERY_ROUTES = {
'tasks.taskA':{"queue":"for_task_A","routing_key":"for_task_A"},
'tasks.taskB':{"queue":"for_task_B","routing_key":"for_task_B"}
}


启动两个worker来分别指定taskA、taskB，开两个窗口分别执行下面语句, 一个work对应一个队列
-A启动任务名称 -l日志级别  -c指定线程数   -Q指定队列名

celery -A tasks worker -l info -n workerA.%h -Q for_task_A

celery -A tasks worker -l info -n workerB.%h -Q for_task_B
~~~

#### 4.celery定时配制

task指定任务，schedule间隔时间，args传递参数没有可以不写，'schedule': crontab(hour=7, minute=30, day_of_week=1)通过crontab指定具体的时间和linux下crontab一样

~~~
CELERYBEAT_SCHEDULE = {
    'taskA_schedule' : {
        'task':'tasks.taskA',
        'schedule':2,
        'args':(5,6)
    },
    'taskB_scheduler' : {
        'task':"tasks.taskB",
        "schedule":10,
        "args":(10,20,30)
    }
}

#启动定时任务

celery -A tasks beat
~~~

#### 5.如何防止 Celery 重复执行同一个任务

~~~
Celery Once 也是利用 Redis 加锁来实现, Celery Once 在 Task 类基础上实现了 QueueOnce 类，该类提供了任务去重的功能，所以在使用时，我们自己实现的方法需要将 QueueOnce 设置为 base

@task(base=QueueOnce, once={'graceful': True})
后面的 once 参数表示，在遇到重复方法时的处理方式，默认 graceful 为 False，那样 Celery 会抛出 AlreadyQueued 异常，手动设置为 True，则静默处理。
~~~

#### 3.用过docker吗

~~~
Docker 是一个开源的应用容器引擎，以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化，共享宿主机资源。docker主要有三部分，容器、镜像、仓库

docker images 来列出本地主机上的镜像
docker search 查找镜像
docker pull  下载镜像
docker run -it 镜像名 /bin/bash 运行容器
docker start 启动容器
docker stop 停止窗口
docker rm 删除容器
docker cp 拷贝文件
docker exec 进入容器


docker -it  i是什么  t是什么

-i  以交互模式运行容器

-t  为容器重新分配一个伪输入终端   -it配合使用

-d  后台运行容器，并返回容器ID；

-p  端口映射



~~~

#### 5.Docker Compose

~~~
Docker Compose是Docker官方提供的一个工具，用于定义和运行多个Docker容器的应用。使用Docker Compose可以将多个容器组合成一个应用，并通过一个配置文件（docker-compose.yml）来管理这些容器。Docker Compose可以帮助我们更方便地管理和部署Docker应用，同时还能够提高应用的可移植性和可维护性。

下面是一些Docker Compose的常用命令：

docker-compose up：启动容器。
docker-compose up -d：以守护进程模式启动容器。
docker-compose down：停止容器并删除容器。
docker-compose stop：停止容器。
docker-compose start：启动已经停止的容器。
docker-compose restart：重启容器。
docker-compose ps：列出所有容器。
docker-compose logs：查看容器日志。
docker-compose exec：在容器中执行命令。
在使用Docker Compose时，我们需要创建一个docker-compose.yml文件，用于定义应用的各个组件。这个文件的格式为YAML格式，可以使用文本编辑器进行编辑。下面是一个简单的docker-compose.yml文件的例子：

version: '3'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
  db:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: example
    volumes:
      - ./data:/var/lib/mysql
在这个例子中，我们定义了两个服务：一个是Nginx Web服务器（web），另一个是MySQL数据库（db）。web服务使用了nginx:latest镜像，并将容器的80端口映射到主机的80端口。web服务还挂载了一个本地的nginx.conf文件到容器的/etc/nginx/nginx.conf路径下。db服务使用了mysql:latest镜像，并设置了MYSQL_ROOT_PASSWORD环境变量以指定root密码。db服务还挂载了一个本地的data目录到容器的/var/lib/mysql路径下。

使用Docker Compose启动这个应用的命令为：

docker-compose up -d
这个命令将会启动web和db两个服务，并在后台运行。在运行过程中，可以使用以下命令来管理这些服务：

docker-compose ps  # 列出所有容器
docker-compose logs web  # 查看web容器的日志
docker-compose exec db mysql -uroot -pexample  # 在db容器中执行mysql命令
需要注意的是，Docker Compose会自动创建一个默认的网络，用于连接这些容器。在容器中可以使用服务的名称来进行通信，例如在web容器中可以使用db作为MySQL数据库的主机名。
~~~

#### Docker Compose搭建mysql主重

~~~
创建一个docker-compose.yml文件，包含两个MySQL服务定义：一个用作主节点，另一个用作从节点。以下是一个示例文件：
version: '3'
services:
  mysql-master:
    image: mysql:5.7
    container_name: mysql-master
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: test
    ports:
      - "3306:3306"
    volumes:
      - ./mysql-master-data:/var/lib/mysql
      - ./mysql-master-config:/etc/mysql/conf.d
    command: mysqld --server-id=1 --log-bin=mysql-bin --binlog-do-db=test --binlog-ignore-db=mysql

  mysql-slave:
    image: mysql:5.7
    container_name: mysql-slave
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3307:3306"
    volumes:
      - ./mysql-slave-data:/var/lib/mysql
      - ./mysql-slave-config:/etc/mysql/conf.d
    command: mysqld --server-id=2 --log-bin=mysql-slave-bin --relay-log=mysql-relay-bin --binlog-do-db=test --binlog-ignore-db=mysql --slave-skip-errors=all --slave-net-timeout=60 --skip-slave-start
在这个文件中，我们定义了两个MySQL服务：mysql-master和mysql-slave。mysql-master服务用作主节点，mysql-slave服务用作从节点。我们使用mysql:5.7镜像作为MySQL服务的基础镜像，并为每个服务提供了一个容器名称、一个重启策略和一些环境变量。

我们还将主节点的端口映射到主机的3306端口，从节点的端口映射到主机的3307端口。我们还将每个服务的数据目录和配置文件目录映射到主机上的目录。最后，我们为每个服务提供了一个命令，用于启动MySQL服务并配置主从复制。

创建两个目录，用于存储MySQL服务的数据和配置文件。在终端中执行以下命令：
mkdir mysql-master-data mysql-master-config mysql-slave-data mysql-slave-config
启动Docker Compose应用程序。在终端中执行以下命令：
docker-compose up -d
这将启动两个MySQL服务，并将它们作为Docker容器在后台运行。

配置主节点。在终端中执行以下命令，连接到主节点的MySQL服务：
docker exec -it mysql-master mysql -uroot -proot
在MySQL命令行中执行以下命令，创建一个用于从节点复制的用户，并授予复制权限：

CREATE USER 'replicator'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replicator'@'%';
然后，执行以下命令，获取主节点的二进制日志文件名和位置：

SHOW MASTER STATUS;
这将返回一个结果集，其中包含主节点的二进制日志文件名和位置。请记下这些值，因为你将在下一步中将它们用于配置从节点。
mysql-bin.000003 |      607 | test         | mysql        
配置从节点。在终端中执行以下命令，连接到从节点的MySQL服务：
docker exec -it mysql-slave mysql -uroot -proot
在MySQL命令行中执行以下命令，将从节点配置为复制主节点：

CHANGE MASTER TO
  MASTER_HOST='mysql-master',
  MASTER_USER='replicator',
  MASTER_PASSWORD='password',
  MASTER_LOG_FILE='mysql-bin.000003',
  MASTER_LOG_POS=607;
请将<master_log_file>和<master_log_pos>替换为你在第4步中获取的值。

然后，执行以下命令，启动从节点的复制过程：

START SLAVE;
检查主从复制是否正常工作。在终端中执行以下命令，连接到从节点的MySQL服务：
docker exec -it mysql-slave mysql -uroot -proot
在MySQL命令行中执行以下命令，查看从节点的复制状态：

SHOW SLAVE STATUS\G
这将返回一个结果集，其中包含有关从节点的复制状态的详细信息。请确保Slave_IO_Running和Slave_SQL_Running列的值均为Yes，这表示从节点正在成功复制主节点上的数据。
~~~



#### 4.dockerfile

~~~
Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 Dockerfile。

Dockerfile 是一个文本文件，其内包含了一条条的指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。有了 Dockerfile，当我们需要定制自己额外的需求时，只需在 Dockerfile 上添加或者修改指令，重新生成 image 即可，省去了敲命令的麻烦。
~~~

编写dockerfile(安装并启动ngnix)

~~~
# Base images 基础镜像
FROM centos

#MAINTAINER 维护者信息
MAINTAINER lorenwe 

#ENV 设置环境变量
ENV PATH /usr/local/nginx/sbin:$PATH

#ADD  文件放在当前目录下，拷过去会自动解压
ADD nginx-1.13.7.tar.gz /tmp/

#RUN 执行以下命令
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    && yum update -y \
    && yum install -y vim less wget curl gcc automake autoconf libtool make gcc-c++ zlib zlib-devel openssl openssl-devel perl perl-devel pcre pcre-devel libxslt libxslt-devel \
    && yum clean all \
    && rm -rf /usr/local/src/*
RUN useradd -s /sbin/nologin -M www

#WORKDIR 相当于cd
WORKDIR /tmp/nginx-1.13.7

RUN ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-pcre && make && make install

RUN cd / && rm -rf /tmp/

COPY nginx.conf /usr/local/nginx/conf/

#EXPOSE 映射端口
EXPOSE 80 443

#ENTRYPOINT 运行以下命令
ENTRYPOINT ["nginx"]

#CMD 运行以下命令
CMD ["-h"]复制代码
~~~

构建静像（-f指定该文件的位置，-t参数指定构建成镜像的仓库、标签）

~~~
"docker build -t lorenwe/centos_nginx . ",注意后面的点不能省略，表示的从当前目录中寻找 dockerfile 来构建镜像
~~~

启动

~~~
docker run -itd -p 8080:80 --name nginx3 lorenwe/centos_nginx -c /usr/local/nginx/conf/nginx.conf
~~~

~~~
1.常用指令讲解
FROM [镜像:版本]：指定所依赖的基础镜像

RUN <命令行命令>：等同于在终端执行的shell命令

RUN ["可执行文件", "参数1", "参数2"]：等同于在终端shell中执行 ./可执行文件

COPY <源文件> <目标文件>：将Dockerfile同目录下的文件拷贝到容器里面

ADD <源文件> <目标文件>：类似于COPY，区别在于如果文件是*.tar、*.gzip、*.bzip2等文件，会自动解压缩

CMD <命令行命令>：类似于RUN，区别在于：

RUN 是在 docker build 时运行
CMD 是在 docker run 时运行
存在多个 CMD 指令，仅最后一个生效
CMD 会被 docker run 的命令行参数指定的--entrypoint 选项所覆盖
ENTRYPOINT ["<可执行命令>", "<参数1>", "<参数22>"]：类似于CMD，存在多个 ENTRYPOINT 指令，仅最后一个生效，区别在于：

ENTRYPOINT 不会被 docker run 的命令行参数指定的指令所覆盖

ENTRYPOINT 可以搭配 CMD 命令使用：一般是变参才会使用 CMD ，这里的 CMD 等于是在给 ENTRYPOINT 传参，比如：

FROM nginx

ENTRYPOINT ["nginx", "-c"] # 定参
CMD ["/etc/nginx/nginx.conf"] # 变参 
1
2
3
4
不传参：

$ docker run nginx:test
1
容器内会执行如下命令：

$ nginx -c /etc/nginx/nginx.conf
1
传参：

$ docker run nginx:test -c /etc/nginx/new.conf
1
容器内会执行如下命令：

$ nginx -c /etc/nginx/new.conf
1
ENV：设置环境变量，示例：

ENV NODE_VERSION 7.2.0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"
1
2
3
4
ARG：类似于ENV，区别在于 ARG 只在 docker build 过程中有效，build 好之后，镜像内不存在设定的环境变量。

VOLUME：定义挂载数据卷，一般为/tmp，作用是避免容器内数据因为重启而丢失。

EXPOSE：声明暴露端口，docker run -P 时会自动映射EXPOSE指定的端口，-p 会覆盖声明的端口。

WORKDIR：指定工作目录，指定的工作目录，会在构建的镜像的每一层都在。（WORKDIR 指定的工作目录，必须是提前创建好的）。docker build 过程中，每一个RUN命令都是新建的一层，只有通过 WORKDIR 创建的目录会一直存在。

LABEL：给镜像添加标签，以键值对的形式存在，比如添加镜像的作者：

LABEL org.opencontainers.image.authors="acgkaka"
1
注意： Dockerfile 的每一行指令都会在docker上新建一层，为了避免镜像过大，尽量将命令写在同一行，例如：

FROM centos
RUN yum -y install **wget**
RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
1
2
3
合并为：

FROM centos
RUN yum -y install wget \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
1
2
3
如上，以 && 符号连接命令，这样执行后，只会创建 1 层镜像。

参考：Dockerfile|菜鸟教程


2.制作Hello World的Dockerfile
1）创建一个空白目录

2）在空白目录中新建一个Dockerfile文本文件：

FROM centos
# 只是单纯的打印"hello world"
RUN echo "hello world"
1
2
3
3）用命令行打开当前目录，输入如下内容

docker build -t hello_world .(最后有一个点)



4）查看docker镜像

docker images



5）创建容器

docker run -d --name=hello_world hello_world



6）启动容器

docker start hello_world



7）补充

删除容器：docker rm -f hello_world

删除镜像：docker rmi hello_world

~~~



#### 4.说一下秒杀解决方案

~~~
微服务架构模块化部署  人人  用户中心  发布信息   购买模块
页面静态化 
缓存
队列
熔断机制  500   600
分表

~~~



~~~
高并发相关常用的一些指标有响应时间（Response Time），吞吐量（Throughput），每秒查询率QPS（Query Per Second），并发用户数等。

响应时间：系统对请求做出响应的时间。例如系统处理一个HTTP请求需要200ms，这个200ms就是系统的响应时间。

吞吐量：单位时间内处理的请求数量。

QPS：每秒响应请求数。在互联网领域，这个指标和吞吐量区分的没有这么明显。

并发用户数：同时承载正常使用系统功能的用户数量。例如一个即时通讯系统，同时在线量一定程度上代表了系统的并发用户数。

主要采用以下解决方案：

1.页面静态化

秒杀页面由商品信息和前端页面资源组成，前后端分离，页面资源不会经过后端服务器，将前端资源，放入CDN服务器中。CDN是内容分发网络，通过中心平台的负载均衡、内容分发、调度等模块使用用户就近获取所需内容，降低网络拥堵，提高用户访问响应速度。

2.缓存预热
将数据提前放入缓存中，比如秒杀，可以将设置好的商品信息、限购数据，库存数据都存入redis中

3.异步化、削峰值填谷，通过消息队列异步地创建订单

4.除了存集群之外，我们还可以通过流式计算如storm、flink来进行实时数据访问次数的统计。如果在短时间内，某条数据的访问次数突然爆增，超过指定的阈值，那么就可以判定为是热点数据，然后把这条热点数据加入到缓存集群中，如果该数据的访问继续爆增，自然也不用担心扛不住的问题，因为都去访问缓存集群的数据了呀。

5.针对高并发我们还可以增加熔断限流保护机制。每个系统上线时，我们都会去做压力测试，了解整个系统的瓶颈点是多少？假设通过压力测试发现集群部署模式下，系统最多承受10万个请求，总共有100台服务器进行部署，均摊下来每个服务器最多能接受的请求不超过1000次，如果有第1001个用户访问时，就直接返回报错信息，让用户进行重试。这种方式虽然用户体验不是特别友好，但是系统却不会出错，也保障了前面1000个用户的使用体验。当下的淘宝、天猫、京东等电商网站大部分采取的便是此类的熔断限流机制。
~~~

5.支付宝支付流程

~~~
支付宝开放平台用企业资质注册-》安装支付宝sdk-》下载生成公钥私钥工具-》生成公钥私钥，在本地项目目录下创建keys文件夹-》将public和private复制到keys-》复制private私钥到支付宝后台换取公钥-》将公钥覆盖本地的public中的内容-》在支付宝管理中心配制回调地址-》在支付接口实例化alipay类，传入app_id,return_url,notify_url,公钥私钥-》调用支付宝支付传入订单号金额-》支付成功后回调-》在回调接口中更新数据库

return_url,notify_url有什么区别？
调用支付宝支付，先调用return_url返回支付结果，我们不能以这个结果作为最终结果。notify_url才是支付宝真正的处理结果，可以作为更新参数的依据，他会自动重试3次。
~~~

#### 6.订单过期处理

~~~
数据库定时任务：不建议使用效率低

Redis 实现方式
Redis 是通过有序集合（ZSet）的方式来实现延迟消息队列的，ZSet 有一个 Score 属性可以用来存储延迟执行的时间。
~~~

方式一查询所有过期的遍历

~~~
from redis import StrictRedis
redis_cli = StrictRedis(host="xxxxx", port=xx, password="xx", db=xx, decode_responses=True)
import time
 
 
class DelayQueue:
    """
    一次性查出所有符合条件的进行消费
    """
 
    def __init__(self):
        self.queue_key = "delay_all"
 
    def do_publish(self):
        now = time.time()
        redis_cli.zadd(self.queue_key, {"key30": now + 30})
        redis_cli.zadd(self.queue_key, {"key10": now + 10})
        redis_cli.zadd(self.queue_key, {"key3": now + 3})
        redis_cli.zadd(self.queue_key, {"key5": now + 5})
        redis_cli.zadd(self.queue_key, {"key8": now + 8})
        data = redis_cli.zrangebyscore(self.queue_key, now, now + 50)
        print("add success, data is: >>>>>> %s" % data)
        self.consume()
 
    # 延迟队列消费
    def consume(self):
        while True:
            # 上一秒
            last_second = time.time() - 1
            now_second = time.time()
            data = redis_cli.zrangebyscore(self.queue_key, last_second, now_second)
            # print("data in delay queue is >>>>>>>: %s" % data)
            if data:
                # 消费
                for each in data:
                    print("消费的是：%s" % each)
            # 删除已经消费的
            redis_cli.zremrangebyscore(self.queue_key, last_second, now_second)
            time.sleep(1)
 
if __name__ == '__main__':
    d = DelayQueue()
    d.do_publish()
~~~

方式二：每次查询最早的一条任务，与当前时间判断，决定是否需要执行

~~~
class DelayFirst:
    """
    每次只查最早的一条任务
    """
 
    def __init__(self):
        self.queue_key = "delay_first"
 
    def publish(self):
        now = time.time()
        redis_cli.zadd(self.queue_key, {"key30": now + 30})
        redis_cli.zadd(self.queue_key, {"key10": now + 10})
        redis_cli.zadd(self.queue_key, {"key3": now + 3})
        redis_cli.zadd(self.queue_key, {"key5": now + 5})
        redis_cli.zadd(self.queue_key, {"key8": now + 8})
        data = redis_cli.zrangebyscore(self.queue_key, now, now + 50)
        print("add success, data is: >>>>>> %s" % data)
        self.do_consume()
 
    # 延迟队列消费
    def do_consume(self):
        while True:
            data = redis_cli.zrange(self.queue_key, 0, 0)
            print("data in delay queue is >>>>>>>: %s" % data)
            if data:
                # 消费
                for each in data:
                    # 获取时间，判断时间是否比当前时间小
                    cur_score = redis_cli.zscore(self.queue_key, each)
                    if cur_score <= time.time():
                        print("消费的是：%s" % each)
                        # 删除已经消费的
                        redis_cli.zrem(self.queue_key, each)
            time.sleep(1)
 
 
if __name__ == '__main__':
    # d = DelayQueue()
    # d.do_publish()
 
    d = DelayFirst()
    d.publish()
~~~



#### 6.mysql和redis连接池

~~~python
import redis
conn_pool=redis.ConnectionPool(host='',port=6379)
conn = redis_Redis(connection_poll=conn_pool)


#mysql连接池
import pymysql
import configUtil
from DBUtils.PooledDB import PooledDB


class MysqlUtil(object):

    # 连接池对象
    __pool = None

    def __init__(self, config):
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self.pool = MysqlUtil.__get_conn(config)

    @staticmethod
    def __get_conn(config):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        host = configUtil.read_config(config, "datasource_url", "mysqlConfig")
        username = configUtil.read_config(config, "datasource_username", "mysqlConfig")
        db_pwd = configUtil.read_config(config, "datasource_password", "mysqlConfig")
        db_database = configUtil.read_config(config, "datasource_database", "mysqlConfig")
        if MysqlUtil.__pool is None:
            __pool = PooledDB(pymysql, mincached=1, maxcached=10, maxconnections=10,
                              host=host, port=3306, user=username, passwd=db_pwd,
                              db=db_database, use_unicode=False, blocking=False, charset="utf8")
        return __pool

    def get_all(self, sql):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        try:
            con = self.pool.connection()
            cur = con.cursor()
            count = cur.execute(sql)
            if count > 0:
                result = cur.fetchall()
            else:
                result = False
            return result
        except Exception as e:
            print('SQL执行有误,原因:', e)
        finally:
            cur.close()
            con.close()

    def update(self, sql):
        try:
            con = self.pool.connection()
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except Exception as e:
            con.rollback()  # 事务回滚
            print('SQL执行有误,原因:', e)
        finally:
            cur.close()
            con.close()

~~~

#### 7.django、flask、tornado的区别

~~~
django是一个大而全的框架，重量级以功能而生的框架。提供了admin管理后台，方便对内容的管理提高高发的效率。自带了中间件session、common、csrf、corsheaders等，以及可以通过自定议中间件重写他的五个方法来做操作。一般是重写他的process_request来做权限管理。django提供了权限、认证、限流、分页等组件。支持常用的session\auth\jwt认证，权限有只读、管理员、登录用户等。django的drf框架用的特别多，主要用于接口开发，可以自动生成接口文档。提供了serilazers对序列化和反序列化的处理，支持嵌套序列化器的使用。提供了三级视图和minxin混入类的配合使用。适合功能多，对性能要求低的，比如一些后台管理管理。

flask是一个轻量级框架，性能比django高，速度快。采用werkzeug作为wsgi服务器。通过router路由装饰器方式处理访问的请求，提供了钩子函数、请求上下文、应用上下文，用request、cookie这样的请求上下文来传递参数，封装了http请求中的内容，记录请求中会话中的信息。用curret,g这样的应用上下文存储应用程序中的变量。提供了丰富的三方组件，常用的有flask-wtf用于对表单的处理，sqlalchemy和数据库的交互，flask-mail发邮件，flask-restful用于构建restful api以及session会话和cors对跨域的支持。适合写一些脚本开发、自动化测试平台等这些项目。

tornado是一个异步非阻塞的框架，基于python中的协程实现，以一种轻量级的线程，可以在单线程中实现并发，每个请求都被封装成一个协程，处理中挂起，等待i/o操作完继续执行，避免线程切换的开销，提高了性能。tornado采用了事件循环机制来管理协程的执行，它会不断的从i/o事件队列中取出事件处理，基于io多路复用模型中的epoll，采用fd文件的方式，首先注册一个io事件，监听当处理完加入已经就绪的队列，循环从已经就绪队列中读取。适合做业务端用户量大、并发访问这样的业务场景，提供了对websocket的集成。(get_query_arguments,get_body_argument获取参数)
~~~

#### 8.字典的排序

~~~python
方法一：
adict={"a":100,"b":20,"c":10,"d":159}
data = sorted(adict.items(),key=lambda x:x[1],reverse=True)
print(data)

方法二：
d = {'apple': 50, 'banana': 20, 'orange': 40, 'pear': 70}
sorted_tuples = sorted(zip(d.values(), d.keys()))
sorted_dict = {k: v for v, k in sorted_tuples}
print(sorted_dict)


8个人  4个开发，2个前端，1个产品，1个运维
~~~



#### 7.排序

##### 插入排序：

插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序；首先将第一个作为已经排好序的，然后每次从后的取出插入到前面并排序；

时间复杂度：O(n²)

空间复杂度：O(1)

稳定性：稳定

~~~
def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            if ilist[i] < ilist[j]:
                ilist.insert(j, ilist.pop(i))
                break
    return ilist
~~~

##### 冒泡排序：

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成

时间复杂度：O(n²)

空间复杂度：O(1)

稳定性：稳定

~~~
def bubble_sort(blist):
    count = len(blist)
    for i in range(0, count):
        for j in range(i + 1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    return blist

blist = bubble_sort([4,5,6,7,3,2,6,9,8])
print(blist)

~~~

##### 快排

快速排序：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列

时间复杂度：O(nlog₂n)

空间复杂度：O(nlog₂n)

稳定性：不稳定

~~~
def quick_sort(qlist):
    if qlist == []:
        return []
    else:
        qfirst = qlist[0]
        qless = quick_sort([l for l in qlist[1:] if l < qfirst])
        qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore

qlist = quick_sort([4,5,6,7,3,2,6,9,8])
~~~

##### 选择排序：

第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕

时间复杂度：O(n²)

空间复杂度：O(1)

稳定性：不稳定

~~~
def select_sort(slist):
    for i in range(len(slist)):
        x = i
        for j in range(i, len(slist)):
            if slist[j] < slist[x]:
                x = j
        slist[i], slist[x] = slist[x], slist[i]
    return slist

slist = select_sort([4,5,6,7,3,2,6,9,8])

~~~

##### 归并排序：

采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并

时间复杂度：O(nlog₂n)

空间复杂度：O(1)

稳定性：稳定

    def merge_sort(array):
        def merge_arr(arr_l, arr_r):
            array = []
            while len(arr_l) and len(arr_r):
                if arr_l[0] <= arr_r[0]:
                    array.append(arr_l.pop(0))
                elif arr_l[0] > arr_r[0]:
                    array.append(arr_r.pop(0))
            if len(arr_l) != 0:
                array += arr_l
            elif len(arr_r) != 0:
                array += arr_r
            return array
            
    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)
    
    return recursive(array)
#### 8.查找

##### 顺序查找

算法简介 顺序查找又称为线性查找，是一种最简单的查找方法。适用于线性表的顺序存储结构和链式存储结构。该算法的时间复杂度为O(n)。 基本思路 从第一个元素m开始逐个与需要查找的元素x进行比较，当比较到元素值相同(即m=x)时返回元素m的下标，如果比较到最后都没有找到，则返回-1。 优缺点 缺点：是当n 很大时，平均查找长度较大，效率低； 优点：是对表中数据元素的存储没有要求。另外，对于线性链表，只能进行顺序查找。 算法实现

```
def sequential_search(lis, key):
  length = len(lis)
  for i in range(length):
    if lis[i] == key:
      return i
    else:
      return False
```

##### 折半查找

二分查找（Binary Search），是一种在有序数组中查找某一特定元素的查找算法。查找过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则查找过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。 这种查找算法每一次比较都使查找范围缩小一半。

算法描述 给予一个包含 个带值元素的数组A 1、 令 L为0 ， R为 n-1 2、 如果L>R，则搜索以失败告终 3、 令 m (中间值元素)为 ⌊(L+R)/2⌋ 4、 如果 AmT，令 R为 m - 1 并回到步骤二 复杂度分析 时间复杂度：折半搜索每次把搜索区域减少一半，时间复杂度为 O(logn) 空间复杂度：O(1)

```
# 二分法查询，排序
list = [1,6,3,8,5,7]
#排序
list1 = sorted(list)
#[1,3,5,6,7,8]
def binary_search(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        m = int((i + j) / 2)
        print("m"+str(m))
        if target == nums[m]:
            return m
        elif target > nums[m]:
            i = m + 1
        else:
            j = m - 1
```

##### 插值查找

算法简介

插值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的 查找方法，其核心就在于插值的计算公式 (key-a[low])/(a[high]-a[low])*(high-low)。 时间复杂度o(logn)但对于表长较大而关键字分布比较均匀的查找表来说，效率较高。

算法思想 基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。 注：对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多。反之，数组中如果分布非常不均匀，那么插值查找未必是很合适的选择。

复杂度分析 时间复杂性：如果元素均匀分布，则O（log log n）），在最坏的情况下可能需要O（n）。 空间复杂度：O（1）。

```
def binary_search(lis, key):
  low = 0
  high = len(lis) - 1
  time = 0
  while low < high:
    time += 1
    # 计算mid值是插值算法的核心代码
    mid = low + int((high - low) * (key - lis[low])/(lis[high] - lis[low]))
    print("mid=%s, low=%s, high=%s" % (mid, low, high))
    if key < lis[mid]:
      high = mid - 1
    elif key > lis[mid]:
      low = mid + 1
    else:
      # 打印查找的次数
      print("times: %s" % time)
      return mid
  print("times: %s" % time)
  return False

if __name__ == '__main__':
  LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
  result = binary_search(LIST, 444)
  print(result)
  
  
  list = [1,2,3,4,5,6,7,8]
  for k,i in enu(list):
     del(list[k])
     
```

#### 时间复杂度大O表示法

~~~
主要检测算法的快慢，操作效率
O(log n),对数时间，二分查找，一半
O(n)线性时间，有多少个执行多少次
O(1)一次找到比如字典
O(n²)

~~~



#### 9.git使用

~~~
1、查看所有分支

git branch -a

2、查看当前分支

git branch

3、如果有就直接提交，没有新建一个分支

git branch shijia

4、切换到新建分支上面

git checkout shijia
(写代码)

5、提交代码到本地缓存区

git add .

6、添加提交的代码备注

git commit -m "备注内容"

7、推送提交的代码到远程新建的分支上面

git push origin shijia:shijia

8、切换到主支

git checkout master

9、把分支代码merge到主分支
git merge shijia

10、合并分支到主支
git push origin master
~~~

#### 10.常用的状态码

~~~
HTTP状态码的英文为HTTP Status Code。下面是常见的HTTP状态码：

200 – 请求成功

301 – 资源(网页等)被永久转移到其它URL

404 – 请求的资源(网页等)不存在

500 – 内部服务器错误

HTTP状态码的分类

HTTP状态码由三个十进制数字组成，第一个十进制数字定义了状态码的类型，后两个数字没有分类的作用。HTTP状态码共分为5种类型：

分类分类描述

1**信息，服务器收到请求，需要请求者继续执行操作

2**成功，操作被成功接收并处理

3**重定向，需要进一步的操作以完成请求

4**客户端错误，请求包含语法错误或无法完成请求

5**服务器错误，服务器在处理请求的过程中发生了错误

HTTP状态码表(版本1) 此表含状态码英文名称

状态 码状态码英文名称中文描述

1开头的状态码

100Continue继续。客户端应继续其请求

101Switching Protocols切换协议。服务器根据客户端的请求切换协议。只能切换到更高级的协议，例如，切换到HTTP的新版本协议

2开头的状态码

200OK请求成功。一般用于GET与POST请求

201Created已创建。成功请求并创建了新的资源

202Accepted已接受。已经接受请求，但未处理完成

203Non-Authoritative Information非授权信息。请求成功。但返回的meta信息不在原始的服务器，而是一个副本

204No Content无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档

205Reset Content重置内容。服务器处理成功，用户终端(例如：浏览器)应重置文档视图。可通过此返回码清除浏览器的表单域

206Partial Content部分内容。服务器成功处理了部分GET请求

3开头的状态码

300Multiple Choices多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端(例如：浏览器)选择

301Moved Permanently永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。今后任何新的请求都应使用新的URI代替

302Found临时移动。与301类似。但资源只是临时被移动。客户端应继续使用原有URI

303See Other查看其它地址。与301类似。使用GET和POST请求查看

304Not Modified未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源

305Use Proxy使用代理。所请求的资源必须通过代理访问

306Unused已经被废弃的HTTP状态码

307Temporary Redirect临时重定向。与302类似。使用GET请求重定向

4开头的状态码

400Bad Request客户端请求的语法错误，服务器无法理解

401Unauthorized请求要求用户的身份认证

402Payment Required保留，将来使用

403Forbidden服务器理解请求客户端的请求，但是拒绝执行此请求

404Not Found服务器无法根据客户端的请求找到资源(网页)。通过此代码，网站设计人员可设置”您所请求的资源无法找到”的个性页面

405Method Not Allowed客户端请求中的方法被禁止

406Not Acceptable服务器无法根据客户端请求的内容特性完成请求

407Proxy Authentication Required请求要求代理的身份认证，与401类似，但请求者应当使用代理进行授权

408Request Time-out服务器等待客户端发送的请求时间过长，超时

409Conflict服务器完成客户端的PUT请求是可能返回此代码，服务器处理请求时发生了冲突

410Gone客户端请求的资源已经不存在。410不同于404，如果资源以前有现在被永久删除了可使用410代码，网站设计人员可通过301代码指定资源的新位置

411Length Required服务器无法处理客户端发送的不带Content-Length的请求信息

412Precondition Failed客户端请求信息的先决条件错误

413Request Entity Too Large由于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。如果只是服务器暂时无法处理，则会包含一个Retry-After的响应信息

414Request-URI Too Large请求的URI过长(URI通常为网址)，服务器无法处理

415Unsupported Media Type服务器无法处理请求附带的媒体格式

416Requested range not satisfiable客户端请求的范围无效

417Expectation Failed服务器无法满足Expect的请求头信息

5开头的状态码

500Internal Server Error服务器内部错误，无法完成请求

501Not Implemented服务器不支持请求的功能，无法完成请求

502Bad Gateway充当网关或代理的服务器，从远端服务器接收到了一个无效的请求

503Service Unavailable由于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的Retry-After头信息中

504Gateway Time-out充当网关或代理的服务器，未及时从远端服务器获取请求

505HTTP Version not supported服务器不支持请求的HTTP协议的版本，无法完成处理

HTTP状态码列表(版本2) 此表的描述更详细些

状态码含义

100客户端应当继续发送请求。这个临时响应是用来通知客户端它的部分请求已经被服务器接收，且仍未被拒绝。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。服务器必须在请求完成后向客户端发送一个最终响应。

101服务器已经理解了客户端的请求，并将通过Upgrade 消息头通知客户端采用不同的协议来完成这个请求。在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。

只有在切换新的协议更有好处的时候才应该采取类似措施。例如，切换到新的HTTP 版本比旧版本更有优势，或者切换到一个实时且同步的协议以传送利用此类特性的资源。

102由WebDAV(RFC 2518)扩展的状态码，代表处理将被继续执行。

200请求已成功，请求所希望的响应头或数据体将随此响应返回。

201请求已经被实现，而且有一个新的资源已经依据请求的需要而建立，且其 URI 已经随Location 头信息返回。假如需要的资源无法及时建立的话，应当返回 ‘202 Accepted’。

202服务器已接受请求，但尚未处理。正如它可能被拒绝一样，最终该请求可能会也可能不会被执行。在异步操作的场合下，没有比发送这个状态码更方便的做法了。
~~~

~~~
vue我用的版本是vue2,经常使用的框架有两个，一个是element ui,主要开发后台管理系统，一个是vant，主要做移动端开发。常用的就是form获取表单信息和table展示。对于一些头部可以进行
~~~

