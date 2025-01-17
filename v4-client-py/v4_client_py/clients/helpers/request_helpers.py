import json
import random

from datetime import datetime

import dateutil.parser as dp


def generate_query_path(url, params):
    entries = params.items()
    if not entries:
        return url

    paramsString = '&'.join('{key}={value}'.format(
        key=x[0],
        value=str(x[1]).lower() if isinstance(x[1], bool) else x[1]) for x in entries if x[1] is not None)
    if paramsString:
        return url + '?' + paramsString

    return url


def json_stringify(data):
    return json.dumps(data, separators=(',', ':'))


def random_client_id():
    return str(int(float(str(random.random())[2:])))


def generate_now_iso():
    return datetime.utcnow().strftime(
        '%Y-%m-%dT%H:%M:%S.%f',
    )[:-3] + 'Z'


def iso_to_epoch_seconds(iso):
    return dp.parse(iso).timestamp()


def epoch_seconds_to_iso(epoch):
    return datetime.utcfromtimestamp(epoch).strftime(
        '%Y-%m-%dT%H:%M:%S.%f',
    )[:-3] + 'Z'


def remove_nones(original):
    return {k: v for k, v in original.items() if v is not None}
