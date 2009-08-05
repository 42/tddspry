import tddspry
from django.conf import settings

class TestRemoveApp(tddspry.django.cases.DatabaseTestCase):
    settings.INSTALLED_APPS.append('test1')
    disabled_apps = ['test1']
    settings.TEST_DISABLED_APPS = []
    
    def setup(self):
        super(TestRemoveApp, self).setup()
        assert not 'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS
    
    def test_one(self):
        pass
        
    def teardown(self):
        super(TestRemoveApp, self).teardown()
        assert  'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS

class TestRemoveAppSettings(tddspry.django.cases.DatabaseTestCase):
    settings.INSTALLED_APPS.append('test1')
    settings.TEST_DISABLED_APPS = ['test1']

    def setup(self):
        super(TestRemoveAppSettings, self).setup()
        assert not 'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS

    def test_one(self):
        pass
        
    def teardown(self):
        super(TestRemoveAppSettings, self).teardown()
        assert  'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS

class TestRemoveAppBoth(tddspry.django.cases.DatabaseTestCase):
    settings.INSTALLED_APPS.append('test1')
    settings.INSTALLED_APPS.append('test2')
    settings.TEST_DISABLED_APPS = ['test1']
    disabled_apps = ['test2']

    def setup(self):
        super(TestRemoveAppBoth, self).setup()
        assert not 'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS
        assert not 'test2' in settings.INSTALLED_APPS, settings.INSTALLED_APPS

    def test_one(self):
        pass
        
    def teardown(self):
        super(TestRemoveAppBoth, self).teardown()
        assert  'test1' in settings.INSTALLED_APPS, settings.INSTALLED_APPS
        assert  'test2' in settings.INSTALLED_APPS, settings.INSTALLED_APPS
