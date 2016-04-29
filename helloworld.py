import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = 'text/plain'
        self.response.write('Hello, CircleCI!')

class ChildPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = 'text/plain'
        self.response.write('Hello, Child!')


app = webapp2.WSGIApplication([
    ('/', MainPage),('/child', ChildPage),
], debug = True)

