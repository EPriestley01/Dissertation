from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_about (self):
        tester=app.test_client(self)
        response=tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_account(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_afterAmend(self):
        tester = app.test_client(self)
        response = tester.get('/wrkSplash', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_afterDelete(self):
        tester = app.test_client(self)
        response = tester.get('/nutSplash', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_afterOrder(self):
        tester = app.test_client(self)
        response = tester.get('/suppSplash', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_amendOrder(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_amendOrder(self):
        tester = app.test_client(self)
        response = tester.get('/keyError', content_type='html/text')
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()