# ALUNOS: VICTOR HUGO DO NASCIMENTO, RODRIGO VIEIRA, JOÃO PEDRO PERES

from instruction.parser import InstructionParser
from instruction.instruction import Instruction

clock = 1

class Register:
    status: str
    value: int
    
    def __init__(self):
        self.status = None
        self.value = 0
        
    def __str__(self):
        return f'status: {self.status}, value: {self.value}'

class ReservationStation:
    op: str = None # operacao
    destination: str = None # representa o registrador destino
    vj: str = None # representa o valor pronto
    vk: str = None
    qj: str = None # se o valor estiver sendo calculado ainda
    qk: str = None
    addr: int = None # para operacoes de laod/store
    busy: bool = False
    time_left: int = 0 # ciclos restantes
    type: str
    
    def __init__(self, type):
        self.type = type
        
    def __str__(self):
        return f'op: {self.op}\nvj: {self.vj}\nvk: {self.vk}\nqj: {self.qj}\nqk: {self.qk}\naddr: {self.addr}\nbusy: {self.busy}\ntime_left: {self.time_left}\ntype: {self.type}'
    
    def is_busy(self):
        return self.busy

    # retorna se o valor esta pronto para ser utilizado e se ele existe nos registradores
    def value_is_ready(self, key):
        register = registers.get(key, -1)
        
        if register == -1: 
            return True, False # registrador nao existe
                
        return register.status == None, True

    def load_values(self, op2, op3=0):
        ready, in_register = self.value_is_ready(op2)
        
        if ready and in_register:
            self.vj = registers[op2].value
            self.qj = None
        elif ready and not(in_register):
            self.vj = op2
            self.qj = None
        else:
            self.vj = None
            self.qj = op2

        ready, in_register = self.value_is_ready(op3)
        
        if ready and in_register:
            self.vk = registers[op3].value
            self.qk = None
        elif ready and not(in_register):
            self.vk = op3
            self.qk = None
        else:
            self.vk = None
            self.qk = op3
            
    def load_memory_values(self, op2, addr):
        self.load_values(op2)
        self.addr = addr
        
    def load_instruction(self, instruction: Instruction):
        if not self.is_busy():
            self.busy = True
            self.op = instruction.oper
            
            match instruction.oper:
                case 'addi' | 'add' | 'sub' | 'subi' | 'mul' | 'div' | 'and' | 'or' | 'blt' | 'bgt' | 'beq' | 'bne':
                    self.load_values(instruction.op2, instruction.op3)
                    
                case 'not':
                    self.load_values(instruction.op2)
                    
                case 'lw' | 'sw':
                    self.load_memory_values(instruction.op2, instruction.addr)
                    
                case 'j':
                    self.load_values(instruction.op1)                
                    
                case _:
                    return 
            
            self.destination = instruction.op1     
            self.time_left = instruction.clocks
    
    def calculate(self):
        match self.op:
            case 'addi' | 'add':
                registers[self.destination].value = int(self.vj) + int(self.vk)
            
            case 'subi' | 'sub':
                registers[self.destination].value = int(self.vj) - int(self.vk)
            
            case 'mul':
                registers[self.destination].value = int(self.vj) * int(self.vk)
                
            case 'div':
                registers[self.destination].value = int(int(self.vj)/int(self.vk))
            
            case 'and':
                registers[self.destination].value = int(self.vj) & int(self.vk)
                
            case 'or':
                registers[self.destination].value = int(self.vj) | int(self.vk)
            
            case 'not':
                registers[self.destination].value = ~int(self.vj)
            
            case 'lw':
                registers[self.destination].value = memory[int(self.vj) + int(self.addr)] 
                
            case 'sw':
                memory[int(self.vj) + int(self.addr)] = int(registers[self.destination].value)
                
            case 'j':
                queue.update_pc(int(self.vk) - 1)
                dispatch_queue.instructions = dispatch_queue.instructions[:dispatch_queue.pc]
                
                
            case 'blt':
                if int(registers[self.destination].value) < int(self.vj):
                    queue.update_pc(int(self.vk) - 1)
                    dispatch_queue.instructions = dispatch_queue.instructions[:dispatch_queue.pc]
                    
            case 'bgt':
                if int(registers[self.destination].value) > int(self.vj):
                    queue.update_pc(int(self.vk) - 1)
                    dispatch_queue.instructions = dispatch_queue.instructions[:dispatch_queue.pc]
                    
            case 'beq':
                if int(registers[self.destination].value) == int(self.vj):
                    queue.update_pc(int(self.vk) - 1)
                    dispatch_queue.instructions = dispatch_queue.instructions[:dispatch_queue.pc]
                    
            case 'bne':
                if int(registers[self.destination].value) != int(self.j):
                    queue.update_pc(int(self.vk) - 1)
                    dispatch_queue.instructions = dispatch_queue.instructions[:dispatch_queue.pc]
                    
            case _:
                return
            
        registers[self.destination].status = None
            
    def process(self):
        self.calculate()
        self.busy = False
        self.destination = None
        self.op = None
        self.vj = None
        self.vk = None
        self.addr = None
            
    def update(self, key):
        if not self.is_busy():
            return

        else:
            if registers[self.destination].status == None:
                registers[self.destination].status = key
            
            if registers[self.destination].status == key:
                if self.vj != None != self.vk:
                    if self.time_left > 0:
                        self.time_left -= 1
                                        
                    else:
                        self.process()
                    
                else:
                    
                    if self.qj != None and (registers[self.qj].status == None or registers[self.qj].status == key):
                        self.vj = registers[self.qj].value
                        self.qj = None
                    
                    if self.qk != None and (registers[self.qk].status == None or registers[self.qk].status == key):
                        self.vk = registers[self.qk].value
                        self.qelemsk = None 

class InstructionQueue:
    instructions: list
    pc: int
    
    def __init__(self):
        self.instructions = []
        self.pc = 0
    
    def load(self, path):
        parser = InstructionParser()
        self.instructions = parser.import_instructions(path)
        
    def add_instruction(self, instruction):
        if instruction != None:
            self.instructions.append(instruction)
        
    def get_instruction(self):
        if not self.reached_end():
            return self.instructions[self.pc]
    
    def next_instruction(self):
        if not self.reached_end():
            self.pc += 1
    
    def update_pc(self, i: int):
        if i < len(self.instructions) and i > -1:
            self.pc = i
    
    def reached_end(self):
        return self.pc >= len(self.instructions)
    
def print_registers(i):
    print('registers:')
    for i in range(i): print(f'r{i}:',registers[f'r{i}'])
    print()
    
def print_memory(i):
    print('memory:', memory[:i])
    
def available_reservation_station(type):
    for key, rs in reservation_stations.items():   
        if not (rs.is_busy()) and rs.type == type: 
            return key, rs
    
    return None, None

def is_any_rs_busy():
    for rs in reservation_stations.values():
        if rs.is_busy():
            return True
        
    return False

def print_clock():
    print(f'=====================\nclock: {clock}\n')

# inicializa os registradores
registers = {}

for i in range(32):
    key = f'r{i}'
    value = Register()
    registers[key] = value
    
# inicializa  a memoria
memory = [0 for _ in range(512)]
                    
#incializa as estacoes de reserva
reservation_stations = {
    'add1' : ReservationStation('ADD/SUB'),
    # 'add2' : ReservationStation('ADD/SUB'),
    # 'add3' : ReservationStation('ADD/SUB'),
    'muldiv1' : ReservationStation('MUL/DIV'),
    # 'muldiv2' : ReservationStation('MUL/DIV'),
    # 'muldiv3' : ReservationStation('MUL/DIV'),
    'ls1' : ReservationStation('MEMORY')
    # 'ls2' : ReservationStation('MEMORY'),
    # 'ls3' : ReservationStation('MEMORY')
}

# inicializa fila de instrucoes e de despacho
queue = InstructionQueue()
queue.load('instruction/test/teste1.txt')
dispatch_queue = InstructionQueue()

print_clock()
while(not queue.reached_end() or not dispatch_queue.reached_end() or is_any_rs_busy()):
    searched_instruction = queue.get_instruction()
    
    if searched_instruction != None:
        queue.next_instruction()
        print(f'searched instruction:\n{searched_instruction}\n')
        
    instruction: Instruction = dispatch_queue.get_instruction()
    rs = None
    if instruction != None:
        key, rs = available_reservation_station(instruction.type)
        
    if rs != None:
        print(f'dispatched instruction:\n{instruction}\n')
        dispatch_queue.next_instruction()
        rs.load_instruction(instruction)
        
        match instruction.oper:
            case 'blt' | 'bgt' | 'beq' | 'bne' | 'j':
                while rs.is_busy():
                    for key, rs2 in reservation_stations.items():
                        print(f'{key}\n{rs2}\n')
                        rs2.update(key)
                        
                    print_registers(6)
                    print_memory(6)
                    
                    clock += 1
                    print_clock()
                                
                continue
            
    print('reservation stations:')
    for key, rs in reservation_stations.items():
        print(f'{key}\n{rs}\n')
        rs.update(key)
        
    print_registers(6)
    print_memory(6)
    
    dispatch_queue.add_instruction(searched_instruction)
    clock += 1
    print_clock()