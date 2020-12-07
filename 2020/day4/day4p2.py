# import
import re


def validate_year(year):
    return re.match("[0-9]{4}", year) is not None


def validate_birth_year(year):
    return validate_year(year) and 1920 <= int(year) <= 2002


def validate_issue_year(year):
    return validate_year(year) and 2010 <= int(year) <= 2020


def validate_expiration_year(year):
    return validate_year(year) and 2020 <= int(year) <= 2030


def validate_height(height):
    result = re.search("([0-9]*)(in|cm)", height)
    if result is not None:
        groups = result.groups()
        if groups[1] == "in":
            return 59 <= int(groups[0]) <= 76
        elif groups[1] == "cm":
            return 150 <= int(groups[0]) <= 193
        else:
            return False
    else:
        return False


def validate_hair_color(color):
    return re.match("[#][0-9a-f]{6}", color) is not None


def validate_eye_color(color):
    return color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_pid(pid):
    return re.match("^[0-9]{9}$", pid) is not None


def validate_cid(cid):
    return True

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
validators = {"byr": validate_birth_year, "iyr": validate_issue_year, "eyr": validate_expiration_year, "hgt": validate_height, "hcl": validate_hair_color, "ecl": validate_eye_color, "pid": validate_pid, "cid": validate_cid}

counter = 0
for passport in passports:
    keys = set(dict(passport).keys())
    if mustContainKeys.issubset(keys):
        valid = True
        for key, value in passport:
            if validators[key](value):
                continue
            else:
                valid = False
                break
        if valid:
            counter += 1

print counter
