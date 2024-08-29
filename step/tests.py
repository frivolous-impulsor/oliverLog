from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from .models import Step
from seed.models import Seed

# Create your tests here.
class StepTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(username='testuser',
                                                    email='test@gmail.com',
                                                    password='secret')
        self.seed = Seed.objects.create(author=self.user,
                                        seedName='Mr.Seed',
                                        content='seed Content')
        self.step = Step.objects.create(title='test Title',
                                        content='test Content',
                                        seed=self.seed)
        
    def test_step_list_view(self):
        seed_id = self.seed.id
        response = self.client.get(reverse('step_list', kwargs={'seed_id': seed_id}))
        self.assertEqual(response.status_code, 200)
    
    def test_step_create_view(self):
        seed_id = self.seed.id
        response = self.client.post(reverse('step_create', kwargs={'seed_id':seed_id}), {
            'title' : 'create title',
            'content' : 'create content',
            'seed' : self.seed
        })
        self.assertEqual(response.status_code, 302)
        

    def test_step_update_view(self):
        seed_id = self.seed.id
        response = self.client.post(reverse_lazy('step_update', kwargs={'seed_id':seed_id, 'pk':1}), {
            'title':'updated title',
            'content': 'updated content'
        })
        self.assertEqual(response.status_code, 302)

    def test_step_delete_view(self):
        seed_id = self.seed.id
        response = self.client.get(reverse('step_delete', kwargs={'seed_id':seed_id, 'pk':1}))
        self.assertEqual(response.status_code, 302)