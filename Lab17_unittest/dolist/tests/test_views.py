from django.test import TestCase
from django.urls import reverse
from .models import Todolist
from .forms import Todolistform
from .views import addTodoitem, completedTodo, deleteCompleted, deleteAll

class TodoviewTestCase(TestCase):
    def setUp(self):
        self.task1 = Todolist.objects.create(text='Task 1', completed=False)
        self.task2 = Todolist.objects.create(text='Task 2', completed=False)
        self.task3 = Todolist.objects.create(text='Task 3', completed=True)
        
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')