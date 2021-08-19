from django.http import HttpResponse


class TestMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('hello this is before requesting view function')
        #return HttpResponse('<h1>Site under maintenance please visit after 1 hour</h1>')
        response = self.get_response(request) #trigger next phase
        print('hello this is after getting response')
        return response

    def process_exception(self, request,exception):
        return HttpResponse('<h1>Currently we are facing some technical problem{}</h1>'.format(exception))