from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    #Testing to check if name exist in the web page
    def test_name_exists(self):
        response = Client().get('/main/')
        self.assertContains(response, response.context["nama"])

    #Testing to check if class name exist in the web page
    def test_class_exists(self):
        response = Client().get('/main/')
        self.assertContains(response, response.context["kelas"])