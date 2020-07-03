import falcon
import constants


app = falcon.API()


class HelloResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = 'hello'


class VerifyResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = constants.VERIFY_TOKEN


hello_resource = HelloResource()
verify_resource = VerifyResource()


app.add_route('/hello', hello_resource)
app.add_route(f'/{constants.VERIFY_TOKEN}.txt', verify_resource)


