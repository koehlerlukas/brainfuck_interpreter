import argparse
import readchar

class BrainfuckInterpreter:
    def __init__(self, input_script):
        self._allowed_operators = ['>', '<', '+', '-', '.', ',', '[', ']']
        self._pointer = 0 
        self._cells = [0]
        self._script = self._read_script(input_script)
        self._debug = []


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
        for i in range(len(self._script)):
            state = "State: i = " + str(i) + ", script[i] = " + str(self._script[i]) + ", pointer = " + str(self._pointer) + ", cells[pointer] = " + str(self._cells[self._pointer])
            self._debug.append(state)
            if self._script[i] == '>':
                self._pointer += 1
                if len(self._cells) ==  self._pointer:
                    self._cells.append(0)

            elif self._script[i] == '<':
                if self._pointer > 0:
                    self._pointer -= 1

            elif self._script[i] == '+':
                if len(self._cells) > self._pointer:
                    self._cells[self._pointer] +=  1

            elif self._script[i] == '-':
                if self._pointer > 0:
                    self._cells[self._pointer] -=  1

            elif self._script[i] == '.':
                if len(self._cells) > self._pointer:
                    print(self._cells[self._pointer])

            elif self._script[i] == ',':
                self._cells[self._pointer] = ord(readchar.readchar())

            elif self._script[i] == '[':
                if self._cells[self._pointer] == 0:
                    while i < len(self._script) and self._script[i] != ']':
                        i += 1
                    if i < len(self._script) and self._script[i] == ']':
                        i += 1

            elif self._script[i] == ']':
                if self._cells[self._pointer] != 0:
                    while self._script[i] != '[' and i > 0:
                        i -= 1
                
            
            i += 1


    def run(self):
        self._execute()
        with open('./debug.txt', "w") as f:
            for line in self._debug:
                f.write(line + "\n")
        

def main():
    parser = argparse.ArgumentParser(description='Interpret your brainfuck script.')
    parser.add_argument('-s', action='store', type=str, required=True, help='Path to your script.')
    args = parser.parse_args()

    BrainfuckInterpreter(args.s).run()


if __name__ == '__main__':
    main()    
    