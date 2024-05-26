"""
RECON STEP: USING SITE REPORT
scope: Obtain invaluable site information via Netcraft
"""

import webbrowser
from utils.data import ProjectData as pd


netcraft = "https://sitereport.netcraft.com"


def run_search(site):
    webbrowser.open(netcraft+f"?url={site}")

# ###*******************************************#######


def view_report(url):
    run_search(url)


view_report(pd.target_url)