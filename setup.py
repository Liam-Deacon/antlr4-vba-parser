#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type: ignore
"""Setup script for package."""
import os
import sys
import configparser
import datetime
import distutils.cmd
import distutils.log
import subprocess
import glob
import shutil

from pathlib import Path

setup_kwargs = {}

from setuptools import find_packages, setup

import setuptools.command.build_py


try:
    import pbr

    setup_kwargs['pbr'] = True
except ImportError:
    setup_kwargs['pbr'] = False

here = os.path.abspath(os.path.dirname(__file__))
basename = os.path.basename(os.path.dirname(__file__))

# give a list of scripts and how they map to a package module
CONSOLE_SCRIPTS = []


class VirtualenvCommand(distutils.cmd.Command):
  """A custom command to create virtual environment."""

  description = 'create virtual environment for project'
  user_options = [
      # The format is (long option, short option, description).
  ]

  def initialize_options(self):
    """Set default values for options."""
    # Each user option must be listed here with their default value.
    ...

  def finalize_options(self):
    """Post-process options."""
    ...

  def run(self):
    """Run command."""
    command = [sys.executable, '-m', 'venv', 'venv']
    self.announce(
        'Running command: %s' % str(command),
        level=distutils.log.INFO)
    subprocess.check_call(command)


class AntlrBuildCommand(distutils.cmd.Command):
  """A custom command to generate antlr4 files from vba.g4 grammar file."""

  description = 'generate antlr4 files form grammar'
  user_options = [
      # The format is (long option, short option, description).
  ]

  def initialize_options(self):
    """Set default values for options."""
    # Each user option must be listed here with their default value.
    ...

  def finalize_options(self):
    """Post-process options."""
    ...

  def run(self):
    """Run command."""
    command = [sys.executable, 'download_external_files.py']
    self.announce(
        'Running command {}'.format(' '.join(command))
    )
    subprocess.check_call(command)

    source_dir = 'data'
    antlr4_jar = os.path.join(source_dir, 'antlr-4.9.2-complete.jar')
    vba_g4 = os.path.join(source_dir, 'vba.g4')

    command = ['java', '-jar', antlr4_jar, '-Dlanguage=Python3', vba_g4]
    self.announce(
        'Running command: %s' % " ".join(command),
        level=distutils.log.INFO)
    subprocess.check_call(command)

    dest_dir = 'antlr4_vba_parser'
    for filename in glob.glob(os.path.join(source_dir, '*.[itp]*')):
        shutil.copy2(filename, dest_dir)
        print('Copied {filename} -> {dest_dir}'.format(**locals()))



class BuildPyCommand(setuptools.command.build_py.build_py):
  """Custom build command."""

  def run(self):
    self.run_command('build_antl4')
    setuptools.command.build_py.build_py.run(self)


# load config using parser
parser = configparser.ConfigParser()
parser.read('%s/setup.cfg' % here)

install_requirements = [line.split('#')[0].strip(' ')
                        for line in open('%s/requirements.txt' % here).readlines()
                        if line and line.split('#')[0] and
                        not line.startswith('git+')]  # can't currently handle git URLs unless using PBR

setup_kwargs['install_requires'] = install_requirements

# add setup.cfg information back from metadata
try:
    from setuptools.config import read_configuration

    config = read_configuration('%s/setup.cfg' % here)
    metadata = config['metadata']
    metadata['summary'] = metadata.get('summary', metadata['description'].split('\n')[0])
    if setup_kwargs.pop('pbr', False) is not True:
        setup_kwargs.update(metadata)
        # explicitly compile a master list of install requirements - workaround for bug with PBR & bdist_wheel
        setup_kwargs['install_requires'] = list(set(list(setup_kwargs.get('install_requires',
                                                                          config.get('options', {})
                                                                                .get('install_requires', []))) +
                                                    install_requirements))

except ImportError:
    metadata = {}
finally:
    readme_filename = '%s/%s' % (here, parser['metadata']['description-file'].strip())
    with open(readme_filename) as f_desc:
        long_description = f_desc.read()
        setup_kwargs['long_description'] = long_description

    # check whether we are using Markdown instead of Restructured Text and update setup accordingly
    if readme_filename.lower().endswith('.md'):
        setup_kwargs['long_description_content_type'] = 'text/markdown'

# update with further information for sphinx
metadata.update(parser['metadata'])

if __name__ == '__main__':
    # actually perform setup here
    setup(
        setup_requires=['pbr', 'setuptools'],
        packages=find_packages(),
        entry_points={
            'console_scripts': CONSOLE_SCRIPTS
        },
        tests_require=['pytest', 'coverage'],
        include_package_data=True,
        cmdclass={
            'venv': VirtualenvCommand,
            'build_antl4': AntlrBuildCommand,
            'build_py': BuildPyCommand,
        },
        **setup_kwargs
    )
