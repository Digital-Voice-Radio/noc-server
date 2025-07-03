
from django.core.management.base import BaseCommand, CommandError
from core.models import Server, Talkgroup
import json

import time

class Command(BaseCommand):

    help = "Write Talkgroup and Server ID fies"

    def add_arguments(self, parser):
        parser.add_argument("--path", default="/var/www/noc.dvdmr.org/downloads", nargs=1, type=str)

    def handle(self, *args, **options):
        PATH = options['path'][0]

        result = []
        print('Updating Files: talkgroup_ids.json')
        for x in Talkgroup.objects.all():
            result.append({ 'tgid': x.tgid, 'callsign': '%s (%s)' % (x.name, x.owner), 'id': x.tgid })

        with open(f'{PATH}/talkgroup_ids.json', 'w') as out:
            out.write(json.dumps({'results': result}))



        print('Updating Files: server_ids.tsv')
        with open(f'{PATH}/server_ids.tsv', 'w') as out:
            out.write("Country  OPB Net ID  IP/Hostname Password    Port\n")
            for x in Server.objects.filter(listed=True):
                if x.hotspot_allow:
                    out.write(f"{x.server_name}    {x.network_id}  {x.hostname}    {x.hotspot_pwd} {x.hotspot_port}\n")
                else:
                    out.write(f"{x.server_name}    {x.network_id}\n")






