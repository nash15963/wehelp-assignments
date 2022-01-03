# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 09:52:30 2022

@author: nash1
"""

#1
def calculate(min, max):
    num_array = []
    for i in range(min,max+1):
        num = i
        num_array.append(num)
    print(sum(num_array))
# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#2
def avg(data):
    # 請用你的程式補完這個函式的區塊
    sal_array = []
    for i in range(len(data["employees"])):
        #print(data["employees"][i]['salary'])
        sal = data["employees"][i]['salary']
        sal_array.append(sal)
    print(sum(sal_array)/len(data["employees"]))

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


#3
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    new = sorted(nums ,reverse = True)
    big = new[0]*new[1]
    print(big)
    
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0

#4.
def twoSum(nums, target):
    #假設兩兩相加且元素位置不重複算法
    temp_array =[]
    # your code here
    for i in range(len(nums)):
        for j in range(len(nums)):
             if nums[i]+nums[j] == target:
                 temp = i
                 temp_array.append(temp)
    return temp_array
                    
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

result=twoSum([5, 20, 1, 2], 3)
print(result) # show [2, 3] because nums[2]+nums[3] is 3


def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    temp = 0
    big =0
    for i in range(len(nums)):
        if nums[i] == 0:
            temp +=1
            if big<temp:
                big = temp
        else:
            temp = 0
    print(big)
    
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3










