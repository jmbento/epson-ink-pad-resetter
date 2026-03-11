# 🖨️ Epson Ink Pad Resetter - Solução Completa Gratuita

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-green)](https://www.python.org/downloads/)
[![Supported Printers](https://img.shields.io/badge/Printers-L355%2CL3160%2CL3250%2BMore-brightgreen)](#-modelos-suportados)

**Resete a almofada de tinta residual de qualquer impressora Epson** sem pagar por ferramentas caras como WICReset. Ferramenta 100% gratuita, open-source e funcionando perfeitamente no macOS, Linux e Windows.

---

## 🎯 O Problema

A Epson **propositalmente programa** as impressoras para parar após um certo número de páginas impressas, forçando você a comprar ferramentas de reset como WICReset ou Epson Adjustment Program (que custam €5 a €20 POR RESET).

**Você comprou a impressora? Você tem direito de consertá-la!**

---

## ✨ Recursos

✅ **Múltiplas impressoras** - Gerencie ilimitadas impressoras com um só comando  
✅ **Todos os modelos L/M/ET** - L355, L3160, L3250, L4160, M1170, ET-2850, etc.  
✅ **Sem USB** - Usa SNMP via WiFi/Ethernet  
✅ **100% Gratuito** - Nenhuma assinatura ou chave de ativação  
✅ **Open Source** - GPL v3, modificável e aprimorável  
✅ **Fácil de usar** - Uma linha de comando  
✅ **Agendamento automático** - Resetar impressoras toda semana/mês  

---

## 📦 Instalação Rápida

### Pré-requisitos
- Python 3.7+
- Impressora Epson conectada na mesma rede (WiFi/Ethernet)
- SNMP habilitado na impressora (padrão)

### 1. Clonar Repositório

```bash
git clone https://github.com/jmbento/epson-ink-pad-resetter.git
cd epson-ink-pad-resetter
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Descobrir IP da Impressora

```bash
# Opção 1: No painel da impressora
# Menu → Rede → WiFi → Mostrar Endereço IP

# Opção 2: Procurar na rede
ping epson.local
# ou acesse http://192.168.1.1 no roteador
```

---

## 🚀 Como Usar

### Verificar Status (UMA impressora)

```bash
python epson_resetter.py --ip 192.168.1.100 --operation read
```

**Output:**
```
[LOG] Conectando a 192.168.1.100...
[LOG] ✓ Conectado
[LOG] Modelo: Epson L355

=== STATUS DA ALMOFADA ===
counter_1: 45% (OK)
counter_2: 12% (OK)
counter_3: 88% (PRECISA RESET ⚠️)
```

### Resetar Status (UMA impressora)

```bash
python epson_resetter.py --ip 192.168.1.100 --operation reset
```

**Output:**
```
[LOG] Resetando 192.168.1.100...
[LOG] Antes: counter_1=45%, counter_2=12%, counter_3=88%
[LOG] Depois: counter_1=0%, counter_2=0%, counter_3=0%
✓ RESET COMPLETO!
```

### Gerenciar MÚLTIPLAS Impressoras

#### Criar arquivo `printers.json`:

```json
{
  "printers": [
    {"name": "Sala de Impressão", "ip": "192.168.1.100", "model": "L355"},
    {"name": "Marketing", "ip": "192.168.1.101", "model": "L3160"},
    {"name": "RH", "ip": "192.168.1.102", "model": "L3250"},
    {"name": "Diretoria", "ip": "192.168.1.103", "model": "ET-2850"}
  ]
}
```

#### Ver status DE TODAS:

```bash
python epson_resetter_pro.py --config printers.json --operation read_all
```

#### RESETAR TODAS:

```bash
python epson_resetter_pro.py --config printers.json --operation reset_all
```

---

## 📊 Modelos Suportados

| Modelo | Status | Notas |
|--------|--------|-------|
| **L355** | ✅ Testado | OK |
| **L3160** | ✅ Testado | OK |
| **L3250** | ✅ Testado | OK |
| **L4160** | ✅ Testado | OK |
| **M1170** | ✅ Config | Provável compatibilidade |
| **ET-2850** | ✅ Config | Novo modelo, funciona |
| **ET-2860** | ✅ Config | Suportado |
| **XP-7100** | ⚠️ Teste | Experimente! |
| **Outros L/M/ET** | ⚠️ Fallback | Config padrão |

---

## ⏰ Automação com Cron (Linux/macOS)

### Verificar todas as impressoras TODO DIA às 8:00 AM:

```bash
0 8 * * * cd /path/to/epson-ink-pad-resetter && python epson_resetter_pro.py --config printers.json --operation read_all >> /var/log/epson_check.log 2>&1
```

### Resetar impressoras CHEIAS todo DOMINGO à 2:00 AM:

```bash
0 2 * * 0 cd /path/to/epson-ink-pad-resetter && python epson_resetter_pro.py --config printers.json --operation reset_all >> /var/log/epson_reset.log 2>&1
```

---

## 🔧 Flags Disponíveis

```
--ip ENDEREÇO_IP        IP da impressora (ex: 192.168.1.100)
--config ARQUIVO.JSON   Arquivo de configuração para múltiplas impressoras
--operation OPERAÇÃO    read, reset, read_all, reset_all
--community COMUNIDADE  String SNMP (padrão: 'public')
--timeout SEGUNDOS      Timeout em segundos (padrão: 5)
--verbose               Modo verbose com mais detalhes
--help                  Mostrar esta ajuda
```

---

## ❓ FAQ

### P: Preciso de USB?
**R:** Não! Usa SNMP via WiFi/Ethernet. Bem melhor.

### P: Funciona com impressoras muito antigas?
**R:** Depende de suporte a SNMP. Teste com `--operation read` primeiro.

### P: Vai danificar minha impressora?
**R:** NÃO! Apenas alteramos um contador de software. A almofada física continua 100% OK.

### P: Qual é a diferença do WICReset?
**R:** WICReset custa €5-20 por reset + é Windows-only. Isto é grátis, open-source e multiplataforma.

### P: Posso resetar a cada 100 páginas automaticamente?
**R:** Sim! Agende com cron (veja [Automação](#-automação-com-cron-linuxmacos)).

---

## 🐛 Troubleshooting

### Erro: "Connection timeout"

```bash
# Verifique se a impressora está online:
ping 192.168.1.100

# Habilite SNMP no painel da impressora:
# Menu → Configuração → Rede → SNMP → Ativado
```

### Erro: "EEPROM read failed"

```bash
# Tente com timeout maior:
python epson_resetter.py --ip 192.168.1.100 --operation read --timeout 10
```

### Módulo `easysnmp` não encontrado

```bash
# Instale as dependências do sistema:
# macOS:
brew install snmp

# Ubuntu/Debian:
sudo apt-get install snmp

# CentOS:
sudo yum install net-snmp

# Depois:
pip install -r requirements.txt
```

---

## 📈 Roadmap

- [ ] Interface gráfica (PyQt5)
- [ ] API Flask para uso remoto
- [ ] Dashboard web em tempo real
- [ ] Detecção automática de printers na rede
- [ ] Suporte a impressoras Ricoh/Canon
- [ ] Alertas por email/Slack

---

## 🤝 Contribuindo

Encontrou um bug? Tem uma impressora que não funciona? **Abra uma [Issue](https://github.com/jmbento/epson-ink-pad-resetter/issues)!**

Quer adicionar suporte a novo modelo? **Faça um [Pull Request](https://github.com/jmbento/epson-ink-pad-resetter/pulls)!**

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

---

## 📚 Referências

- [Zedeldi/epson-printer-snmp](https://github.com/Zedeldi/epson-printer-snmp) - Inspiração
- [Bloody-Badboy L3250 Reset](https://gist.github.com/Bloody-Badboy/c16b6ee97439b858ab78733428c79a57) - Protocolo L3250
- [k3dt/epson-l3160-ink-waste-resetter](https://github.com/k3dt/epson-l3160-ink-waste-resetter) - Suporte L3160
- Epson SNMP Protocol Documentation (não-oficial)

---

## ⚖️ Licença

GPL v3 - Veja [LICENSE](LICENSE) para detalhes.

Em resumo: Use, modifique e distribua livremente, mas mantenha o código aberto.

---

## 💬 Comunidade

- 🐛 **Issues**: [github.com/jmbento/epson-ink-pad-resetter/issues](https://github.com/jmbento/epson-ink-pad-resetter/issues)
- 💡 **Discussões**: [github.com/jmbento/epson-ink-pad-resetter/discussions](https://github.com/jmbento/epson-ink-pad-resetter/discussions)
- 📢 **Reddit**: Venha comentar em r/Epson ou r/printers!

---

## 📞 Suporte

Tem dúvidas? **[Abra uma Issue!](https://github.com/jmbento/epson-ink-pad-resetter/issues/new)**

Estamos aqui para ajudar! 🚀

---

**Desenvolvido com ❤️ por [jmbento](https://github.com/jmbento)**  
**Criado para economizar seu dinheiro e tempo!**
