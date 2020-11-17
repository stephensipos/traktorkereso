
from django.core.management.base import BaseCommand, CommandError

import glob
import os
import re
import argparse
import pathlib
import json
import datetime

from traktorkereso.tractors.models import Condition
from traktorkereso.tractors.models import Tractor
from traktorkereso.tractors.models import Equipment

def save_tractor(tractor):
    fields = {}
    
    fields["make"] = tractor.get("make", None)
    fields["model"] = tractor.get("model", None)
    fields["price"] = parse_price(tractor.get("price", None))
    fields["year"] = parse_year_month(tractor.get("year", None))

    if "condition" in tractor:
        fields["condition"] = Condition.objects.get(description = tractor["condition"])
    
    fields["hours"] = parse_hours(tractor.get("hours", None))
    fields["engine_power"] = parse_engine_power(tractor.get("engine_power", None))
    fields["documents_valid"] = parse_year_month(tractor.get("documents_valid", None))
    fields["documents_type"] = tractor.get("documents_type", None)
    fields["description"] = tractor.get("description", None)
    fields["image_url"] = tractor.get("image_url", None)
    fields["url"] = tractor.get("url", None)
    fields["fuel_type"] = tractor.get("fuel_type", None)

    tractor_instance = Tractor(**fields)
    tractor_instance.save()

    equipment_instances = []
    for equipment in tractor["equipment"]:
        equipment_instances.append(Equipment(tractor=tractor_instance, name=equipment))
        
    Equipment.objects.bulk_create(equipment_instances, ignore_conflicts=True)


def parse_int_with_suffix(text, suffix):
    if text is None:
        return None

    pattern = re.compile(f"(([\\s\\d]+){suffix})", re.I)
    matches = pattern.search(text)
    if matches:
        match = matches.group(len(matches.groups()))
        
        value = int(re.sub(r"\s", "", match))
        return value
    else:
        return None

def parse_price(text):
    return parse_int_with_suffix(text, "Ft")

def parse_hours(text):
    return parse_int_with_suffix(text, "Óra")

def parse_engine_power(text):
    return parse_int_with_suffix(text, "kW")

def parse_year_month(text):
    if text is None:
        return None

    pattern = re.compile(r"(\d{4})(/(1?\d))?")
    matches = pattern.search(text)
    
    if matches:
        year = int(matches[1]) if matches[1] is not None else 1900
        month = int(matches[3]) if matches[3] is not None else 1

        return datetime.datetime(year, month, 1)
    else:
        return None

class Command(BaseCommand):
    help = 'Imports tractros into the database'

    def add_arguments(self, parser):
        parser.add_argument("source", help="Folder to scan for json files")

    def handle(self, *args, **options):
        if not os.path.isdir(options["source"]):
            print("source is not a directory")
            exit()
        else:
            os.chdir(options["source"])
            for file in glob.glob("*.json"):
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)
                    try:
                        save_tractor(data)
                    except Exception as e:
                        self.stderr.write(file)
                        self.stderr.write(e)