"""Lolcode kernel module"""
##!/usr/bin/env python
import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel

workingdir = "/tmp/lolcodekernel/"

class janslolcodekernel(Kernel):
    """Lolcode kernel class"""
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'lolcode'
    language_version = '0.10.5'
    language_info = {
        'name': 'lolcode',
        'mimetype': 'application/lolcode',
        'file_extension': '.lc',
    }
    banner = "LOL CODE HAS KERNEL"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open(workingdir + "haha.lc", "w", encoding="utf-8") as file:
                file.write(code)
            solution = pexpect.run('lci haha.lc').decode('ascii')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_shutdown(self, restart):
        shutil.rmtree(workingdir)
