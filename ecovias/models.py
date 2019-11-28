from django.db import models

class People(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    optin = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} <{}>".format(self.name, self.email)

    def send_email(self):
        return 'Sim' if self.optin else 'Não'

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

class Log(models.Model):
    status = models.CharField(max_length=150)
    operation = models.CharField(max_length=10)
    convoy = models.BooleanField(default = False)
    convoy_message = models.CharField(max_length=250, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def lanes(self):
        str_lanes = self.operation.replace('S', '↑')
        str_lanes = str_lanes.replace('D', '↓')
        str_lanes = str_lanes.replace('X', 'x')
        str_lanes = str_lanes.replace('Z', 'x')
        return str_lanes

    def has_convoy(self):
        return 'Sim' if self.convoy else 'Não'

    def __str__(self):
        return self.status

    @staticmethod
    def get_lane(string):
        str_lanes = string.replace('S', '↑')
        str_lanes = str_lanes.replace('D', '↓')
        str_lanes = str_lanes.replace('X', 'x')
        str_lanes = str_lanes.replace('Z', 'x')
        return str_lanes

    @staticmethod
    def get_operation(operation):
        if operation == '5 x 5':
            return '{} (Normal)'.format(operation)
        elif operation == '8 x 2':
            return '{} (Subida)'.format(operation)
        elif operation == '7 x 3':
            return '{} (Descida)'.format(operation)
        else:
            return operation

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
