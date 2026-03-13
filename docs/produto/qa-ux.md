# QA — UX

Casos de teste focados em fluxos e interações do usuário.

## Booking Público

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| 1 | Acessar link de agendamento válido | Exibe perfil do profissional e serviços disponíveis |
| 2 | Acessar link de agendamento inválido | Exibe página de erro adequada |
| 3 | Selecionar serviço e data | Exibe apenas horários disponíveis |
| 4 | Tentar agendar horário já ocupado | Horário não aparece na lista |
| 5 | Preencher nome e telefone e confirmar | Agendamento criado, cliente recebe WhatsApp |
| 6 | Submeter sem preencher campos obrigatórios | Exibe validação nos campos |
| 7 | Agendar fora do horário de funcionamento | Horário não aparece na lista |

## Notificações WhatsApp

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| 1 | Agendamento confirmado | Cliente recebe mensagem imediatamente |
| 2 | 24h antes do horário | Cliente recebe lembrete automático |
| 3 | Agendamento cancelado | Cliente recebe notificação de cancelamento |
