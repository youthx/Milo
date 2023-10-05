import argparse 
import src


parser = argparse.ArgumentParser(description="Milo is a python virtual environment.")

parser.add_argument('--init', '-i', type=str,
                    help="The name of your project.")

parser.add_argument('--assets', '-a', action="store_true",
                    help="Adds asset support.")

args = parser.parse_args()

if __name__ == "__main__":
    if args.init:
        src.builder.create_default_environment(args.init, args.assets)
    