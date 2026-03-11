# Documentação — Zavvy

> Site: https://zavvy.com.br
> App: https://app.zavvy.com.br
> Data da captura: 2026-03-11
> Capturas de tela: pasta `screenshots/`

---

## Visão Geral

**Zavvy** é uma plataforma de agenda inteligente com confirmação automática pelo WhatsApp, voltada para profissionais autônomos que trabalham com agendamentos.

**Tagline:** _"Seus clientes nunca mais vão faltar."_

**Proposta de valor central:** O cliente recebe mensagem de confirmação no momento do agendamento e 24h antes do horário. Ele confirma ou remarca direto no WhatsApp — e a agenda do profissional atualiza sozinha.

---

## Estrutura de Páginas

| Página | URL | Screenshot |
|--------|-----|------------|
| Home | `https://zavvy.com.br/` | `screenshots/home/` |
| Termos de Uso | `https://zavvy.com.br/termos-de-uso` | `screenshots/termos-de-uso/full-page.png` |
| Política de Privacidade | `https://zavvy.com.br/politica-de-privacidade` | `screenshots/politica-de-privacidade/full-page.png` |
| Login (app externo) | `https://app.zavvy.com.br/login` | — |
| Cadastro (app externo) | `https://app.zavvy.com.br/signup` | — |

---

## Home Page (`/`)

A home page é um **single-page** com navegação por âncoras. Contém 7 seções principais.

### Navegação (Header)

| Item | Âncora/Link |
|------|-------------|
| WhatsApp | `#whatsapp-demo` |
| Como Funciona | `#como-funciona` |
| Preço | `#preco` |
| FAQ | `#faq` |
| Entrar | `https://app.zavvy.com.br/login` |
| Testar grátis | `https://app.zavvy.com.br/signup` |

---

### Seção 1 — Hero
**Screenshot:** `screenshots/home/01-hero.png`

- Headline: _"Seus clientes nunca mais vão faltar. Confirmação automática pelo WhatsApp."_
- Descrição: O cliente recebe mensagem na confirmação e 24h antes, confirma ou remarca direto no WhatsApp, e a agenda atualiza sozinha.
- CTAs: **"Testar grátis por 14 dias"** | **"Já tenho conta"**
- Diferenciais em destaque:
  - Sem cartão de crédito
  - Pronta em 3 minutos
  - Para qualquer profissional que trabalha com agendamento

---

### Seção 2 — WhatsApp Demo (`#whatsapp-demo`)
**Screenshot:** `screenshots/home/02-whatsapp-demo.png`

Demonstração visual (mock de conversa WhatsApp) mostrando:
- Mensagem automática enviada ao cliente lembrando do horário
- Cliente responde `1` para confirmar ou `2` para remarcar
- Sistema confirma ou oferece novos horários automaticamente

**Problemas que o Zavvy resolve (apresentados nesta seção):**
| Problema | Descrição |
|----------|-----------|
| Cliente marca e não aparece | Sem confirmação, 30% dos clientes simplesmente não vêm |
| Dia inteiro no WhatsApp confirmando | Processo manual e esquecido |
| Agenda no caderno ou na cabeça | Risco de conflitos e duplo agendamento |
| Cliente manda mensagem à meia-noite | Sem sistema online, o profissional fica de plantão |

---

### Seção 3 — Como Funciona (`#como-funciona`)
**Screenshot:** `screenshots/home/03-como-funciona.png`

4 passos para começar:

| Passo | Ação | Descrição |
|-------|------|-----------|
| 1 | Cadastre seus serviços | Consulta, sessão, aula — com duração e preço. Em 3 minutos no ar. |
| 2 | Conecte o WhatsApp | Integração simples para envio de confirmações automáticas. |
| 3 | Compartilhe seu link | Cole no Instagram, WhatsApp Status ou cartão de visitas. Clientes agendam 24h. |
| 4 | Relaxe | Confirmação 24h antes, remarcação automática, agenda sempre atualizada. |

**Públicos-alvo mencionados:**
- Psicólogos e Terapeutas
- Nutricionistas
- Personal Trainers
- Advogados e Consultores
- Profissionais de Beleza (corte, manicure, estética)
- Professores Particulares
- Qualquer profissional autônomo com horários marcados

---

### Seção 4 — Funcionalidades (`#funcionalidades`)
**Screenshot:** `screenshots/home/04-funcionalidades.png`

| Funcionalidade | Descrição |
|----------------|-----------|
| Confirmação automática pelo WhatsApp | Mensagem na confirmação e 24h antes; agenda atualiza sozinha |
| Link de agendamento 24h | Clientes agendam a qualquer hora sem precisar contatar o profissional |
| Google Calendar sincronizado | Compromissos pessoais bloqueiam horários automaticamente |
| Remarcação pelo WhatsApp | Cliente remarca direto na conversa, sem incomodar o profissional |
| Gestão de clientes | Histórico completo de cada cliente |
| App no celular (PWA) | Acesso de qualquer lugar com experiência de app nativo |
| Relatórios simples | Agendamentos, faltas e cancelamentos do mês |
| Google Meet automático | Link gerado e enviado automaticamente para atendimentos online |
| Seguro (LGPD) | Dados protegidos com criptografia e conformidade LGPD |

---

### Seção 5 — Preço (`#preco`)
**Screenshot:** `screenshots/home/05-preco.png`

**Plano único:** Profissional

| | Valor |
|--|-------|
| Preço promocional de lançamento | **R$ 20/mês** (por 12 meses) |
| Preço regular | R$ 49,90/mês |
| Mensagens WhatsApp (cobradas à parte) | R$ 0,25 por mensagem |

**O que está incluso:**
- Confirmação automática pelo WhatsApp
- Remarcação pelo WhatsApp
- Link de agendamento personalizado
- Sincronização com Google Calendar
- Lembretes automáticos ilimitados
- Gestão de clientes
- Relatórios e métricas
- Suporte por email

**Custo de mensagens:** Cada agendamento gera 2 mensagens (confirmação + lembrete 24h antes).
Exemplo: 30 clientes/mês = R$ 15,00 em mensagens.

**Observações:** Cancele quando quiser. Sem fidelidade. Restam 49 vagas (promoção de lançamento).

---

### Seção 6 — FAQ (`#faq`)
**Screenshot:** `screenshots/home/06-faq.png`

Perguntas frequentes abordadas:

1. Como funciona a confirmação pelo WhatsApp?
2. A mensagem vai do meu número ou do Zavvy?
3. Meu cliente precisa baixar algum app?
4. Quanto custa o Zavvy?
5. Quanto custa a mensagem pelo WhatsApp?
6. Funciona para equipes com mais de um profissional?
7. E se o cliente não responder a confirmação?
8. Como funciona o link do Google Meet?
9. Como começo a usar?
10. Meus dados estão seguros?

---

### Seção 7 — Footer / CTA Final
**Screenshot:** `screenshots/home/07-footer.png`

- CTA final: _"Seu próximo cliente não vai faltar"_
- Sub: _"Comece hoje. Em 3 minutos sua agenda está no ar com confirmação automática pelo WhatsApp."_
- Botão: **"Começar meu teste grátis"**
- Links no rodapé: [Termos de Uso](/termos-de-uso) | [Política de Privacidade](/politica-de-privacidade)

---

## Página: Termos de Uso (`/termos-de-uso`)
**Screenshot:** `screenshots/termos-de-uso/full-page.png`

Página com os termos legais de uso da plataforma Zavvy.

---

## Página: Política de Privacidade (`/politica-de-privacidade`)
**Screenshot:** `screenshots/politica-de-privacidade/full-page.png`

Página com a política de privacidade e conformidade LGPD da plataforma Zavvy.

---

## Estrutura de Arquivos (Screenshots)

```
screenshots/
├── home/
│   ├── 01-hero.png               # Seção inicial / headline principal
│   ├── 02-whatsapp-demo.png      # Demo de conversa WhatsApp + problemas
│   ├── 03-como-funciona.png      # 4 passos + públicos-alvo
│   ├── 04-funcionalidades.png    # Lista de funcionalidades
│   ├── 05-preco.png              # Planos e preços
│   ├── 06-faq.png                # Perguntas frequentes
│   └── 07-footer.png             # CTA final e rodapé
├── termos-de-uso/
│   └── full-page.png             # Página completa dos termos de uso
└── politica-de-privacidade/
    └── full-page.png             # Página completa da política de privacidade
```

---

## Identidade Visual

| Elemento | Detalhe |
|----------|---------|
| Logo | "zavvy" (minúsculas, tipografia verde) |
| Cor primária | Verde (#1DB954 aproximado) |
| Fundo | Off-white claro |
| Tipografia | Sans-serif moderna, bold nos headlines |
| Estilo | Minimalista, clean, voltado para conversão |

---

## Notas Técnicas (Site)

- Site construído como **landing page de uma única página** (`/`) com seções acessadas via âncoras
- App separado em subdomínio: `app.zavvy.com.br`
- Mensagens WhatsApp via API (cobradas por mensagem enviada)
- Integração com Google Calendar e Google Meet
- Conformidade com LGPD mencionada explicitamente
- PWA (Progressive Web App) para acesso mobile

---

---

# Documentação do App — `app.zavvy.com.br`

> Explorado em sessão autenticada em 2026-03-11
> Screenshots: `screenshots/app/`

## Visão Geral do App

Aplicação web (PWA) acessível via `app.zavvy.com.br`. Interface com sidebar fixa de navegação à esquerda.

**Usuário de teste:** Fabio da Silva Lino (`fabiosl@gmail.com`) — Plano **Starter** (em período de teste)
**Link de agendamento público:** `booking.zavvy.com.br/ofabio`

---

## Estrutura de Navegação (Sidebar)

| Item | Rota | Descrição |
|------|------|-----------|
| Home | `/dashboard` | Dashboard com resumo da semana |
| Agenda | `/agenda` | Calendário de agendamentos |
| Clientes | `/clients` | Lista e perfil de clientes |
| Configurações | `/settings` | Configurações gerais da conta |
| + Novo Agendamento | — | Botão de ação principal (verde) |
| Compartilhar Link | — | Atalho para link/QR Code |

---

## Tela: Dashboard (`/dashboard`)

**Screenshot:** `screenshots/app/dashboard/01-home.png`

### Elementos presentes:
- **Alerta de pendentes:** Banner amarelo indicando agendamentos sem confirmação do dia
- **Seção "Próximos":** Lista de próximos agendamentos (ou CTA para compartilhar link se vazia)
- **Link de agendamento:** `booking.zavvy.com.br/ofabio` com botões "Copiar link" e "QR Code"
- **Resumo semanal** (cards):
  - Agendados (com breakdown: confirmados / pendentes)
  - Concluídos
  - Cancelados
  - Não compareceram
- **Resumo semanal em gráfico:** Período exibido no rodapé (ex: "9 de mar. – 15 de mar.")

---

## Tela: Agenda (`/agenda`)

**Screenshot:** `screenshots/app/agenda/`

### Views disponíveis:
| View | Descrição |
|------|-----------|
| Dia | Visão horária de um único dia |
| Semana | Visão semanal (padrão) — colunas SEG a DOM |
| Lista | Listagem cronológica de agendamentos |

### Navegação:
- Setas `<` `>` para semana anterior/próxima
- Data atual destacada em verde

### Card de agendamento (na grade):
- Horário + nome do cliente + nome do serviço
- Cor: verde para confirmados, amarelo para pendentes

### Modal "Detalhes do agendamento":
Aberto ao clicar em um agendamento. Contém:

| Campo | Detalhe |
|-------|---------|
| Status badge | Pendente / Confirmado / Concluído / Cancelado |
| Data e hora | Ex: Quarta-feira, 11 Março 2026, 10:00 – 11:00 (1h) |
| Cliente | Nome + telefone + botão WhatsApp |
| Serviço | Nome + duração + valor ("A combinar" se sem preço fixo) |
| Ações | Concluir · Remarcar horário · Não compareceu · Cancelar |

---

## Tela: Clientes (`/clients`)

**Screenshot:** `screenshots/app/clientes/`

### Lista de clientes:
- **Busca** por nome
- **Filtros:** Todos · Agendados · Inativos · Ordenar (Mais recente)
- **Cards de resumo:** Total · Agendados · Atendimentos (total histórico)
- **Colunas da tabela:** Cliente · Telefone · Último Atendimento · Próximo · Atendimentos · (ícone WhatsApp)

### Perfil do cliente (`/clients/:id`):

**Informações básicas:**
- Avatar com iniciais + Nome + Telefone
- Contador: `N visitas` · `N agendados`
- Ações rápidas: **WhatsApp** · **Ligar** · **Agendar**
- Ícone de editar perfil (canto superior direito)

**Abas do perfil:**

#### Aba: Histórico
- **PRÓXIMOS:** agendamentos futuros com status badge, serviço, ações (Concluir / Cancelar)
- **ANTERIORES:** agendamentos passados com status (Concluído, Cancelado, etc.)

#### Aba: Mensagens
- Conversa de WhatsApp trocada com o cliente via Zavvy

#### Aba: Anotações
- **Anotações Privadas** — campo livre, visível apenas para o profissional
- Cliente não tem acesso a essas informações
- Botão `+` para criar nova anotação
- Estado vazio: "Nenhuma anotação ainda" + CTA "Criar primeira anotação"

### Gaps identificados (vs. clínica):
> O perfil atual armazena apenas nome, telefone e anotações livres.
> Não há campos estruturados para dados clínicos (anamnese, diagnóstico, convênio, data de nascimento).

---

## Tela: Configurações (`/settings`)

**Screenshot:** `screenshots/app/configuracoes/`

### Seção: Perfil do usuário
- Avatar + Nome + Profissão (ex: "Designer de produto") + Status (badge "Teste")
- Clicável → editar perfil

### Seção: MEU NEGÓCIO
| Item | Descrição |
|------|-----------|
| Serviços e preços | Gerencie seu catálogo de serviços |
| Horários de funcionamento | Defina sua disponibilidade por dia/hora |

### Seção: NOTIFICAÇÕES E LEMBRETES
| Notificação | Toggle | Observação |
|-------------|--------|------------|
| Notificações push | ✅ Ativo | Alertas no app |
| WhatsApp para clientes | ✅ Ativo | Confirmação + lembrete 24h antes — ~2 mensagens/agendamento a R$0,25/msg |
| Notificações por email | ✅ Ativo | Novos agendamentos e cancelamentos |

### Seção: INTEGRAÇÕES
| Integração | Status | Ação |
|------------|--------|------|
| WhatsApp | ✅ Conectado (+55 11 97777-7030) | Alterar |
| Google Calendar | — | Sincronize sua agenda |
| Link de agendamento | `booking.zavvy.com.br/ofabio` | Copiar |
| QR Code | — | Compartilhe visualmente |

### Seção: CONTA
| Item | Descrição |
|------|-----------|
| Assinatura | Plano Starter — clica para gerenciar |
| Perfil | Nome, foto e link de agendamento |
| Excluir conta | Apagar permanentemente |
| Sair da conta | Logout |

---

## Estado Atual do Produto

| Aspecto | Situação |
|---------|----------|
| Fase | Lançamento — poucos cadastros iniciais |
| Aquisição | Testando anúncios pagos; alguns usuários orgânicos via Google |
| Plano ativo | Starter (período de teste) |
| Clientes no app | 1 cliente cadastrado (Matheus) |
| Agendamentos | 2 no total (1 concluído, 1 pendente) |

---

## Funcionalidades Ausentes (Roadmap identificado)

### Prioridade Alta — Pequenas Clínicas

| Feature | Situação atual | O que precisaria |
|---------|----------------|-----------------|
| **Agenda recorrente** | Cada agendamento é avulso | Repetir sessão semanalmente por N semanas, com confirmação automática em cada |
| **Ficha clínica do paciente** | Apenas anotação livre + histórico de agendamentos | Campos estruturados: data de nascimento, anamnese, diagnóstico, convênio |
| **Multi-profissional** | 1 conta = 1 profissional | Múltiplos profissionais sob o mesmo negócio, cada um com sua agenda |
| **Pacote de sessões** | Não existe | Ex: "Pacote de 10 sessões" com controle de créditos restantes |
| **Prontuário por sessão** | Não existe | Anotação vinculada a um atendimento específico (evolução clínica) |

---

## Estrutura de Arquivos (Screenshots — App)

```
screenshots/
├── home/                              # Landing page (zavvy.com.br)
│   ├── 01-hero.png
│   ├── 02-whatsapp-demo.png
│   ├── 03-como-funciona.png
│   ├── 04-funcionalidades.png
│   ├── 05-preco.png
│   ├── 06-faq.png
│   └── 07-footer.png
├── termos-de-uso/
│   └── full-page.png
├── politica-de-privacidade/
│   └── full-page.png
└── app/                               # App logado (app.zavvy.com.br)
    ├── dashboard/
    │   └── 01-home.png
    ├── agenda/
    │   ├── 01-semana.png
    │   ├── 02-detalhe-agendamento.png
    │   └── 03-lista.png
    ├── clientes/
    │   ├── 01-lista.png
    │   ├── 02-perfil-historico.png
    │   ├── 03-perfil-mensagens.png
    │   └── 04-perfil-anotacoes.png
    └── configuracoes/
        ├── 01-geral.png
        └── 02-integracoes.png
```

> ⚠️ Screenshots do app (`screenshots/app/`) serão capturados quando a extensão Chrome reconectar.
