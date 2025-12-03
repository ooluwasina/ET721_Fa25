from django.urls import reverse, resolve
from django.test import TestCase
from dolist.views import index, addTodoitem, completedTodo
from dolist.models import Todolist

class TestUrls(TestCase):
    def test_index_urls(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)


    def test_add_urls(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func, addTodoitem)

    def test_completed_urls(self):
        url = reverse('completed', args=[1])
        self.assertEqual(resolve(url).func, completedTodo)

    def test_urls_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)       

        response =  self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 405)

        