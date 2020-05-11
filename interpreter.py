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
            self._debug.append(("State: i =", i, ", script[i] =", self._script[i], ", pointer =", self._pointer, "cells[pointer] =", self._cells[self._pointer]))
            if self._script[i] == '>':
                self._pointer += 1
                if len(self._cells) == self._pointer:
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
                    print(chr(self._cells[self._pointer]))

            elif self._script[i] == ',':
                self._cells[self._pointer] = ord(readchar.readchar())

            elif self._script[i] == '[':
                i = self._start_loop(i)

            elif self._script[i] == ']':
                i = self._end_loop(i)
            i += 1

    
    def _start_loop(self, curr_pos: int) -> int:
        if self._cells[self._pointer] == 0:
            while curr_pos < len(self._script) - 1 and self._script[curr_pos] != ord(']'):
                curr_pos += 1
            if curr_pos < len(self._script) - 1 and self._script[curr_pos] == ord(']'): 
                curr_pos += 1
    
        return curr_pos



    def _end_loop(self, curr_pos: int) -> int:
        if self._cells[self._pointer] != 0:
            while self._script[curr_pos] != ord('[') and curr_pos > 0:
                curr_pos -= 1

        return curr_pos

    def run(self):
        self._execute()
        with open('./debug.txt', "w") as f:
            
        

def main():
    parser = argparse.ArgumentParser(description='Interpret your brainfuck script.')
    parser.add_argument('-s', action='store', type=str, required=True, help='Path to your script.')
    args = parser.parse_args()

    BrainfuckInterpreter(args.s).run()


if __name__ == '__main__':
    main()    
    