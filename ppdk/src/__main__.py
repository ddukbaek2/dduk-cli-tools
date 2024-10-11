#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Callable, Awaitable, Iterator, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
from argparse import ArgumentParser
import sys
from dduk.application.predefinedsymbols import PredefinedSymbols
from dduk.application.application import Application
import ppdk


#--------------------------------------------------------------------------------
# 프로젝트 메인 함수.
#--------------------------------------------------------------------------------
def Main(arguments : list[str]) -> int:
	# 첫번째 인수 실행 파일 경로는 제외.
	try:
		# return ppdk.Main(arguments)
		parser = ArgumentParser()
		parser.add_argument("command")
		subparsers = parser.add_subparsers(dest = "command", required = True)
		newParser = subparsers.add_parser("new")
		newParser.add_argument("-p", "")\
		

		parser.add_argument("-p", "--path", default = "")
		parser.add_argument("-i", "--interpreter", default = "")
		parser.add_argument("-o", "--interpreter", default = "top")
		parser.add_argument("arguments", nargs = '*', default = list())
		return ppdk.Main(parser)
	except Exception as exception:
		Application.LogException(exception)
		Application.Exit(1)