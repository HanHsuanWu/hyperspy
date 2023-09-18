# -*- coding: utf-8 -*-
# Copyright 2007-2023 The HyperSpy developers
#
# This file is part of HyperSpy.
#
# HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperSpy. If not, see <https://www.gnu.org/licenses/#GPL>.

from hyperspy.drawing.markers import Markers
from matplotlib.collections import LineCollection


class Lines(Markers):
    """A set of Line Segments Markers."""

    _key = "segments"

    def __init__(
        self, segments, transform="data", **kwargs
    ):
        """Initialize the set of Segments Markers.

        Parameters
        ----------
        segments : [n, 2, 2] array-like or ragged array with shape (n, 2,3) at every navigation position
            Defines the lines[[[x1,y1],[x2,y2]], ...] of the center of the ellipse.
        kwargs : dict
            Additional keyword arguments are passed to matplotlib.collections.LineCollection.

        Notes
        -----
        Unlike markers using ``offsets`` argument, the positions of the segments
        are defined by the ``segments`` argument and the tranform specifying the
        coordinate system of the ``segments`` is ``transform``.

        """
        if "offsets_transform" in kwargs and kwargs["offsets_transform"] != "display":
            raise ValueError(
                 "The offsets_transform argument is not supported for Lines Markers. Instead, "
                 "use the ``transform`` argument to specify the transform of the "
                 "markers.")
        kwargs["offsets_transform"] = "display"
        super().__init__(
            collection=LineCollection,
            segments=segments,
            transform=transform,
            **kwargs
        )
