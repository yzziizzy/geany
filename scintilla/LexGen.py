# LexGen.py - implemented 2002 by Neil Hodgson neilh@scintilla.org
# Released to the public domain.

# Regenerate the Scintilla and SciTE source files that list
# all the lexers and all the properties files.
# Should be run whenever a new lexer is added or removed.
# Requires Python 2.1 or later
# Most files are regenerated in place with templates stored in comments.
# The VS .NET project file is generated into a different file as the
# VS .NET environment will not retain comments when modifying the file.
# The files are copied to a string apart from sections between a
# ++Autogenerated comment and a --Autogenerated comment which is
# generated by the CopyWithInsertion function. After the whole
# string is instantiated, it is compared with the target file and
# if different the file is rewritten.
# Does not regenerate the Visual C++ 6 project files but does the VS .NET
# project file.

import string
import sys
import os
import glob

# EOL constants
CR = "\r"
LF = "\n"
CRLF = "\r\n"
if sys.platform == "win32":
    NATIVE = CRLF
else:
    # Yes, LF is the native EOL even on Mac OS X. CR is just for
    # Mac OS <=9 (a.k.a. "Mac Classic")
    NATIVE = LF

# Automatically generated sections contain start and end comments,
# a definition line and the results.
# The results are replaced by regenerating based on the definition line.
# The definition line is a comment prefix followed by "**".
# If there is a digit after the ** then this indicates which list to use
# and the digit and next character are not part of the definition
# Backslash is used as an escape within the definition line.
# The part between \( and \) is repeated for each item in the list.
# \* is replaced by each list item. \t, and \n are tab and newline.
def CopyWithInsertion(input, commentPrefix, retainDefs, eolType, *lists):
	copying = 1
	listid = 0
	output = []
	for line in input.splitlines(0):
		isStartGenerated = line.startswith(commentPrefix + "++Autogenerated")
		if copying and not isStartGenerated:
			output.append(line)
		if isStartGenerated:
			if retainDefs:
				output.append(line)
			copying = 0
			definition = ""
		elif not copying and line.startswith(commentPrefix + "**"):
			if retainDefs:
				output.append(line)
			definition = line[len(commentPrefix + "**"):]
			listid = 0
			if definition[0] in string.digits:
				listid = int(definition[:1])
				definition = definition[2:]
			# Hide double slashes as a control character
			definition = definition.replace("\\\\", "\001")
			# Do some normal C style transforms
			definition = definition.replace("\\n", "\n")
			definition = definition.replace("\\t", "\t")
			# Get the doubled backslashes back as single backslashes
			definition = definition.replace("\001", "\\")
			startRepeat = definition.find("\\(")
			endRepeat = definition.find("\\)")
			intro = definition[:startRepeat]
			out = ""
			if intro.endswith("\n"):
				pos = 0
			else:
				pos = len(intro)
			out += intro
			middle = definition[startRepeat+2:endRepeat]
			for i in lists[listid]:
				item = middle.replace("\\*", i)
				if pos and (pos + len(item) >= 80):
					out += "\\\n"
					pos = 0
				out += item
				pos += len(item)
				if item.endswith("\n"):
					pos = 0
			outro = definition[endRepeat+2:]
			out += outro
			out = out.replace("\n", eolType) # correct EOLs in generated content
			output.append(out)
		elif line.startswith(commentPrefix + "--Autogenerated"):
			copying = 1
			if retainDefs:
				output.append(line)
	output = [line.rstrip(" \t") for line in output] # trim trailing whitespace
	return eolType.join(output) + eolType

def UpdateFile(filename, updated):
	""" If the file is different to updated then copy updated
	into the file else leave alone so CVS and make don't treat
	it as modified. """
	try:
		infile = open(filename, "rb")
	except IOError:	# File is not there yet
		out = open(filename, "wb")
		out.write(updated)
		out.close()
		print "New", filename
		return
	original = infile.read()
	infile.close()
	if updated != original:
		os.unlink(filename)
		out = open(filename, "wb")
		out.write(updated)
		out.close()
		print "Changed", filename
	#~ else:
		#~ print "Unchanged", filename

def Generate(inpath, outpath, commentPrefix, eolType, *lists):
	"""Generate 'outpath' from 'inpath'.

	    "eolType" indicates the type of EOLs to use in the generated
	        file. It should be one of following constants: LF, CRLF,
	        CR, or NATIVE.
	"""
	#print "generate '%s' -> '%s' (comment prefix: %r, eols: %r)"\
	#      % (inpath, outpath, commentPrefix, eolType)
	try:
		infile = open(inpath, "r")
	except IOError:
		print "Can not open", inpath
		return
	original = infile.read()
	infile.close()
	updated = CopyWithInsertion(original, commentPrefix,
		inpath == outpath, eolType, *lists)
	UpdateFile(outpath, updated)

def Regenerate(filename, commentPrefix, eolType, *lists):
	"""Regenerate the given file.

	    "eolType" indicates the type of EOLs to use in the generated
	        file. It should be one of following constants: LF, CRLF,
	        CR, or NATIVE.
	"""
	Generate(filename, filename, commentPrefix, eolType, *lists)

def FindModules(lexFile):
	modules = []
	f = open(lexFile)
	for l in f.readlines():
		if l.startswith("LexerModule"):
			l = l.replace("(", " ")
			modules.append(l.split()[1])
	return modules

def ciCompare(a,b):
	return a.lower() < b.lower()

def RegenerateAll():
	root="./"

	# Find all the lexer source code files
	lexFilePaths = glob.glob(root + "Lex*.cxx")
	lexFiles = [os.path.basename(f)[:-4] for f in lexFilePaths]
	print lexFiles
	lexerModules = []
	for lexFile in lexFilePaths:
		lexerModules.extend(FindModules(lexFile))
	lexerModules.sort(ciCompare)

	Regenerate(root + "KeyWords.cxx", "//", NATIVE, lexerModules)
	
RegenerateAll()
