#写单元测试
import unittest

from doMounttab import parse_mounts

class TestMount(unittest.TestCase):
    def test_mount(self):
        result = parse_mounts()
        self.assertIsInstance(result,list)
        self.assertIsInstance(result[0],tuple)
    
    def test_root(self):
        result = parse_mounts()
        for x in result:
            if x[1] == '/' and x[2] != 'rootfs':
                self.assertEqual(x[2],'ext4')

unittest.main()
