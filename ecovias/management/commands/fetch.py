from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from ecovias.models import Log
from ecovias.models import People
from django.conf import settings

import requests

class Command(BaseCommand):

    help = 'Check Ecovias website to fetch Anchieta/Imigrantes status'

    def handle(self, *args, **options):

        request = requests.get(settings.BASE_URL)
        json = request.json()
        send_email = False

        op_name = json['TrafficOperation']['Name']
        op_desc = json['TrafficOperation']['Description']
        op_anchieta = None
        op_imigrantes = None
        has_convoy = json['Convoy']['HasConvoy']
        convoy_message = json['Convoy']['Message']

        for road in json['TrafficOperation']['Roads']:
            op_imigrantes = road['Lanes'] if road['Name'] == 'Imigrantes' else op_imigrantes
            op_anchieta = road['Lanes'] if road['Name'] == 'Anchieta' else op_anchieta

        operation = "{}{}".format(op_imigrantes, op_anchieta)
        # Comparing current status with the last one in the Log database table
        last_status = Log.objects.order_by('-id')

        if not(last_status):
            send_email = True

        if len(last_status) > 0:
            if last_status[0].status != op_name:
                send_email = True
            if last_status[0].operation != operation:
                send_email = True
            if last_status[0].convoy != has_convoy:
                send_email = True
            if last_status[0].convoy_message != convoy_message:
                send_email = True

        if send_email:
            self.send_emails({
                'op_name': Log.get_operation(op_name),
                'op_imigrantes': Log.get_lane(op_imigrantes),
                'op_anchieta': Log.get_lane(op_anchieta),
                'convoy_message': convoy_message,
                'images': settings.IMAGES
            },
            last_status[0].convoy,
            has_convoy
        )

        log = Log(
            status = op_name,
            operation = operation,
            convoy = has_convoy,
            convoy_message = convoy_message
        )

        log.save()

    def send_emails(self, params, hadConvoy = False, hasConvoy = False):
        people = People.objects.all().filter(optin=True)

        subject = 'Atualização: Anchieta/Imigrantes'
        if hasConvoy and not(hadConvoy):
            subject = '💩 COMBOIO 💩: Anchieta/Imigrantes'
        elif not(hasConvoy) and hadConvoy:
            subject = '🕺 FIM COMBOIO 🎉: Anchieta/Imigrantes'

        for person in people:
            params['url_optout'] = '{}optout/{}'.format(settings.SITE_URL, person.uuid)
            msg_html = render_to_string(
                '{}/ecovias/templates/email/notification.html'.format(settings.BASE_DIR),
                params
            )

            send_mail(
                subject,
                None,
                settings.EMAIL_FROM,
                [person.email],
                html_message=msg_html,
            )


