from django.utils.functional import cached_property
from rest_base.models import BaseUser, BaseToken


class User(BaseUser):
    @cached_property
    def attribute(self) -> dict:
        return dict(
            user_id=self.user_id,
            username=self.username,
        )


class Token(BaseToken):
    pass
