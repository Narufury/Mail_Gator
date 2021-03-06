import os
import subprocess


def trace_route(IP):
    print("")
    os.system("traceroute " + IP)
    print("")
    print("----------------------------------")
    print("\n")
    os.system("whois " + IP)


def map_geo(IP):
    subprocess.Popen(["firefox", "https://ipleak.net/?q="+IP])


def header_analyse():
    subprocess.Popen(["firefox", "https://www.whatismyip.com/email-header-analyzer/"])


def last_servering_ip(url):
    os.system("dependency/vt url last_serving_ip_address " + url)


def url_authen(url):
    os.system("dependency/vt url " + url + " --include=last_analysis_results.*.result")