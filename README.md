# Django Constants

This is a Django app designed to store global constants with different data types. It provides a central location to manage and access configuration values that can be easily reused throughout your Django project.

## Getting Started

1. Add "django_constants" to the INSTALLED_APPS list in your project's settings:
```
INSTALLED_APPS = [
    # ...
    "django_constants",
    # ...
]
```

2. Apply migrations:
```
python manage.py migrate
```

## Usage

### Adding Global Constants
1. Log in to the Django admin interface.
Navigate to the "Global Constants" section.
Add new constants with their names, values, and data types.

2. Create/Update through models
```
from django_constants.models import GlobalConstant, KeyTypeChoices

GlobalConstant.objects.create(
    key="CONSTANT_NAME", key_type=KeyTypeChoices.INT, value="123"
)

# NOTE: key is a unique field in database so only one key can exist in GlobalConstant model
GlobalConstant.objects.filter(key="CONSTANT_NAME").update(value="1234")

# Similary constants of other types can be created by specifying the key type and value as string
GlobalConstant.objects.create(
    key="sample_str", key_type=KeyTypeChoices.STR, value="abc"
)
```

3. Sample create functions for all other available data types

```
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
```

4. Accessing Global Constants

The get_constant_value method returns the constant value with the appropriate data type as specified during creation.

```
# Get the value of a constant
constant_value = GlobalConstant.objects.get_constant_value("CONSTANT_NAME")
# Output -> constant_value = 1234 (type <class 'int'>)

constant_value = GlobalConstant.objects.get_constant_value("sample_dict")
# Output -> constant_value = {"abc":"def",1:"234","4":{"a":"b"}} (type <class 'dict'>)
```


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## v1.0.0
- First version of this Django constants!
- Validated against Django >= 3.2 .
- Support for data types such as str, int, float, bool, dict, list, tuple, set

## Next Milestones
- Add support for bytes datatype
- Add encryption logic for senstive constants like secret keys, payment related info, etc.