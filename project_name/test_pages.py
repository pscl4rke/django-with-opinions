

from unittest.mock import patch

from django.test import TestCase, Client


class Test404(TestCase):

    def test_GET_unauthenticated(self):
        response = Client().get("/dsxwqrkvsry/")
        self.assertContains(response, "Not Found", status_code=404)


class Test500(TestCase):

    def test_GET_unauthenticated(self):
        client = Client()
        client.raise_request_exception = False
        from . import views
        with patch.object(views.LOG, "info") as function:
            function.side_effect = Exception("Example Error ciffewixlf")
            response = client.get("/")
        self.assertNotContains(response, "ciffewixlf", status_code=500)


class TestHome(TestCase):

    def test_GET_unauthenticated(self):
        response = Client().get("/")
        self.assertContains(response, "Hello World")
