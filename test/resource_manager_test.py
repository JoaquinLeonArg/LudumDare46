import unittest
from resources.manager import ResourceManager

class TestResourceManager(unittest.TestCase):
    
    def test_resources_exist(self):
        for _, resources in ResourceManager.resources.items():
            self.assertGreater(len(resources), 0)

if __name__ == "__main__":
    unittest.main()