#What is the difference between `import math` and `from math import pi`?

#| Feature                  | `import math`         | `from math import pi`     |

#| Imports                  | Whole module          | Only `pi`                 |
#| Access via module prefix | Yes (`math.pi`)       | No (`pi` directly)        |
#| Memory usage             | Slightly more         | Slightly less             |
#| Namespace pollution      | Minimal (only `math`) | More (adds `pi` directly) |
