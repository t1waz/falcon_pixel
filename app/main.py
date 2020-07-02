import falcon


app = falcon.API()


class HelloResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = 'hello'


hello_resource = HelloResource()

app.add_route('/hello', hello_resource)

