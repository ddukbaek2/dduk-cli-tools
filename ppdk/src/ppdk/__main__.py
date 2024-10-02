#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Callable, Iterator, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
from argparse import ArgumentParser, Namespace
import subprocess
import sys
from dduk.application.predefinedsymbols import PredefinedSymbols
from dduk.application.application import Application


def GetInstalledPythonInterpreters() -> list[str]:
	try:
		if sys.platform == "win32":
			output : str = subprocess.check_output("where python", shell = True, text = True)
		else:
			output : str = subprocess.check_output("which -a python python3", shell = True, text = True)
		return output.strip().split("\n")
	except Exception as exception:
		return list()


#--------------------------------------------------------------------------------
# 패키지 메인 함수.
#--------------------------------------------------------------------------------
def Main(parser : ArgumentParser) -> int:
	parsedArguments : Namespace = parser.parse_args()
	command : str = parsedArguments.command
	path : str = parsedArguments.path
	arguments : list[str] = parsedArguments.arguments

	for pythonInterpreter in GetInstalledPythonInterpreters():
		builtins.print(pythonInterpreter)

	if command == "new": # p, i
		interpreter : str = parsedArguments.interpreter
		if not interpreter:
			
		builtins.print(interpreter)
		pass
	elif command == "update":
		pass
	elif command == "build":
		pass
	elif command == "archive":
		pass
	elif command == "run": # p a
		pass
	elif command == "tests":
		pass
	elif command == "debug": # p a
		pass
	elif command == "service": # p a
		pass
	else:
		builtins.print(command)
		builtins.print(path)
		builtins.print(interpreter)
		builtins.print(arguments)

	return 0