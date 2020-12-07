# import
import re

# read input
file = open("passports.txt", "r")

passports = []
passportLine = []
for line in file.readlines():
    if len(line.lstrip()) > 0:
        passportLine.extend(re.findall("([\w]*):([#\w]*)\s*", line))
    else:
        passports.append(passportLine)
        passportLine = []
passports.append(passportLine)

mustContainKeys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

counter = 0
for passport in passports:
    keys = set(dict(passport).keys())
    if mustContainKeys.issubset(keys):
        counter += 1

print counter