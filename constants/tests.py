from django.test import TestCase
from django.test import TestCase
from constants.models import GlobalConstant, KeyTypeChoices


# Create your tests here.
class GlobalConstantTest(TestCase):
    def setUp(self) -> None:
        GlobalConstant.objects.create(
            key="sample_str", key_type=KeyTypeChoices.STR, value="abc"
        )
        GlobalConstant.objects.create(
            key="sample_int", key_type=KeyTypeChoices.INT, value="123"
        )
        GlobalConstant.objects.create(
            key="sample_float", key_type=KeyTypeChoices.FLOAT, value="123.345"
        )
        GlobalConstant.objects.create(
            key="sample_bool", key_type=KeyTypeChoices.BOOL, value="True"
        )
        GlobalConstant.objects.create(
            key="sample_dict",
            key_type=KeyTypeChoices.DICT,
            value="""{"abc":"def",1:"234","4":{"a":"b"}}""",
        )
        GlobalConstant.objects.create(
            key="sample_list",
            key_type=KeyTypeChoices.LIST,
            value="""["123","ABC",12,14.567,True,False]""",
        )
        GlobalConstant.objects.create(
            key="sample_tuple",
            key_type=KeyTypeChoices.TUPLE,
            value="""("123","ABC",12,14.567,True,False)""",
        )
        GlobalConstant.objects.create(
            key="sample_set",
            key_type=KeyTypeChoices.SET,
            value="""{"123","ABC",12,14.567,True,False}""",
        )

    def test_str(self):
        sample_str = GlobalConstant.objects.get_constant_value("sample_str")
        self.assertEqual(sample_str, "abc")
        self.assertEqual(isinstance(sample_str, str), True)

    def test_int(self):
        sample_int = GlobalConstant.objects.get_constant_value("sample_int")
        self.assertEqual(sample_int, 123)
        self.assertEqual(isinstance(sample_int, int), True)

    def test_float(self):
        sample_float = GlobalConstant.objects.get_constant_value("sample_float")
        self.assertEqual(sample_float, 123.345)
        self.assertEqual(isinstance(sample_float, float), True)

    def test_bool(self):
        sample_bool = GlobalConstant.objects.get_constant_value("sample_bool")
        self.assertEqual(sample_bool, True)
        self.assertEqual(isinstance(sample_bool, bool), True)

    def test_dict(self):
        sample_dict = GlobalConstant.objects.get_constant_value("sample_dict")
        self.assertEqual(sample_dict, {"abc": "def", 1: "234", "4": {"a": "b"}})
        self.assertEqual(isinstance(sample_dict, dict), True)

    def test_list(self):
        sample_list = GlobalConstant.objects.get_constant_value("sample_list")
        self.assertEqual(sample_list, ["123", "ABC", 12, 14.567, True, False])
        self.assertEqual(isinstance(sample_list, list), True)

    def test_tuple(self):
        sample_tuple = GlobalConstant.objects.get_constant_value("sample_tuple")
        self.assertEqual(sample_tuple, ("123", "ABC", 12, 14.567, True, False))
        self.assertEqual(isinstance(sample_tuple, tuple), True)

    def test_set(self):
        sample_set = GlobalConstant.objects.get_constant_value("sample_set")
        self.assertEqual(sample_set, {"123", "ABC", 12, 14.567, True, False})
        self.assertEqual(isinstance(sample_set, set), True)
