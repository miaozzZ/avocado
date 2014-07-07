#!/usr/bin/python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2014
# Author: Ruda Moura <rmoura@redhat.com>

from avocado import test
from avocado import job


class multiplextest(test.Test):

    """
    Execute the Linux Build test.
    """

    def setup(self):
        self.compile_code()
        self.set_hugepages()
        self.set_numa_balance()
        self.assembly_vm()

        if self.params.os_type == 'windows':
            self.log.info('Preparing VM with Windows (%s)', self.params.win)
        if self.params.os_type == 'linux':
            self.log.info('Preparing VM with Linux (%s)', self.params.distro)

    def compile_code(self):
        self.log.info('Compile code')
        self.log.info('gcc %s %s', self.params.gcc_flags, 'code.c')

    def set_hugepages(self):
        if self.params.huge_pages == 'yes':
            self.log.info('Setting hugepages')

    def set_numa_balance(self):
        if self.params.numa_balance:
            self.log.info('Numa balancing: %s', self.params.numa_balance)
        if self.params.numa_balancing_migrate_deferred:
            self.log.info('Numa balancing migrate deferred: %s',
                          self.params.numa_balancing_migrate_deferred)

    def assembly_vm(self):
        self.log.info('Assembling VM')
        if self.params.drive_format:
            self.log.info('Drive format: %s', self.params.drive_format)
        if self.params.nic_model:
            self.log.info('NIC model: %s', self.params.nic_model)
        if self.params.enable_msx_vectors == 'yes':
            self.log.info('Enabling msx models')

    def action(self):
        self.log.info('Executing synctest...')
        self.log.info('synctest --timeout %s --tries %s',
                      self.params.sync_timeout,
                      self.params.sync_tries)

        self.log.info('Executing ping test...')
        cmdline = 'ping --timeout %s --tries %s' % (self.params.ping_timeout,
                                                    self.params.ping_tries)

        if self.params.ping_flags:
            cmdline += ' %s' % self.params.ping_flags

        self.log.info(cmdline)


if __name__ == "__main__":
    job.main()