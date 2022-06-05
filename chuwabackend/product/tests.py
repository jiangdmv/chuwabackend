from django.test import TestCase
from django.contrib.auth.models import User
from product.models import PostProduct, Category

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        test_post = PostProduct.objects.create(category_id=1, name='test1', description='test description', price='3.33', quantity='2', image='http://test.com', status='published')

    def test_product_content(self):
        post = PostProduct.postobjects.get(id=1)
        cat = Category.objects.get(id=1)

        name = f'{post.name}'
        description = f'{post.description}'
        price = f'{post.price}'
        quantity = f'{post.quantity}'
        image = f'{post.image}'
        status = f'{post.status}'

        self.assertEqual(name, 'test1')
        self.assertEqual(description, 'test description')
        self.assertEqual(price, '3.33')
        self.assertEqual(quantity, '2')
        self.assertEqual(image, 'http://test.com')
        self.assertEqual(status, 'published')

        self.assertEqual(str(PostProduct), 'test1:$3.33')
        self.assertEqual(str(cat), 'Computer')






