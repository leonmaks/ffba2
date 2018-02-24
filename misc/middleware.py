from . import models as misc


class RootMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Код будет выполняться для каждого запроса
        # перед вызовом вью/контроллера (и затем промежуточного слоя).
        # В данном случае - инициируем глобальную переменную request.
        misc.Root.thread.request = request

        # Вызов вью/контроллера (и последующего промежуточного слоя).
        response = self.get_response(request)

        # Код будет выполняться после вызова вью/контроллера.
        # В данном случае:
        #      1) проверяем, установлена ли глобальная переменная request;
        #      2) если да, удаляем ее.
        if hasattr(misc.Root.thread, 'request'):
            del misc.Root.thread.request

        return response
