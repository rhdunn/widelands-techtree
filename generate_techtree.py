# Generate a Widelands tribe economy graph ("tech tree") from Widelands source code
#
# Copyright (C) Reece H. Dunn
#
# This file is part of widelands-techtree.
#
# widelands-techtree is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2, or (at your option) any later version.
#
# widelands-techtree is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with the program; see the file COPYING. If not,
# write to the Free Software Foundation, Inc., 59 Temple Place
# - Suite 330, Boston, MA 02111-1307, USA.

import sys

# NOTE: ConfigParser in python expects a section header at the start, so can't be used here.
def read_conf(conf):
	data = {}
	section = None
	with open(conf) as f:
		for line in f:
			line = line.replace('\n', '')
			if '[' in line:
				section = line.replace('[', '').replace(']', '')
			elif section == None:
				if 'size=' in line:
					data['type'] = 'building'
					data['size'] = line.replace('size=', '')
				elif 'output=' in line:
					output = [ line.replace('output=', '') ]
					if data.has_key('output'):
						output.extend(data['output'])
					data['output'] = output
			elif section == 'inputs':
				if '=' in line:
					input = [ line[:line.find('=')] ]
					if data.has_key('input'):
						input.extend(data['input'])
					data['input'] = input
	return data

print read_conf(sys.argv[1])
