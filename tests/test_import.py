try:
    from robustbase import Qn
    print("Importing Qn from robustbase... Success!")
except ImportError:
    print("Failed to import Qn from robustbase!")

try:
    from robustbase.stats import Qn as Qn_stat
    print("Importing Qn from robustbase.stats... Success!")
except ImportError:
    print("Failed to import Qn from robustbase.stats!")

try:
    from robustbase import Sn
    print("Importing Sn from robustbase... Success!")
except ImportError:
    print("Failed to import Sn from robustbase!")

try:
    from robustbase.stats import Sn as Sn_stat
    print("Importing Sn from robustbase.stats... Success!")
except ImportError:
    print("Failed to import Sn from robustbase.stats!")


