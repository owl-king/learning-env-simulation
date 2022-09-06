# Simulate env for your learning 

## Requirements
- python3

# Installation
```bash
git clone  https://github.com/owl-king/learning-env-simulation 
```

# Usage
python3 main.py -h
```bash
usage: main.py [-h] [--module MODULE] [--tool TOOL]
               [--action {create,clean,question,answer}]

Emulate environment for your learning tasks

optional arguments:
  -h, --help            show this help message and exit
  --module MODULE       The module you want to practice
  --tool TOOL           The tool you want to emulate environment
  --action {create,clean,question,answer}
                        Action you want to performs? (create|clean)
```

To practice `find`:
```bash
# To create env
python3 main.py --module tools --tool find --action create

# View env with tree
tree ./env
# Or with exa
exa -T ./env
```

To clean up `find` env:
```bash
python3 main.py --module tools --tool find --action clean
```

To get sample questions for `find` tool:
```bash
python3 main.py --module tools --tool find --action question
```

To get an answer for a sample question :
```bash
python3 main.py --module tools --tool find --action answer 
```

# Roadmap
- [x] find
