#! python3
# domaincheck.py
# look up information about domain(s) and display report

import socket

import click
import whois

@click.command()
@click.argument('host_names', nargs=-1)
@click.option(
    '--host_names_file',
    type=click.File('r'),
    required=False,
)

def check_host_names(host_names_file, host_names):
    """
         Check IP addresses, domain registration, nameservers, and zone records
    """
    if host_names:
        add_s = ''
        host_count = len(host_names)
        if host_count > 1: add_s = 's'
        args_listed = ('Hostname{} specified: {}'.format(add_s, host_count))
        click.echo(args_listed)
        get_host_data(host_names)

    elif host_names_file:
        hosts_in_file = host_names_file.readlines()
        hosts_in_file = [x.strip() for x in hosts_in_file]
        get_host_data(hosts_in_file)
        # click.echo(hosts_in_file)

    else:          # no hostnamespassed as argument or filename
        click.echo('Please provide at least one domain name to check!')

def get_host_data(hostnames):
    host_data = ''
    for i in hostnames:
        ip_addr = socket.gethostbyname(i)
        whois_data = whois.whois(i)
        # click.echo(whois_data)
        # click.echo('{} - {}'.format(i, ip_addr))
        reg = whois_data['registrar']
        expires = whois_data['expiration_date']
        # get the lowercase domain name
        dnames = whois_data['domain_name']
        if isinstance(dnames, list):
            dnames = dnames[0]
        dnames = dnames.lower()
        # get the first nameserver
        nservers = whois_data['name_servers']
        ns0 = nservers[0].lower()

        click.echo(
                '{}\t{}\t{}\t{}\t{}\t{}'.format(
                                    i,
                                    ip_addr,
                                    dnames,
                                    reg,
                                    expires,
                                    ns0,
                                    )
                   )
    return host_data


if __name__ == '__main__':
    check_host_names()
