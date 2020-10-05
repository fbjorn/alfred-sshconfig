# encoding: UTF-8
import os
import re
import sys

sys.path.append("lib")  # noqa

from lib.workflow import Workflow3, Workflow


def get_hosts():
    path = os.path.join(os.path.expanduser("~"), ".ssh", "config")
    with open(path) as f:
        conf = f.read()
    hosts = re.findall(r"[\t ]*?Host[\t ]+?(.+)$", conf, re.MULTILINE)
    return hosts


def main(wf):
    # type: (Workflow) -> int

    query = ""
    if len(wf.args):
        query = wf.args[0]

    hosts = wf.cached_data("hosts", get_hosts, max_age=10)
    hosts = wf.filter(query, hosts)
    for host in hosts:
        wf.add_item(title=host, valid=True, arg=host)  # TODO: Add IP and user/keypair

    wf.send_feedback()
    return 0


if __name__ == "__main__":
    workflow = Workflow3()
    sys.exit(workflow.run(main))
