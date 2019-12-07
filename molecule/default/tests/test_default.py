import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_interface(host):
    assert host.interface('wg0').exists


def test_can_reach_server(host):
    for ip in ['10.5.0.1', '10.5.0.20', '10.5.0.21']:
        assert host.addr(ip).is_reachable
