=======================
Django Constants
=======================

This is a Django app designed to store global constants with different data types. It provides a central location to manage and access configuration values that can be easily reused throughout your Django project.

## Getting Started

1. Add 'constants' to the INSTALLED_APPS list in your project's settings:
```
INSTALLED_APPS = [
    # ...
    'constants',
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
from constants.models import GlobalConstant, KeyTypeChoices

GlobalConstant.objects.create(key="sample_int",key_type=KeyTypeChoices.INT, value="123")

# NOTE: key is a unique field in database so only one key can exist in GlobalConstant model
GlobalConstant.objects.filter(key="sample_int").update(value="123")
```

### Accessing Global Constants

You can access the global constants throughout your application using the GlobalConstant model methods:

```
from constants.models import GlobalConstant

# Get the value of a constant
constant_value = GlobalConstant.objects.get_constant_value('CONSTANT_NAME')
```

The get_constant_value method returns the constant value with the appropriate data type as specified during creation.


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

