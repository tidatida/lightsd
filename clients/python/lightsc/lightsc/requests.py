# Copyright (c) 2016, Louis Opter <louis@opter.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from typing import (
    Any,
    List,
    TypeVar,
)


class Request:

    def __init__(self, *args: Any) -> None:
        self.params = args

RequestClass = TypeVar("RequestClass", bound=Request)


class SetLightFromHSBK(Request):

    def __init__(
        self,
        targets: List[str],
        h: float, s: float, b: float, k: int,
        transition_ms: int
    ) -> None:
        Request.__init__(self, targets, h, s, b, k, transition_ms)


class GetLightState(Request):

    def __init__(self, targets: List[str]) -> None:
        Request.__init__(self, targets)


class PowerOff(Request):

    def __init__(self, targets: List[str]) -> None:
        Request.__init__(self, targets)


class PowerOn(Request):

    def __init__(self, targets: List[str]) -> None:
        Request.__init__(self, targets)


class PowerToggle(Request):

    def __init__(self, targets: List[str]) -> None:
        Request.__init__(self, targets)


class SetWaveform(Request):

    def __init__(
        self,
        targets: List[str],
        waveform: str,
        h: float, s: float, b: float, k: int,
        period_ms: int,
        cycles: int,
        skew_ratio: float,
        transient: bool = True,
    ) -> None:
        Request.__init__(
            self,
            targets,
            waveform,
            h, s, b, k,
            period_ms,
            cycles,
            skew_ratio,
            transient,
        )
