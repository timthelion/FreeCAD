#! python
# -*- coding: utf-8 -*-
# (c) 2006 Juergen Riegel 

from __future__ import absolute_import
from . import template
import generateBase.generateModel_Module

class TemplateModuleGui (template.ModelTemplate):
    def Generate(self):
        print ("Genertate() needs to be implemented in a Template class!")

