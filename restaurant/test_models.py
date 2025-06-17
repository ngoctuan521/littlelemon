"""
sql commands:
CREATE DATABASE test_my_db;
GRANT ALL PRIVILEGES ON test_my_db.* TO 'root'@'%';
"""
from django.test import TestCase

from .models import Menu

class MenuTestCase(TestCase):
    def test_get_item(self):
        """Test the string representation of a menu item."""
        item = Menu.objects.create(title="Pizza", price=10, inventory=20)
        self.assertEqual(str(item), "Pizza: 10")

