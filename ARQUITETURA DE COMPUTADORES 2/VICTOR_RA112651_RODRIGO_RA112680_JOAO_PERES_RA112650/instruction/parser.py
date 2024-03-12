from instruction.instruction import Instruction

class InstructionParser:
    
    def import_instructions(self, file_path) -> list:
        instructions_txt = []
        
        with open(file_path, 'r') as f:
            for line in f:
                instructions_txt.append(line)
        
        instructions = []
        
        for txt in instructions_txt:
            instructions.append(self.parse_to_instruction(txt))
            
        return instructions
            
    def handle_txt_formats(self, txt: str) -> str:
        txt = txt.strip()
        txt = txt.replace(', ', ' ')
        txt = txt.replace(',', ' ')
        
        return txt

    def parse_to_instruction(self, txt: str):
        txt = self.handle_txt_formats(txt)
        args = txt.split(' ')
    
        return Instruction(*args)
    
# teste para importar instrucoes do teste1.txt
if __name__ == '__main__':
    parser = InstructionParser()
    instructions = parser.import_instructions("instruction/test/teste2.txt")
    for instruction in instructions:
        print(instruction, end='\n\n')