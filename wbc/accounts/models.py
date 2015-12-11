# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Permission, Group
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from wbc.stakeholder.models import Stakeholder
from wbc.projects.slug import unique_slugify


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User)

    info        = models.TextField(blank=True, help_text=_('Say something about yourself'))
    twitter     = models.CharField(max_length=256, blank=True, help_text=_('Your twitter nick'))
    stakeholder = models.OneToOneField(Stakeholder, blank=True, null=True, help_text="Öffentliches Profil", editable=False)

    @property
    def full_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        else:
            return self.user.username

    def get_fields(self):
        return [field.name for field in self._meta.fields if field.name not in ['id', 'user', 'stakeholder']]

    def as_dict(self):
        return {field: getattr(self, field) for field in self.get_fields()}

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('user',)

        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


def create_profile_for_user(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user.groups.add(Group.objects.get(name='user'))
        profile = Profile()
        profile.user = user
        profile.save()
        stakeholder = Stakeholder(name=profile.full_name)    
        stakeholder.save()
        profile.stakeholder = stakeholder
        profile.save()

post_save.connect(create_profile_for_user, sender=User)
