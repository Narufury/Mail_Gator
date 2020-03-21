import os
from colorama import Fore

# - Color
red = Fore.RED
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX


# Main Menue
def main_menu():
    print(yellow, '\n [*] Main Menue [*]')
    print(white, ' \n  1) Email Identities and Data')
    print(white, ' 2) Web Tracking Email Address')
    print(white, ' 3) IP Source Route')
    print(white, ' 4) Malware Anlayse')
    print(white, ' 5) Volatility Memory')
    print(white, ' 99) Exit')


def email_id_menu():
    print(yellow, '\n [*] Email Identities and Data [*] ')
    print(white, '\n  1) Full Email Metadata')
    print(white, ' 2) Short list Metadata')
    print(white, ' 3) Body Email Extract')
    print(white, ' 50) Return To Main Menu')
    print(white, ' 99) Exit')


def web_tracking():
    print(yellow, '\n [*] Web Tracking Email Address [*]')
    print(white, '\n  1) Google Dorks')
    print(white, ' 2) Open Multiple Url From File')
    print(white, ' 3) Security Reffered Website')
    print(white, ' 50) Retun To Main Menu')
    print(white, ' 99) Exit')


# menu 2 of web_tracking
def refered_websit():
    print(yellow, '\n [*] Email Adresse Check [*]')
    print(white, '\n  1) Hunter.IO')
    print(white, ' 2) Mail Hippo')
    print(white, ' 50) Retun To Previous Menu')
    print(white, ' 99) Exit')


def ip_source_route():
    print(yellow, '\n [*] IP Route / Geolocation Tracking / Header Analyse   [*]')
    print(white, '\n  1) IP Route ') # traceroute + whois
    print(white, ' 2) IP Map Geolocation') # https://ipleak.net/?q="public_ip_target_without_cotes"
    print(white, ' 3) Analyse Email Header') # https://www.whatismyip.com/email-header-analyzer/
    print(white, ' 4) Last Servering IP')
    print(white, ' 5) Url Authenticity')
    print(white, ' 50) Return To Main Menu')
    print(white, ' 99) Exit')


def vt_analyse():
    print(yellow, '\n [*] Malware Analyse [*] ')
    print(white, '\n 1) Get Base64 File Hash')
    print(white, '2) Analyse Attachment')
    print(white, '50) Return To Main Menu')
    print(white, '99) Exit')


def volatility_m():
    print(yellow, '\n [*] Volatility Memory [*]')
    print(white, '\n 1) Exiftool')
    print(white, '2) Strings')
    print(white, '3) Hexdump')
    print(white, '4) PDF ID')
    print(white, '5) PDF PARSER')
    print(white, '6) Office Doc Analyse & Macro Analyse')
    print('99) Exit')