import ast
from typing import Union
from django.db import models


class KeyTypeChoices(models.TextChoices):
    STR = "STR"
    INT = "INT"
    FLOAT = "FLOAT"
    BOOL = "BOOL"
    DICT = "DICT"
    LIST = "LIST"
    TUPLE = "TUPLE"
    SET = "SET"


class GlobalConstantManager(models.Manager):
    def get_constant_value(self, constant_name) -> Union[str, int, float, dict, None]:
        try:
            constant: GlobalConstant = self.get(key=constant_name)
            return constant.cast_value()
        except self.model.DoesNotExist:
            return None


class GlobalConstant(models.Model):
    key = models.CharField(
        max_length=512,
        unique=True,
        blank=False,
        null=False,
    )
    key_type = models.CharField(
        choices=KeyTypeChoices.choices,
        max_length=512,
        blank=False,
        null=False,
    )
    value = models.TextField(blank=False, null=False)

    objects = GlobalConstantManager()

    def __str__(self):
        return self.key

    def cast_value(self):
        if self.key_type == KeyTypeChoices.STR:
            return self.value
        return ast.literal_eval(self.value)
