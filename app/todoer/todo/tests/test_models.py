from datetime import datetime, timezone
from freezegun import freeze_time
from django.test import TestCase
from todo.models import Todo


class TodoTest(TestCase):
    def _build_simple_todo(self, **kwargs):
        if 'title' not in kwargs:
            kwargs['title'] = 'my test todo'
        todo = Todo(**kwargs)
        todo.save()
        return todo

    def test_string_representation(self):
        todo = self._build_simple_todo()
        self.assertEqual(todo.title, str(todo))

    @freeze_time('2017-01-01')
    def test_default_value(self):
        todo = self._build_simple_todo()
        self.assertEqual(todo.status, Todo.PENDING)
        self.assertEqual(todo.created_at, datetime.now(timezone.utc))
        self.assertEqual(todo.comment, '')
