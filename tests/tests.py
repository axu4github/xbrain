# coding=utf-8

import unittest
import sys


class TestPythonEnv(unittest.TestCase):
    """ 测试Python运行环境 """

    def test_python_version(self):
        """ python3以上版本 """
        self.assertTrue(sys.version.startswith("3"))


if __name__ == "__main__":
    unittest.main()
