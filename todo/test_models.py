from django.test import TestCase
from .models import item

class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        Item = item(name="Create a Test")
        Item.save()
        self.assertEqual(Item.name, "Create a Test")
        self.assertFalse(Item.done)
        
    def test_can_create_an_item_with_a_name_and_status(self):
        Item=item(name="Create a Test", done=True)
        Item.save()
        self.assertEqual(Item.name, "Create a Test")
        self.assertTrue(Item.done)
        
    def test_item_as_a_string(self):
        Item = item(name = "Create a Test")
        self.assertEqual("Create a Test", str(Item))