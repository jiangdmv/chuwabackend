from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from product.models import PostProduct, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('product_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):

        self.test_category = Category.objects.create(name='Computer')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        data = {'name': 'new', 'description': 'test description', 'price': '3.33', 'quantity': '2', 'image': 'http://test.com', 'status': 'published'}
        url = reverse('product_api:listcreate')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


