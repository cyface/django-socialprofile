"""Custom Widget to enable use of HTML5 Form element types"""
from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput


class H5EmailInput(TextInput):
    """HTML5 Email Input Type"""
    input_type = 'email'


class H5NumberInput(TextInput):
    """HTML5 Number Input Type"""
    input_type = 'number'


class H5TelephoneInput(TextInput):
    """HTML5 Telephone Number Input Type"""
    input_type = 'tel'


class H5DateInput(DateInput):
    """HTML5 Date Input Type"""
    input_type = 'date'


class H5DateTimeInput(DateTimeInput):
    """HTML5 DateTime Input Type"""
    input_type = 'datetime'


class H5TimeInput(TimeInput):
    """HTML5 Time Input Type"""
    input_type = 'time'
