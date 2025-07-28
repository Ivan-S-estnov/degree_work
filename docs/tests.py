from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from docs.models import Course, Lesson, Checkout
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            name="test_course",
            description="test_description",
        )
        self.lesson = Lesson.objects.create(name="test_lesson", course=self.course)
        self.checkout = Checkout.objects.create(
            lesson=self.lesson,
            question="test_question",
            answer_first="test_answer_first",
            answer_second="test_answer_second",
            answer_third="test_answer_third",
            right_answer="test_right_answer",
        )

        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("docs:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test_course")

    def test_course_create(self):
        url = reverse("docs:course-list")
        data = {"name": "Курс1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_update(self):
        url = reverse("docs:course-detail", args=(self.course.pk,))
        data = {"description": "курс тестирования для самообучения"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("description"), "курс тестирования для самообучения")

    def test_course_delete(self):
        url = reverse("docs:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse("docs:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "name": self.course.name,
                    "description": self.course.description,
                    "owner": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            name="test_course", description="test_description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="test_lesson",
            description="test_lesson_description",
            course=self.course,
            owner=self.user,
        )
        self.checkout = Checkout.objects.create(
            lesson=self.lesson,
            question="test_question",
            answer_first="test_answer_first",
            answer_second="test_answer_second",
            answer_third="test_answer_third",
            right_answer="test_right_answer",
        )

        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("docs:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test_lesson")

    def test_lesson_create(self):
        result = {
            "name": "Урок первый",
            "description": "Введение",
            "course": {
                "id": 1,
                "name": "Курс тестовый",
                "description": "Обобщенный",
                "owner": 1,
            },
            "owner": 1,
        }
        url = reverse("docs:lesson_build")
        data = result
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):
        url = reverse("docs:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Урок3"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Урок3")

    def test_lesson_delete(self):
        url = reverse("docs:lesson_destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("docs:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "course": {
                        "id": self.course.id,
                        "name": self.course.name,
                        "description": self.course.description,
                        "owner": 1,
                    },
                    "owner": 1,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class CheckoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="newone@forcheck.org")
        self.course = Course.objects.create(
            name="test_course", description="test_description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="test_lesson", course=self.course, owner=self.user
        )
        self.checkout = Checkout.objects.create(
            lesson=self.lesson,
            question="test_question",
            answer_first="test_answer_first",
            answer_second="test_answer_second",
            answer_third="test_answer_third",
            right_answer="test_right_answer",
        )
        self.client.force_authenticate(user=self.user)

    def test_checkout_retrieve(self):
        url = reverse("docs:test_retrieve", args=(self.checkout.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("question"), "test_question")

    def test_checkout_create(self):
        url = reverse("docs:create_test")
        data = {
            "lesson": {
                "name": "Урок первый",
                "description": "Введение",
                "course": {
                    "id": 1,
                    "name": "Курс тестовый",
                    "description": "Обобщенный",
                    "owner": 1,
                },
                "owner": 1,
            },
            "question": "Проверочный вопрос",
            "answer_first": "первый ответ",
            "answer_second": "ответ номер два",
            "answer_third": "ответ третий",
            "right_answer": "good choose",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_checkout_update(self):
        url = reverse("docs:update_test", args=(self.checkout.pk,))
        data = {"answer_first": "Верный ответ"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("answer_first"), "Верный ответ")

    def test_checkout_delete(self):
        url = reverse("docs:destroy_test", args=(self.checkout.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Checkout.objects.all().count(), 0)

    def test_checkout_list(self):
        url = reverse("docs:test_list")
        response = self.client.get(url)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "lesson": {
                        "name": self.lesson.name,
                        "description": self.lesson.description,
                        "course": {
                            "id": self.course.id,
                            "name": self.course.name,
                            "description": self.course.description,
                            "owner": 1,
                        },
                        "owner": 1,
                    },
                    "question": self.checkout.question,
                    "answer_first": self.checkout.answer_first,
                    "answer_second": self.checkout.answer_second,
                    "answer_third": self.checkout.answer_third,
                    "right_answer": self.checkout.right_answer,
                }
            ],
        }
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
