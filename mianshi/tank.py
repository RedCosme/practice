#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'
# python version 2.7

from test import test_support
import unittest


class TankPosition(object):
    """
    坦克坐标用（x, y）表示，
    行进方向（W：西，E：东，N：北，S：南）
    其中向东向北，每100米坐标加1,
    x代表东西走向，y代表南北走向
    L和R分别表示左右转向
    T和P分别表示时间同步和位置校准
    M表示坦克行进100米
    """
    # 初始化坦克状态
    def __init__(self, x, y, first_direction):
        self.x = x
        self.y = y
        self.direction = first_direction

    # 重写str方法
    def __str__(self):
        return "当前坦克的位置为：({},{}),坦克的行进方向为：{}".format(self.x, self.y, self.direction)

    # 移动坦克
    def move_tank(self):
        # 向西走-1
        if self.direction == 'W':
            self.x -= 1
        # 向东走+1
        elif self.direction == 'E':
            self.x += 1
        # 向北走+1
        elif self.direction == 'N':
            self.y += 1
        # 向南走-1
        elif self.direction == 'S':
            self.y -= 1

    # 左转
    def turn_left(self):
        # 西向左转南
        if self.direction == 'W':
            self.direction = 'S'
        # 东向左转北
        elif self.direction == 'E':
            self.direction = 'N'
        # 北向左转西
        elif self.direction == 'N':
            self.direction = 'W'
        # 南向左转东
        elif self.direction == 'S':
            self.direction = 'E'

    # 右转
    def turn_right(self):
        # 西向右转北
        if self.direction == 'W':
            self.direction = 'N'
        # 东向右转南
        elif self.direction == 'E':
            self.direction = 'S'
        # 北向右转东
        elif self.direction == 'N':
            self.direction = 'E'
        # 南向右转西
        elif self.direction == 'S':
            self.direction = 'W'
        else:
            pass

    # 同步时间
    def sync_time(self):
        pass

    # 校准位置
    def stand_position(self):
        pass


# 主程序
def main(x, y, direction, singles):
    # 定义坦克的方向
    base_direction = ['W', 'E', 'N', 'S']
    # 获取坦克初始位置
    # 转换数据类型进行异常捕获
    try:
        x = int(x)
        y = int(y)
    except Exception as e:
        print "坐标输入格式不正确，请重新输入！"

    # 获取坦克的初始行进方向
    direction = str(direction).upper()
    if direction in base_direction:
        pass
    else:
        print "请输入正确的行进方向（W：西，E：东，N：北，S：南）"
    # 实例化坦克对象
    tank = TankPosition(x, y, direction)
    if singles:
        # 遍历信号内容
        for single in singles:
            # 修改坦克坐标
            if single == 'M':
                tank.move_tank()
            # 坦克左转
            elif single == 'L':
                tank.turn_left()
            # 坦克右转
            elif single == 'R':
                tank.turn_right()
            # 时间同步
            elif single == 'T':
                tank.sync_time()
            # 校准坦克位置
            elif single == 'P':
                tank.stand_position()
            else:
                continue
        print tank
        return tank


class TankTestCase(unittest.TestCase):

    def testTankPostion(self):
        x = 11
        y = 39
        direction = 'W'
        singles = 'MTMPRPMTMLMRPRMTPLMMTLMRRMP'
        ret = main(x, y, direction, singles)
        self.assertEqual(ret.x, 9)
        self.assertEqual(ret.y, 43)
        self.assertEqual(ret.direction, 'E')


def test_main():
    test_support.run_unittest(TankTestCase)


if __name__ == '__main__':
    test_main()
    main(11, 39, 'w', 'MTMPRPMTMLMRPRMTPLMMTLMRRMP')
