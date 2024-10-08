from unittest import skip

from django.test import TestCase
from django.utils import timezone

from core.models import (
    Skill,
    Project,
    JobExperience,
    Education,
    Interest,
    Certificate,
)
from utils.base_model_test import BaseModelTestCase


class SkillModelTestCase(BaseModelTestCase, TestCase):
    model = Skill
    fields = {
        "name": "python",
        "logo": None,
        "priority": 1,
    }
    fields_2 = {
        "name": "django",
        "logo": None,
        "priority": 2,
    }

    def test_ordering(self):
        instance1 = self.model._default_manager.create(**self.fields)
        instance2 = self.model._default_manager.create(**self.fields_2)
        instances = self.model._default_manager.all()
        self.assertEqual(list(instances), [instance1, instance2])


class ProjectModelTestCase(BaseModelTestCase, TestCase):
    model = Project

    fields = {
        "name": "RPC",
        "source_link": "www.example.com",
        "live_link": None,
        "description": "TEST PROJECT",
        "status": "Ongoing",
    }
    fields_2 = {
        "name": "RPC_2",
        "source_link": "www.example2.com",
        "live_link": None,
        "description": "TEST PROJECT2",
        "status": "Ongoing",
    }


class JobExperienceModelTestCase(BaseModelTestCase, TestCase):
    model = JobExperience
    fields = {
        "company_name": "Digitoon",
        "position": "Back end developer",
        "start_date": timezone.datetime(2020, 1, 1),
    }
    fields_2 = {
        "company_name": "Digitoon",
        "position": "DevOps engineer",
        "start_date": timezone.datetime(2021, 1, 1),
    }

    def test_ordering(self):
        instance1 = self.model._default_manager.create(**self.fields)
        instance2 = self.model._default_manager.create(**self.fields_2)
        instances = self.model._default_manager.all()
        self.assertEqual(list(instances), [instance2, instance1])

    def test_str_representation(self):
        instance = self.model(**self.fields)
        self.assertEqual(str(instance), instance.company_name + " " + instance.position)

    @skip
    def test_years_of_experience_property(self):
        # TODO years_of_experience bug should be fixed

        instance1 = self.model._default_manager.create(
            company_name="test",
            position="Test position",
            start_date=timezone.datetime(2019, 8, 1),
            end_date=timezone.datetime(2020, 1, 11),
        )
        self.assertEqual(instance1.years_of_experience, 1)


class EducationModelTestCase(BaseModelTestCase, TestCase):
    model = Education
    fields = {
        "university_name": "Test university",
        "degree": "bachelor",
        "start_date": timezone.datetime(2020, 1, 1),
    }
    fields_2 = {
        "university_name": "Test university 2 ",
        "degree": "bachelor",
        "start_date": timezone.datetime(2023, 2, 2),
    }

    def test_str_representation(self):
        instance = self.model(**self.fields)
        self.assertEqual(
            str(instance), instance.university_name + " " + instance.degree
        )


class InterestModelTestCase(BaseModelTestCase, TestCase):
    model = Interest
    fields = {
        "name": "game",
    }
    fields_2 = {
        "name": "game2",
    }


class CertificateModelTestCase(BaseModelTestCase, TestCase):
    model = Certificate
    fields = {
        "name": "Python course",
    }
    fields_2 = {
        "name": "django course",
    }
