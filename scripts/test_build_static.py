from build_static import HTMLTouchUp
from unittest import (TestCase, TestSuite, TextTestRunner)

class HTMLTouchUpTestCase(TestCase):
    def setUp(self):
        self.parser = HTMLTouchUp()

    def test_HTMLTouchUp_PassRegularTag_ExpectEcho(self):
        self.parser.feed("<div class='1'><p class='2'>Hi</p></div>")
        self.assertEqual(
            self.parser.return_html(), 
            '<div class="1"><p class="2">Hi</p></div>'
        )
    
    def test_HTMLTouchUp_PassSelfClosingTag_ExpectReplacement(self):
        self.parser.feed("<div class='1'><script src='../dist/bundle.js'/></div>")
        self.assertEqual(
            self.parser.return_html(),
            '<div class="1"><script src="index.js"/></div>'
        )     

def make_test_suite():
    suite = TestSuite()
    suite.addTest(HTMLTouchUpTestCase("test_HTMLTouchUp_PassRegularTag_ExpectEcho"))
    suite.addTest(HTMLTouchUpTestCase("test_HTMLTouchUp_PassSelfClosingTag_ExpectReplacement"))
    return suite

if __name__ == '__main__':
    test_suite = make_test_suite()
    TextTestRunner(verbosity=2).run(test_suite)