#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Callable, Iterator, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import sys
from dduk.application.predefinedsymbols import PredefinedSymbols
from dduk.application.application import Application


#--------------------------------------------------------------------------------
# 패키지 메인 함수.
#--------------------------------------------------------------------------------
def Main(arguments : list[str]) -> int:
	Application.Log("pdk")
	return 0