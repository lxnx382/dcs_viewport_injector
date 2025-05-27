import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dcs_viewport_injector.injector import run_injection


if __name__ == "__main__":
    run_injection("config.json")
