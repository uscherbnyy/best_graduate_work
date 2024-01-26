from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


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


def listusers(request):
    '''
    На вывод всех пользователей
    :param reqest:
    :return:
    '''

    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'listusers.html', context)


def user_selection(request):
    '''
    перенаправляет на список всех пользователей с возможностью перехода на каждого по отдельности.
    :param request:
    :return:
    '''

    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user_selection.html', context)


def user_detail(request, user_id):
    """

    Выводит конкретного пользователя
    :param request:
    :param user_id:
    :return:
    """

    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user
    }
    return render(request, 'user_detail.html', context)


def destroy(self, request):
    pass
    # user = self.get_object()
    # if request.user.is_superuser:  # Предполагаем, что админ может удалять жестко
    #     user.delete()
    # else:
    #     user.is_active = False  # Предполагаем, что мягкое удаление ставит пользователя неактивным
    #     user.save()
    #
    # return redirect('user_selection.html')


def update(request):
    pass
