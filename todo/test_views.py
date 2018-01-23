from django.test import TestCase
from .models import item
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    def test_get_home_page(self):
        page=self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
        
    def test_get_add_item_page(self):
        page=self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    def test_get_edit_item_page(self):
        Item=item(name='Create a Test')
        Item.save()
        
        page=self.client.get("/edit/{0}".format(Item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    def test_get_edit_page_for_item_that_does_not_exit(self):
        page=self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        Item = get_object_or_404(item, pk=1)
        self.assertEqual(Item.done, False)
        
    def test_post_edit_an_item(self):
        Item=item(name="Create a Test")
        Item.save()
        
        id = Item.id
        
        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        Item = get_object_or_404(item, pk=1)
        
        self.assertEqual("A different name", Item.name)
        
    def test_toggle_status(self):
        Item=item(name="Create a Test")
        Item.save()
        id = Item.id
        
        response = self.client.post("/toggle/{0}".format(id))
        
        Item = get_object_or_404(item, pk=id)
        self.assertEqual(Item.done, True)
        