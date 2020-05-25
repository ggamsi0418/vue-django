import unittest
import json
from django.test import Client


class BlogAppTest(unittest.TestCase):

    def test_post_list(self):
        client = Client()

        res = client.get('/blog/post/list/')
        print(res)
        contents = res.context_data['object_list']
        print(contents)