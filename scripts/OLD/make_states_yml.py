#!/usr/bin/env python3
#
# MAKE STATES.YML CONTENT
#

from pg import *

states: dict[str, str] = STATE_NAMES

print("states:")
for xx in study_states:
    name: str = states[xx]
    # print("{}:".format(xx))
    print("- xx:", xx)
    print("  name:", name)
    print("  official:", officials_copy[xx])
    for label, id in notables_copy[xx].items():
        print("  {}: {}".format(label, id))
    print("  baseline:", baseline_maps[xx])
    print("  ready:", "false")

pass
