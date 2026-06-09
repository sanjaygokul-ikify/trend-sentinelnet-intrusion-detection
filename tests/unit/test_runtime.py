import unittest
from packages.utils.metrics import get_runtime

class TestRuntime(unittest.TestCase):
    def test_get_runtime(self):
        runtime = get_runtime()
        self.assertGreaterEqual(runtime, 0)

if __name__ == '__main__':
    unittest.main()