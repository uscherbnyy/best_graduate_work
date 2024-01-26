from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Проверяет аунтификацию
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        # Пользователь зарегистрирован и вошел в систему
        return render(request, 'home.html', {})
    else:
        # Пользователь не зарегистрирован или не вошел в систему
        return render(request, 'no_log.html', {})

