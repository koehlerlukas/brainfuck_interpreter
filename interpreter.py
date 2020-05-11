import argparse
import readchar

class BrainfuckInterpreter:
    def __init__(self, input_script):
        self._allowed_operators = ['>', '<', '+', '-', '.', ',', '[', ']']
        self._pointer = 0 
        self._cells = [0]
        self._script = self._read_script(input_script)


    def _read_script(self, input_script: str) -> list:
        res = []
        try:
            with open(input_script, "r") as file:
                for c in file.read():
                    if c in self._allowed_operators:
                        res.append(c)
        except Exception:
            print('Error reading input file.')
            exit(1)
        
        return res

    def _execute(self):
        for c in self._script:
            if c == '>':
                self._pointer += 1
                if len(self._cells) == self._pointer:
                    self._cells.append(0)
            elif c == '<':
                if self._pointer > 0:
                    self._pointer -= 1
            elif c == '+':
                if len(self._cells) > self._pointer:
                    self._cells[self._pointer] += 1
            elif c == '-':
                if len(self._cells) > self._pointer:
                    self._cells[self._pointer] -= 1
            elif c == '.':
                if len(self._cells) > self._pointer:
                    print(self._cells[self._pointer])
            elif c == ',':
                self._cells[self._pointer] = ord(self._read_input())
            elif c == '[':
                pass
            elif c == ']':
                pass
    
    def _read_input(self):
        value = readchar.readchar()
        print(ord(value))
        return value

    def _start_loop(self):
        pass

    def _end_loop(self):
        pass
    
    def run(self):
        self._execute()
        

def main():
    parser = argparse.ArgumentParser(description='Interpret your brainfuck script.')
    parser.add_argument('-s', action='store', type=str, required=True, help='Path to your script.')
    args = parser.parse_args()

    BrainfuckInterpreter(args.s).run()


if __name__ == '__main__':
    main()    
    