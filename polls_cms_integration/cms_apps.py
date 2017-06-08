from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .cms_menus import PollsMenu


class PollsApphook(CMSApp):
    app_name = 'polls'
    name = _('Polls Application')

    # when this app is attached to a page, also automatically attach menus
    def get_menus(self, page=None, language=None, **kwargs):
        return [PollsMenu]

    def get_urls(self, page=None, language=None, **kwargs):
        return ['polls.urls']

apphook_pool.register(PollsApphook)
