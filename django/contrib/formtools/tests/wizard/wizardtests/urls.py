from django.conf.urls import patterns, url
from django.contrib.formtools.tests.wizard.wizardtests.forms import (
    SessionContactWizard, CookieContactWizard, Page1, Page2, Page3, Page4)

from django.contrib.formtools.tests.wizard.wizardtests.forms import (
    RevalidationWizard, EmptyPage1, EmptyPage2, EmptyPage3)

urlpatterns = patterns('',
    url(r'^wiz_session/$', SessionContactWizard.as_view(
        [('form1', Page1),
         ('form2', Page2),
         ('form3', Page3),
         ('form4', Page4)])),
    url(r'^wiz_cookie/$', CookieContactWizard.as_view(
        [('form1', Page1),
         ('form2', Page2),
         ('form3', Page3),
         ('form4', Page4)])),
     url(r'^wiz_other_template/$', CookieContactWizard.as_view(
         [('form1', Page1),
          ('form2', Page2),
          ('form3', Page3),
          ('form4', Page4)],
          template_name='other_wizard_form.html')),
    url(r'^wiz_revalidation/$', RevalidationWizard.as_view(
        [('form1', EmptyPage1),
         ('form2', EmptyPage2),
         ('form3', EmptyPage3)])),
)
