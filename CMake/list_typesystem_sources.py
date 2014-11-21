#!/bin/env python

import os.path
import re
import sys
import xml.sax

prefix = None

class_types = {
  'object-type',
  'value-type',
  'interface-type'
}

scope_types = class_types | {
  'namespace-type'
}

#==============================================================================
class typesystem_parser(xml.sax.ContentHandler):
  #----------------------------------------------------------------------------
  def __init__(self):
    self.current_namespace = []
    self.package_name = None
    self.package_prefix_path = None

  #----------------------------------------------------------------------------
  def printFile(self, name):
    print os.path.join(self.package_prefix_path, name.lower())

  #----------------------------------------------------------------------------
  def printFiles(self, prefix, extensions):
    for extension in extensions:
      self.printFile(prefix + '.' + extension)

  #----------------------------------------------------------------------------
  def printWrapperFiles(self, names):
      self.printFiles('_'.join(names) + '_wrapper', ['cpp', 'h'])

  #----------------------------------------------------------------------------
  def startElement(self, name, attrs):
    if name == 'typesystem':
      self.package_name = attrs['package']
      self.package_prefix_path = os.path.join(prefix, self.package_name)
      self.printFile(self.package_name + '_module_wrapper.cpp')
      self.printFile(self.package_name + '_python.h')

    elif name == 'namespace-type':
      self.current_namespace.append(attrs['name'])
      self.printWrapperFiles(self.current_namespace)

    elif name in class_types:
      self.current_namespace.append(attrs['name'])
      self.printWrapperFiles(self.current_namespace)

  #----------------------------------------------------------------------------
  def endElement(self, name):
    if name in scope_types:
      self.current_namespace.pop()

#==============================================================================
if __name__ == '__main__':
  if len(sys.argv) < 3:
    sys.exit(1)

  prefix = sys.argv[2]
  xml.sax.parse(sys.argv[1], typesystem_parser())