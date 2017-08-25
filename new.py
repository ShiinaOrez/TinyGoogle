#!/usr/bin/env python
# encoding: utf-8
str py=("ling","yi","er","san","si","wu","liu","qi","ba","jiu")
int arr=[]
int sum=0

class Read() :
    def __init__(self,num) :
        self.num = int(num)
        self.sumup = 0

    def sum_up(self) :
        while number!=0:
            int a=number%10
            int b=number/10
            sum+=a
            number=b
        print(sum)    
        pass

    def print_it(self) :
    	int ss=sum,i=0;
        while ss!=0:
            i++
            int a=ss%10
            int b=ss/10
            arr[i]=a
            ss=b
        while i>0:
            print(py[i] )
            i--
        pass   

    def change(self) :
    	int tool=1,i=1
        while tool<sum:
            tool*=7
        tool/=7
        while tool>0:
            int a=sum%tool
            int b=sum/tool
            print(b)
            sum =a 
        pass

if __name__ == '__main__' :
    number = Read(input("输入一个尽可能长的数字\n"))
    number.sum_up()
    number.print_it()
    number.change()
