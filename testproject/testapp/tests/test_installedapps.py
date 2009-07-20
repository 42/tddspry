import tddspry
from django.conf import settings

class TestRemoveApp(tddspry.django.cases.DatabaseTestCase):
    settings.INSTALLED_APPS.append('test1')
    remove_from_installedapps = ['test1']

    def setup(self):
        super(TestRemoveApp, self).setup()
        assert not 'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS

    def teardown(self):
        super(TestRemoveApp, self).teardown()
        assert  'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS

