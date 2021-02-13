from test_onepo.page.app import App


class TestCase:
    def test_case(self):
        app = App()
        app.start().main().goto_search()