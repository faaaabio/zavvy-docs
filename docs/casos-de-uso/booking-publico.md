# Booking Público

**URL:** `booking.zavvy.com.br/:slug`

Página pública de agendamento. O cliente acessa sem precisar criar conta ou instalar nada.

---

## Objetivo

Permitir que qualquer cliente agende um horário com o profissional a qualquer hora do dia, a partir de um link ou QR Code compartilhado.

---

## Atores

| Ator | Descrição |
|------|-----------|
| Cliente | Pessoa que quer agendar um horário |
| Profissional | Quem recebe o agendamento (não interage diretamente nesse fluxo) |

---

## Fluxo principal

1. Cliente acessa o link de agendamento (`booking.zavvy.com.br/seunome`)
2. Visualiza o perfil do profissional e os serviços disponíveis
3. Seleciona o serviço desejado
4. Escolhe a data disponível
5. Escolhe o horário disponível
6. Preenche nome e telefone (WhatsApp)
7. Confirma o agendamento
8. Recebe confirmação automática no WhatsApp

---

## Regras

- Apenas horários dentro da disponibilidade configurada pelo profissional aparecem
- Horários já ocupados não são exibidos
- O cliente não precisa criar conta
- O telefone informado é usado para envio das notificações via WhatsApp

---

## Resultado

- Agendamento criado e visível na agenda do profissional
- Cliente recebe mensagem de confirmação no WhatsApp
- Cliente recebe lembrete automático 24h antes do horário
