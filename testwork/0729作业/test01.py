"""
3.分析以下需求，并用代码实现
	1.定义一个方法equals(int[] arr1,int[] arr2),
	功能:比较两个数组是否相等(长度和内容均相等则认为两个数组是相同的)
	2.定义一个方法fill(int[] arr,int value),
	功能:将数组arr中的所有元素的值改为value
	3.定义一个方法fill(int[] arr,int fromIndex,int toIndex,int value),
	功能:将数组arr中的元素从索引fromIndex开始到toIndex(不包含toIndex)
		对应的值改为value
	4.定义一个方法copyOf(int[] arr, int newLength),
	功能:将数组arr中的newLength个元素拷贝到新数组中,并将新数组返回,从索引为0开始
	5.定义一个方法copyOfRange(int[] arr,int from, int to),
	功能:将数组arr中从索引from(包含from)开始到索引to结束(不包含to)的元素复制到新数组中,
	并将新数组返回
"""
def equals(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    index=0
    while (index<len(arr1)):
        if arr1[index] != arr2[index]:
            return False
        index += 1
    return True
arr1=[1,2,3,4,5]
arr2=[1,2,3,4]
#print(equals(arr1,arr2))

def fillone(list_data,value):
    index=0
    while (index<len(list_data)):
        list_data[index] = value
        index += 1
    print(list_data)
fillone(arr1,7)

def filltwo(list_data,fromIndex,toIndex,value):
    index=fromIndex
    while (index<toIndex):
        list_data[index] = value
        index += 1
    print(list_data)
filltwo(arr1,2,4,99)

def copyOf(list_data, newLength):
    new_list_data = []
    index=0
    while (index<newLength):
        new_list_data.append(list_data[index])
        index += 1
    return new_list_data







