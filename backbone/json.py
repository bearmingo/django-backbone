#/usr/bin/python

import simplejson
import datetime

from django.utils.timezone import is_aware

class DjangoJSONEncoder(simplejson.JSONEncoder):
    """
    Becase django's JSONEncoder is subclass json.JSONEncoder
    """

    def default(self, o):
        if isinstance(o, datatime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datatime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DjangoJSONEncoder, self).default(o)
