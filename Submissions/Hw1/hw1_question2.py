# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:55:29 2018

@author: ron
"""


def check_palindrome():
    # Check last four digits of num
    def cond_1(num):
        num_str = str(num)
        return num_str[2:] == num_str[5:1:-1]

    # Check last five digits of num+1
    def cond_2(num):
        cond_num = num + 1
        num_str = str(cond_num)
        return num_str[1:] == num_str[5:0:-1]

    # Check middle digits of num+2
    def cond_3(num):
        cond_num = num + 2
        num_str = str(cond_num)
        return num_str[1:5] == num_str[4:0:-1]

    # Check all digits of num+3
    def cond_4(num):
        cond_num = num + 3
        num_str = str(cond_num)
        return num_str == num_str[::-1]

    test_conditions = [cond_1, cond_2, cond_3, cond_4]
    for n in range(100000, 1000000):
        if all([test(n) for test in test_conditions]):
            print(n)


if __name__ == '__main__':
    check_palindrome()
