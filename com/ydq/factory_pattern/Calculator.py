#coding=utf-8
'''
An easy instance of factory-pattern, by implementing a simple calculator.
'''
from abc import ABCMeta, abstractmethod

class OperationFactory:
    def creatOpteration(self, op, num_A, num_B):
        newOp = {
            '+' : OperationAdd(num_A, num_B),
            '-' : OperationSubtract(num_A, num_B),
            '*' : OperationMultiply(num_A, num_B),
            '/' : OperationEliminate(num_A, num_B)
        }.get(op)
        if(newOp == None) :
            raise Exception('不支持的计算!')
        return newOp

#parent class of calculator operations
class Operation:
    num_A = 0.0
    num_B = 0.0

    def __init__(self, a, b):
        self.num_A = a
        self.num_B = b

    @abstractmethod
    def calulator(self):
        pass

class OperationAdd(Operation) :
    def calulator(self):
        return self.num_A + self.num_B

class OperationSubtract(Operation):
    def calulator(self):
        return self.num_A - self.num_B

class OperationMultiply(Operation):
    def calulator(self):
        return self.num_A * self.num_B

class OperationEliminate(Operation):
    def calulator(self):
        if(self.num_B == 0):
            raise Exception('除数不能为0!')
        return self.num_A / self.num_B

class Calculator:
    def main(self=None):
        str = raw_input('请输入计算式(空格分隔)：\n')
        nums = str.split(" ")
        if(len(nums) != 3):
            raise Exception('输出格式错误!')
        op = OperationFactory().creatOpteration(nums[1], float(nums[0]), float(nums[2]))
        result = op.calulator()
        print ('结算结果为：{0} = {1}'.format(str, result) )

    if __name__ == '__main__':
        main()