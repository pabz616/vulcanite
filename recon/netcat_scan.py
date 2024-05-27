import os
import pytest


"""
RECON STEP: NETWORK SCANNER w. NET CAT
"""


@pytest.mark.security
def scan_ip(ip):
    """Fingerprint Webserver"""
    # deepcode ignore CommandInjection: <please specify a reason of ignoring this>
    os.system(f"nc -nv -w 1 -z {ip} 80")
    
    
def banner_grab(ip):
    """Banner grab - verbose option"""
    os.system(f"nc nv {ip} 80")
    
    
target_ip = input("Please enter the target IP address: ")    
# deepcode ignore CommandInjection: <please specify a reason of ignoring this>
scan_ip(target_ip)
# banner_grab(target_ip)