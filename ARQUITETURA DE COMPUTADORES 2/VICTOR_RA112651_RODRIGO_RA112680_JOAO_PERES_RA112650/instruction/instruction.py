clocks_by_instruction = {
    'mul': 15,
    'div': 25
}

instructions_by_type = {
    'ADD/SUB': ['add', 'addi', 'sub', 'subi', 'and', 'or', 'not', 'blt', 'bgt', 'beq', 'bne', 'j'],
    'MUL/DIV': ['mul', 'div'],
    'MEMORY': ['lw', 'sw']
}

class Instruction:
    oper : str
    op1 : str
    op2 : str
    op3 : str
    addr: str
    type : str
    clocks : int
    
    def __init__(self, oper, op1, op2=None, op3=None):
        self.oper = oper
        
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        
        self.addr = None
        
        if oper == 'lw' or oper == 'sw':
            self.handle_memory_op()
        
        self.type = self.get_type()
        self.clocks = clocks_by_instruction.get(self.oper, 5)
        
    def __str__(self):
        return f"oper: {self.oper}\nop1: {self.op1}\nop2: {self.op2}\nop3: {self.op3}\naddr: {self.addr}\ntype: {self.type}\nclocks: {self.clocks}"
        
    def get_type(self):
        for type, instructions_list in instructions_by_type.items():
            if self.oper in instructions_list:
                return type
            
        return None
    
    def handle_memory_op(self):
       v1, v2 = self.op2.split('(')[:2]
       v2 = v2.replace(')', '')
       self.addr = v1
       self.op2 = v2