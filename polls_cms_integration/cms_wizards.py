from cms.utils.urlutils import admin_reverse
from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import PollWizardForm


class PollWizard(Wizard):
    # FIXME: better would be to add choices to the PollWizardForm, and return
    # None here (to say on whatever page the user clicked the Create btn on)
    def get_success_url(self, poll, **kwargs):
        return admin_reverse('polls_poll_change', args=(poll.pk,))


poll_wizard = PollWizard(
    title='Poll',
    weight=200,
    form=PollWizardForm,
    description='Create a new Poll'
)

wizard_pool.register(poll_wizard)
