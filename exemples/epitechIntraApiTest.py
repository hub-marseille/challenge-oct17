#!/usr/bin/python3

from sys import argv, stderr, exit, stdout
import requests, json

BASE_URL = "https://intra.epitech.eu"


def usage(program_name):
    print("USAGE")
    print("\t\t%s autologin" % program_name)
    print("")
    print("DESCRIPTION")
    print("\t\tautologin\tLien autologin pour l'intra EPITECH")


def autologin(url):
    session = requests.session()
    session.get(url)
    return session


def show_logtime(session):
    request = session.get(BASE_URL + '/user?format=json')
    user_info = json.loads(request.text)
    print("Bonjour %s, tu as passé %s heures à l'école ces 7 derniers jours" % (user_info["title"], user_info["nsstat"]["active"]))

def main():
    if (len(argv) == 2):
        if (argv[1] == '-h'):
            usage(argv[0])
        else:
            session = autologin(argv[1])
            show_logtime(session)
    else:
        usage(argv[0])

if __name__ == "__main__":
    main()
