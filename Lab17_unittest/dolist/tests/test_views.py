from django.test import TestCase
from django.urls import reverse
from dolist.forms import Todolistform
from dolist.models import Todolist
from dolist.views import addTodoitem, completedTodo, deleteCompleted, deleteAll

class TodoviewTestCase(TestCase):
    def setUp(self):
        self.task1 = Todolist.objects.create(text='Task 1', completed=False)
        self.task2 = Todolist.objects.create(text='Task 2', completed=False)
        self.task3 = Todolist.objects.create(text='Task 3', completed=True)
        
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_todo_item(self):
        response = self.client.post(reverse(addTodoitem), {'text': 'Task 4'})
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Todolist.objects.count(), 4)
        self.assertTrue(Todolist.objects.filter(text='Task 4').exists())

    def test_completed_todo_iew(self):
        response = self.client.post(reverse(addTodoitem), {'text': 'New Task', 'text': 'New Task 2'})
        self.assertEqual(response.status_code, 302) 


        self.assertTrue(Todolist.objects.count(), 5)

    def test_add_todo_item_invalid(self):
        response = self.client.post(reverse(addTodoitem), {'text': ''})
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Todolist.objects.count(), 3)

    def test_completed_todo_valid(self):
        response = self.client.post(reverse(completedTodo, args = [self.task1.id]))
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.completed)