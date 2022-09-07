
from flask import Flask, request, make_response, jsonify, logging

from collections import defaultdict
import datetime

urls_stats = defaultdict(list)

ONE_DAY_SECONDS = 24 * 60 * 60

def make_visit(short_code):
    urls_stats[short_code].append(datetime.datetime.now())
    return

def get_stats(short_code):
    now = datetime.datetime.now()
    values = urls_stats[short_code]
    counter = 0

    for time in values:
        diff = now - time 
        if diff.total_seconds() < ONE_DAY_SECONDS:
            counter = counter + 1
    
    return counter


def cleanup_visits(short_code):
    del urls_stats[short_code]
