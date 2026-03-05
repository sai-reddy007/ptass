from integrations.adapters.bugcrowd import BugcrowdAdapter
from integrations.adapters.cobalt_strike import CobaltStrikeAdapter
from integrations.adapters.generic_tools import GenericToolAdapter

ADAPTERS = {
    "cobalt_strike": CobaltStrikeAdapter(),
    "bugcrowd": BugcrowdAdapter(),
    "hackerone": GenericToolAdapter("hackerone"),
    "burp_suite": GenericToolAdapter("burp_suite"),
    "nmap": GenericToolAdapter("nmap"),
    "nessus": GenericToolAdapter("nessus"),
    "openvas": GenericToolAdapter("openvas"),
    "owasp_zap": GenericToolAdapter("owasp_zap"),
}
