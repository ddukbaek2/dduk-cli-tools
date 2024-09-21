#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Callable, Iterator, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
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
		return ppdk.Main(arguments[1:])
	except Exception as exception:
		Application.LogException(exception)
		Application.Exit(1)