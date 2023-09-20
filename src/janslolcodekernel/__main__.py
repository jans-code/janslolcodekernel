#!/usr/bin/env python
# *_* coding: utf-8 *_*

""" Main module """

from ipykernel.kernelapp import IPKernelApp
from .kernel import janslolcodekernel
IPKernelApp.launch_instance(kernel_class=janslolcodekernel)
