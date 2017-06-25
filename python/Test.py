import mcp
import unittest


class TestMCP(unittest.TestCase):

    def setUp(self):
        pass

    def test_helloWorld(self):
        self.assertEqual(1, 1)

    def test_mcp(self):
        m = mcp.mcp()
        self.assertEqual(m.this_returns_one(), 1)

if __name__ == "__main__":
    unittest.main()
