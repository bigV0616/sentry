# -*- coding: utf-8 -*-

from __future__ import absolute_import

import six

from sentry.api.serializers import serialize
from sentry.api.serializers.models.project import (
    ProjectWithOrganizationSerializer, ProjectWithTeamSerializer
)
from sentry.testutils import TestCase


class ProjectSerializerTest(TestCase):
    def test_simple(self):
        user = self.create_user(username='foo')
        organization = self.create_organization(owner=user)
        team = self.create_team(organization=organization)
        project = self.create_project(team=team, organization=organization, name='foo')

        result = serialize(project, user)

        assert result['slug'] == project.slug
        assert result['name'] == project.name
        assert result['id'] == six.text_type(project.id)


class ProjectWithTeamSerializerTest(TestCase):
    def test_simple(self):
        user = self.create_user(username='foo')
        organization = self.create_organization(owner=user)
        team = self.create_team(organization=organization)
        project = self.create_project(team=team, organization=organization, name='foo')

        result = serialize(project, user, ProjectWithTeamSerializer())

        assert result['slug'] == project.slug
        assert result['name'] == project.name
        assert result['id'] == six.text_type(project.id)
        assert result['team'] == serialize(team, user)


class ProjectWithOrganizationSerializerTest(TestCase):
    def test_simple(self):
        user = self.create_user(username='foo')
        organization = self.create_organization(owner=user)
        team = self.create_team(organization=organization)
        project = self.create_project(team=team, organization=organization, name='foo')

        result = serialize(project, user, ProjectWithOrganizationSerializer())

        assert result['slug'] == project.slug
        assert result['name'] == project.name
        assert result['id'] == six.text_type(project.id)
        assert result['organization'] == serialize(organization, user)
