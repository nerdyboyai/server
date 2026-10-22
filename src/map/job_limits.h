/*
===========================================================================

  Copyright (c) 2025 LandSandBoat Dev Teams

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see http://www.gnu.org/licenses/

===========================================================================
*/

#pragma once

// Number of job slots, including NONE (0) and MON (23). Slot 24 is the first custom job.
#define MAX_JOBTYPE 25

// Job slots the wire formats carry (0-31). The unlocked-job mask is 32 bits, so this is the
// ceiling for job IDs without a larger change. Packet arrays use this size and fill only
// entries below MAX_JOBTYPE. The custom client must read the same width.
#define MAX_PACKET_JOBTYPE 32

static_assert(MAX_JOBTYPE <= MAX_PACKET_JOBTYPE, "MAX_JOBTYPE must fit in the packet job arrays");
