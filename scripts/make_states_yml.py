#!/usr/bin/env python3
#
# MAKE STATES.YML CONTENT
#

import math
from collections import defaultdict

from pg import *

states: dict[str, str] = make_state_names()

print("states:")
for xx in study_states:
    name: str = states[xx]
    print("- xx:", xx)
    print("  name:", name)
    print("  official:", officials_copy[xx])
    for label, id in notables_copy[xx].items():
        print("  {}: {}".format(label, id))
    print("  baseline:", baseline_maps[xx])
    print("  ready:", "false")

pass
