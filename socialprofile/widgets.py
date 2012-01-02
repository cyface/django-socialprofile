from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput

class H5EmailInput(TextInput):
    input_type = 'email'

class H5NumberInput(TextInput):
    input_type = 'number'

class H5TelephoneInput(TextInput):
    input_type = 'tel'

class H5DateInput(DateInput):
    input_type = 'date'

class H5DateTimeInput(DateTimeInput):
    input_type = 'datetime'

class H5TimeInput(TimeInput):
    input_type = 'time'