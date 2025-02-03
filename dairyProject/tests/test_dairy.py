import unittest

from celery.worker.consumer.mingle import exception
from pysnmp.proto.errind import NoAccessEntry
from pysnmp.smi.error import NoAccessError

from dairyProject.dairy import Dairy

class TestDairyClass(unittest.TestCase):
    def test_that_class_exists(self):
        dairy = Dairy("fullname", "pin")

    def test_that_dairy_can_add_entry_and_check_size(self):
        dairy = Dairy("fullname", "pin")
        dairy.add_entry("title", "body")
        self.assertEqual(1, dairy.my_size())

    def test_dairy_can_add_entry_and_retrieve_entry(self):
        dairy = Dairy("fullname", "pin")
        dairy.add_entry("title", "body")

    def test_to_lock_dairy(self):
        dairy = Dairy("fullname", "pin")
        dairy.lock()
        self.assertTrue(dairy.is_lock())
        self.assertRaises(TypeError, dairy.unlock, "abc")
        dairy.unlock("pin")
        self.assertFalse(dairy.is_lock())

    def test_to_get_dairy_name(self):
        dairy = Dairy("fullname", "pin")
        actual = dairy.get_fullname()
        expected = "fullname"
        self.assertEqual(expected, actual)


    def test_to_setUsername(self):
        dairy = Dairy("fullname", "pin")
        dairy.set_fullname("<NAME>")
        self.assertEqual(dairy.fullname, "<NAME>")


    def test_to_create_entry_with_wrong_values(self):
        dairy = Dairy("fullname", "pin")
        self.assertRaises(ValueError, dairy.add_entry, "", "body")
        self.assertRaises(ValueError, dairy.add_entry, "title", "")

    def test_to_add_entry_and_check_size(self):
        dairy = Dairy("fullname", "pin")
        dairy.add_entry("title", "body")
        dairy.add_entry("title", "body")
        dairy.add_entry("title", "body")
        self.assertEqual(3, dairy.my_size())

    def test_to_create_two_entry_find_entry_by_id(self):
        dairy = Dairy("fullname", "pin")
        dairy.add_entry("title", "body")
        dairy.add_entry("title2", "body")
        entry1 = dairy.find_entry_by_id(1)
        entry2 = dairy.find_entry_by_id(2)
        self.assertEqual("title", entry1.get_title())
        self.assertEqual("title2", entry2.get_title())

    def test_create_no_entry_find_entry_by_id(self):
        dairy = Dairy("fullname", "pin")
        self.assertRaises(IndexError, dairy.find_entry_by_id, 1)

    def test_to_lock_dairy_and_try_to_add_entry(self):
        dairy =Dairy("fullname", "pin")
        dairy.lock()
        self.assertRaises(NoAccessError, dairy.add_entry, "title", "body")

    def test_to_add_entry_and_delete_entry_and_check_size(self):
        dairy = Dairy("fullname", "pin")
        dairy.add_entry("title", "body")
        self.assertEqual(1, dairy.my_size())
        dairy.deleteEntryById(1)
        self.assertEqual(0, dairy.my_size())

    def test_to_create_entry_and_delete_entry_with_invalid_id(self):
        dairy = Dairy("fullname", "pin")
        self.assertRaises(IndexError, dairy.delete_entry_by_Id, 1)
        dairy.add_entry("title", "body")
        self.assertRaises(IndexError, dairy.delete_entry_by_Id, 12)

    def test_create_entry_lock_entry_try_to_update_entry(self):
        dairy = Dairy("fullname", "pin")
        dairy.add_entry("title", "body")
        dairy.lock()
        self.assertRaises(ValueError, dairy.update_entry_by_id, 1, "new title", "new body")
        dairy.unlock("pin")
        dairy.update_entry_by_id(1, "new title", "new body")
        self.assertEqual(1, dairy.my_size())
        self.assertEqual("new title", dairy.find_entry_by_id(1).get_title())


if __name__ == '__main__':
    unittest.main()
