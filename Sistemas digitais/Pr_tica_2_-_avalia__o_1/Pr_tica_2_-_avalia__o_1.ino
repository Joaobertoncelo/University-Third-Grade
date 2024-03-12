//#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#define LED1 PD6
#define LED2 PD7
#define BTN1 PD3
#define BTN2 PD2
#define INT_BTN1 PCINT19
#define INT_BTN2 PCINT18
#define tst_bit(Y,bit_x)(Y&(1<<bit_x))
#define cpl_bit(Y,bit_x)(Y^=(1<<bit_x))

ISR(PCINT0_vect) {
// determinar em qual pino (botão) houve mudança de sinal
if (!tst_bit(PORTD, PD7)) {
cpl_bit(PORTD, LED2);
}
_delay_ms(300);
}

ISR(PCINT1_vect) {
// determinar em qual pino (botão) houve mudança de sinal
if (!tst_bit(PORTD, PD6)) {
cpl_bit(PORTD, LED2);
}
_delay_ms(200);
}

int main() {
// configura os LEDs como saída e botões como entrada
DDRD &= 0x03;
DDRD |= (1<<LED1) | (1<<LED2);
// desliga os LEDs e liga o pull-up dos botões
PORTD &= 0x03;
PORTD |= (1<<BTN1) | (1<<BTN2);
// habilita interrupção por mudança de sinal no PORTD
PCICR = 1<<PCIE2;
// habilita interrupção nos botões
PCMSK2 = (1<<INT_BTN1) | (1<<INT_BTN2);
// habilita a chave geral das interrupções
sei();
while (1){
  cpl_bit(PORTD, LED1);
  };
}
