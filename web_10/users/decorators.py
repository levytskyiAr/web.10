from django.shortcuts import redirect

def user_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            # Якщо користувач не аутентифікований, перенаправляємо його на сторінку входу
            return redirect('login')  # Замініть 'login' на ім'я вашого URL шляху для сторінки входу
    return wrapper
