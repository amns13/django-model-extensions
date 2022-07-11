from datetime import timedelta
from unittest import mock

from django.test import TestCase
from django.utils import timezone

from .testapp.models import CreatedUpdatedTimestampTestModel


class TestCreateUpdateTimestampModel(TestCase):
    """
    Test cases for CreatedUpdatedTimeStampModel
    Mocking for auto_now, auto_now_add fields. Refer from below link:
    https://dev.to/serhatteker/testing-createdupdatedautonow-fields-in-django-139k
    """

    def setUp(self) -> None:
        self.mocked_time_now = timezone.now()
        self.mocked_time_past = timezone.now() - timedelta(days=1)

    @mock.patch("django.utils.timezone.now")
    def test_created_at_last_updated_at_is_now_on_create(self, mock_now):
        """
        Test created_at, last_updated_at is equal to current timestamp
        when a new object created.
        """
        mock_now.return_value = self.mocked_time_now
        obj = CreatedUpdatedTimestampTestModel.objects.create()
        self.assertEqual(obj.created_at, self.mocked_time_now)
        self.assertEqual(obj.last_updated_at, self.mocked_time_now)

    @mock.patch("django.utils.timezone.now")
    def test_last_updated_at_is_now_on_update(self, mock_now):
        """
        Test last_updated_at is equal to current timestamp
        when an existing object is updated.
        """
        mock_now.return_value = self.mocked_time_past
        obj = CreatedUpdatedTimestampTestModel.objects.create()
        mock_now.return_value = self.mocked_time_now
        obj.save()
        self.assertEqual(obj.created_at, self.mocked_time_past)
        self.assertEqual(obj.last_updated_at, self.mocked_time_now)


class TestUpdateQueryOnCreatedUpdatedTimeStampModel(TestCase):
    """Test Cases for CreateUpdateTimestampManager"""

    def setUp(self) -> None:
        self.object_count = 3
        for _ in range(self.object_count):
            CreatedUpdatedTimestampTestModel.objects.create()

        self.mocked_update_time = timezone.now() + timedelta(days=1)

    @mock.patch("django.utils.timezone.now")
    def test_last_updated_at_is_now_on_running_update_query(self, mock_now):
        """
        Test last_updated_at is equal to current timestamp when update query is run.
        Test created_at is not updated.
        """
        mock_now.return_value = self.mocked_update_time
        update_result = CreatedUpdatedTimestampTestModel.objects.update()
        self.assertEqual(update_result, self.object_count)

        test_objects = CreatedUpdatedTimestampTestModel.objects.all()
        for obj in test_objects:
            self.assertNotEqual(obj.created_at, self.mocked_update_time)
            self.assertEqual(obj.last_updated_at, self.mocked_update_time)
