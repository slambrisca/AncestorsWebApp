from django.test import TestCase
from  ancestors.models import Person,Gender,IdType, File
from django.db.utils import IntegrityError


def createPerson(name="name",surname="surname",gender=Gender.NONE,id_type=IdType.DNI,id_number="1"):
    return Person(name=name,surname=surname,gender=gender,id_type=id_type,id_number=id_number)

class PersonTest(TestCase):


    def test_string_representation(self):
        mockedPerson = createPerson()
        self.assertEqual(str(mockedPerson),"name surname DNI:1")


    def test_save_person(self):
        mockedPerson = createPerson()
        try:
            mockedPerson.save()
        except IntegrityError:
            self.fail("Can not save mocked person: ValueError")

    def test_save_person_without_name(self):
        mockedPerson = createPerson(name=None)
        with self.assertRaises(IntegrityError):
            mockedPerson.save()

    def test_save_person_without_surname(self):
        mockedPerson = createPerson(surname=None)
        with self.assertRaises(IntegrityError):
            mockedPerson.save()

    def test_save_person_without_id_type(self):
        mockedPerson = createPerson(id_type=None)
        with self.assertRaises(IntegrityError):
            mockedPerson.save()

    def test_save_person_without_id_number(self):
        mockedPerson = createPerson(id_number=None)
        with self.assertRaises(IntegrityError):
            mockedPerson.save()

    def test_save_person_without_gender(self):
        mockedPerson = createPerson(gender=None)
        with self.assertRaises(IntegrityError):
            mockedPerson.save()

    def test_addFile(self):
        person = createPerson()
        person.save()
        file = person.addFile("path")

        self.assertEqual(person.getFiles(), [file])




class FileTest(TestCase):

    def test_string_representation(self):
        file = File(path="path")
        self.assertEqual(str(file),"path")

    def test_save_file(self):
        person = createPerson()
        person.save()
        file = File(person=person,path="path")
        try:
            file.save()
        except IntegrityError:
            self.fail("Can not save file: IntegrityError")

    def test_save_file_with_unsaved_person(self):
        file = File(person=createPerson(),path="")
        with self.assertRaises(ValueError):
            file.save()

    def test_save_file_without_person(self):
        file = File(path="")
        with self.assertRaises(IntegrityError):
            file.save()

    def test_getPath(self):
        file = File(path="test")
        self.assertEqual("test",file.getPath())

    def test_getPerson(self):
        person = createPerson()
        person.save()
        file = File(person=person,path="path")

        self.assertEqual(file.getPerson(),person)
