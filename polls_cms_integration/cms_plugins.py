from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import PollPluginModel


class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel
    module = _('Polls')  # section header (label in UI) of the plugin
    name = _('Poll')  # name (label in UI) of the plugin
    render_template = 'polls_cms_integration/poll_plugin.html'

    def render(self, context, instance, placeholder):
        # instance will be an instance of self.model (ie PollPluginModel)
        context.update({'poll': instance.poll})
        return context

plugin_pool.register_plugin(PollPluginPublisher)
