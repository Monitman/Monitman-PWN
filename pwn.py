#! /usr/bin/env python3

import locale, sys
from dialog import Dialog

def disclaimer():
    d = Dialog(dialog="dialog",autowidgetsize=True)
    d.set_background_title("Monitman LLC -> Baba Yaga PWN")

    d.msgbox("Legal Disclaimer: This application is intended for use by security professionals, it's aim is to assist them in easily finding security problems and testing the security of both people and systems. Please use this application in accordance with your local/state/federal laws.")


def main():
    d = Dialog(dialog="dialog",autowidgetsize=True)
    d.set_background_title("Monitman LLC -> Baba Yaga PWN")

    code, tag = d.menu("Pick your poison:",
          choices=[("1", "Wireless Tools"),
                   ("2", "About PWN"),
                   ("->", "Exit")
                  ])

    if code == d.OK:
        if tag == "->":
            print "Have a good day..."
            sys.exit(0)
        elif tag == "2":
           d.msgbox("This application was written and is maintained by Monitman LLC. Send any queries, patches or suggestions to support@monitman.solutions")
           main()

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    disclaimer()
    main()

