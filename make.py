#!/usr/bin/env python3

# Author: Peter Nardi
# Date: 11/09/21
# License: (see MIT License at the end of this file)

# Title: make

# This script performs various utility operations on a pypi development
# project -- similiar to a makefile.

# Imports

import argparse
import os
import subprocess as sp
import textwrap
import webbrowser

from pathlib import Path

# -------------------------------------------------------------------


def clean():

    # Whole directories to delete
    directories = []
    directories.append('__pycache__')
    directories.append('.pytest_cache')
    directories.append('build')
    directories.append('dist')
    directories.append('.eggs')
    directories.append('htmlcov')
    directories.append('*.egg-info')

    # NOTE: If this command were being run on the command line, you'd need to
    # escape the semicolon (\;)
    command = 'find . -name DIR -type d -exec rm -rf {} ; -prune'

    for directory in directories:
        print(command.replace('DIR', directory))
        sp.run(command.replace('DIR', directory).split())

    # Files to delete.
    files = []
    files.append('*.egg')
    files.append('*.pyc')
    files.append('*.pyo')
    files.append('.coverage')

    command = 'find . -name FILE -type f -delete'

    for file in files:
        print(command.replace('FILE', file))
        sp.run(command.replace('FILE', file).split())

    return

# -------------------------------------------------------------------


def dist():

    clean()

    commands = []
    commands.append('python3 -m build')
    commands.append('twine check dist/*')

    for command in commands:
        print(command)
        sp.run(command.split())

    return

# -------------------------------------------------------------------


def pushtest():

    dist()

    command = 'twine upload --repository-url https://test.pypi.org/legacy/ '
    command += 'dist/*'
    print(command)
    sp.run(command.split())

    return

# -------------------------------------------------------------------


def test():

    command = 'pytest --tb=short'
    print(command)
    sp.run(command.split())

    return

# -------------------------------------------------------------------


def coverage():

    commands = []
    commands.append('coverage run -m pytest')
    commands.append('coverage report -m')
    commands.append('coverage html')

    for command in commands:
        print(command)
        sp.run(command.split())

    P = str(Path(__file__).resolve().parent) + '/htmlcov/index.html'
    webbrowser.open('file://' + P, new=2)

    return

# -------------------------------------------------------------------


def release():

    dist()

    command = 'twine upload dist/*'
    print(command)
    sp.run(command.split())

    return

# -------------------------------------------------------------------


def bump(category):

    command = 'bump2version ' + category
    print(command)
    sp.run(command.split())

    return


# -------------------------------------------------------------------


def docs(basename):

    src = 'src/' + basename
    docs = 'docs/' + basename

    commands = []
    commands.append(f'rm -rf {docs}')
    commands.append('pdoc --html --output-dir docs ' + src)
    for command in commands:
        print(command)
        sp.run(command.split())

    # Open documentation in the default browser.
    P = str(Path(__file__).resolve().parent) + '/docs/index.html'
    webbrowser.open('file://' + P, new=2)

    return


# -------------------------------------------------------------------


def performTask(args):

    # This is the name of the project.
    basename = 'parser201'

    if args.clean:
        clean()
    elif args.dist:
        dist()
    elif args.pushtest:
        pushtest()
    elif args.test:
        test()
    elif args.coverage:
        coverage()
    elif args.release:
        release()
    elif args.bump:
        bump(args.bump)
    elif args.docs:
        docs(basename)
    else:
        msg = "Please provide a task to perform. Use "
        msg += f"./{os.path.basename(__file__)} -h for help."
        print('\n' + textwrap.fill(msg) + '\n')

    return

# -------------------------------------------------------------------


def main():

    # Build a python argument parser

    msg = """Perform various utility operations for a pypi development
    project."""

    epi = "Latest update: 09 Nov 2021"

    parser = argparse.ArgumentParser(description=msg, epilog=epi)

    msg = """clean-up build products."""
    parser.add_argument('-c', '--clean',
                        help=msg,
                        action='store_true',
                        dest='clean')

    msg = """create a distribution package ready for publication to pypi, but
    do not actually publish. Good for installing locally and checking the
    integrity of the build before release."""
    parser.add_argument('-d', '--dist',
                        help=msg,
                        action='store_true',
                        dest='dist')

    msg = """create and push a distribution package to test.pypi.org."""
    parser.add_argument('-p', '--pushtest',
                        help=msg,
                        action='store_true',
                        dest='pushtest')

    msg = """run pytest with the --tb=short option."""
    parser.add_argument('-t', '--test',
                        help=msg,
                        action='store_true',
                        dest='test')

    msg = """generate an HTML version of a code coverage report and open it in
    the default browser."""
    parser.add_argument('--coverage',
                        help=msg,
                        action='store_true',
                        dest='coverage')

    msg = """bump the version number of the project based on the provided
    choice: major, minor, patch."""
    parser.add_argument('-b', '--bump',
                        help=msg,
                        choices=['major', 'minor', 'patch'])

    msg = """generate a distribution package and release it to pypi.org."""
    parser.add_argument('-r', '--release',
                        help=msg,
                        action='store_true',
                        dest='release')

    msg = """generate API documentation using pdoc3"""
    parser.add_argument('--docs',
                        help=msg,
                        action='store_true',
                        dest='docs')

    args = parser.parse_args()

    performTask(args)

    return

# -------------------------------------------------------------------


if __name__ == '__main__':
    main()

# ========================================================================

# MIT License

# Copyright 2019-2021 Peter Nardi

# Terms of use for source code:

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
