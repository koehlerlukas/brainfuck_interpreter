import argparse

class BrainfuckInterpreter:
    def __init__(self, input_script):
        self._input = input_script
        self._allowed_chars = ['>', '<', '+', '-', '.', ',', '[', ']'] 

    def _read(self):
        res = []
        try:
            with open(self._input, "r") as file:
                for c in file.read():
                    if c in self._allowed_chars:
                        res.append(c)
        except:
            print('Error reading input file.')
            exit(1)
        
        self._script = res

    def _execute(self):
        ptr = 0
        for c in self._script:
            if c == '>':
                pass
            elif c == '<':
                pass
            elif c == '+':
                pass
            elif c == '-':
                pass
            elif c == '.':
                pass
            elif c == ',':
                pass
            elif c == '[':
                pass
            elif c == '}':
                pass
    
    def run(self):
        self._read()
        self._execute()
        

def main():
    parser = argparse.ArgumentParser(description='Interpret your brainfuck script.')
    parser.add_argument('-s', action='store', type=str, required=True, help='Path to your script.')
    args = parser.parse_args()

    BrainfuckInterpreter(args.s).run()


if __name__ == '__main__':
    main()    
    