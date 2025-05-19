# profiles/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import ProfileForm

User = get_user_model()

class ProfileTests(TestCase):
    def setUp(self):
        # Cria um usuário para os testes
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
            email='testuser@example.com'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertContains(response, 'User')

    def test_profile_edit_get(self):
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_profile_edit_post_valid(self):
        response = self.client.post(reverse('profile_edit'), {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_profile_edit_post_invalid(self):
        response = self.client.post(reverse('profile_edit'), {
            'first_name': '',
            'last_name': '',
            'email': 'invalidemail'
        })
        self.assertEqual(response.status_code, 200)

        # Extrai o formulário do contexto da resposta
        form = response.context.get('form')
        self.assertIsInstance(form, ProfileForm)

        # Imprime os erros para diagnóstico
        print("Form errors:", form.errors)

        # Verifica os erros do formulário diretamente
        self.assertTrue(form.errors)
        self.assertIn('first_name', form.errors, "Erro 'first_name' não encontrado.")
        self.assertIn('last_name', form.errors, "Erro 'last_name' não encontrado.")
        self.assertIn('email', form.errors, "Erro 'email' não encontrado.")
        self.assertEqual(form.errors.get('first_name'), ['This field is required.'])
        self.assertEqual(form.errors.get('last_name'), ['This field is required.'])
        self.assertEqual(form.errors.get('email'), ['Enter a valid email address.'])