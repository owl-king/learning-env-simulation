import argparse
import importlib
import pathlib
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Emulate environment for your learning tasks')
    parser.add_argument("--module", help="The module you want to practice")
    parser.add_argument("--tool", help="The tool you want to emulate environment")
    parser.add_argument("--action", help="Action you want to performs? (create|clean)", choices=['create', 'clean', 'question', 'answer'])

    if len(sys.argv) > 1:
        args = parser.parse_args()
        module_name = args.module + "." + args.tool
        module = importlib.import_module(module_name)
        action = args.action.lower().strip()
        if action == 'create':
            module.build_env(pathlib.Path().resolve())
        if action == 'clean':
            module.clean_up_env(pathlib.Path().resolve())
        if action == 'question':
            module.questions()
        if action == 'answer':
            module.answer()
