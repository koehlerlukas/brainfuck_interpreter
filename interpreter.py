import argparse
import readchar

class BrainfuckInterpreter:

    def __init__(self, input_script):
        self._pointer = 0 
        self._cells = [0]
        self._script = self._read_script(input_script)
    
    def _check_code(self, code):
        brackets = 0
        for c in code:
            if c == '[':
                brackets += 1
            elif c == ']':
                brackets -= 1
            
            if brackets < 0 or brackets > 1:
                print('Two dimensional loop not yet implemented.')
                exit(1)

    def _read_script(self, input_script: str) -> list:
        allowed_operators = ['>', '<', '+', '-', '.', ',', '[', ']']
        result = []
        try:
            with open(input_script, "r") as file:
                for c in file.read():
                    if c in allowed_operators:
                        result.append(c)
        except Exception:
            print('Error reading input file.')
            exit(1)

        self._check_code(result)
        return result

    def _execute(self):
        
        opening = -1
        closing = -1 
        
        i = 0
        while i < len(self._script):

            if self._script[i] == '>':
                self._pointer += 1
                if len(self._cells) == self._pointer:
                    self._cells.append(0)

            elif self._script[i] == '<':
                self._pointer = 0 if self._pointer <= 0 else self._pointer - 1

            elif self._script[i] == '+':
                self._cells[self._pointer] +=  1

            elif self._script[i] == '-':
                self._cells[self._pointer] -=  1

            elif self._script[i] == '.':
                print(chr(self._cells[self._pointer]))

            elif self._script[i] == ',':
                self._cells[self._pointer] = ord(readchar.readchar())

            elif self._script[i] == '[':
                opening = i
                if self._cells[self._pointer] == 0 and closing != -1:
                    i = closing + 1

            elif self._script[i] == ']':
                closing = i 
                if self._cells[self._pointer] != 0 and opening != -1:
                    i = opening + 1
            i += 1

    def run(self):
        self._execute()
        

def main():
    parser = argparse.ArgumentParser(description='Interpret your brainfuck script.')
    parser.add_argument('-s', action='store', type=str, required=True, help='Path to your script.')
    args = parser.parse_args()

    BrainfuckInterpreter(args.s).run()


if __name__ == '__main__':
    main()    
    