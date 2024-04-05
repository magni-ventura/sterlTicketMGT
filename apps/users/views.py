from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class CreateUserView(View):
    def post(self, request):
        data = request.POST
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        is_staff = data.get('is_staff', False)
        is_superuser = data.get('is_superuser', False)

        try:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, is_staff=is_staff, is_superuser=is_superuser)
            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

