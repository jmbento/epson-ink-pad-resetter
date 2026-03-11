# ⚡ Quick Start Guide - macOS

## O Problema

Sua impressora Epson está com erro **"Ink Pad Full"** ou similar? 😱

Você pode resetar em **1 minuto** com este guia!

---

## Passo 1: Clone o Repositório

```bash
git clone https://github.com/jmbento/epson-ink-pad-resetter.git
cd epson-ink-pad-resetter
```

---

## Passo 2: Instale SNMP (macOS)

⚠️ **IMPORTANTE:** Execute este comando primeiro!

```bash
brew install snmp
```

Se não tiver Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## Passo 3: Instale Dependências Python

```bash
pip install -r requirements.txt
```

Se der erro de `pip`, use:
```bash
pip3 install -r requirements.txt
```

---

## Passo 4: Descubra o IP da Sua Impressora

### Opção 1: Painel da Impressora (Recomendado)
```
Menu → Configuração (Setup)
→ Rede (Network)
→ Status
→ Procure por "IP Address" ou "Endereço IP"
```

Exemplo: `192.168.1.100`

### Opção 2: Terminal (macOS)
```bash
ping epson.local
```

Ou procure no roteador:
```bash
arp -a | grep -i epson
```

---

## Passo 5: Verifique o Status

Substituia `192.168.1.100` pelo IP real da sua impressora:

```bash
python3 epson_resetter.py --ip 192.168.1.100 --operation read
```

**Output esperado:**
```
[LOG] Conectado a 192.168.1.100
[LOG] Modelo: Epson L355

=== WASTE INK STATUS ===
counter_1: 45% (OK)
counter_2: 88% (PRECISA RESET)
counter_3: 12% (OK)
```

---

## Passo 6: RESETE a Almofada!

```bash
python3 epson_resetter.py --ip 192.168.1.100 --operation reset
```

**Aguarde 1-2 minutos...**

**Output esperado:**
```
[LOG] Resetando...
[LOG] Antes:  counter_1=45%, counter_2=88%, counter_3=12%
[LOG] Depois: counter_1=0%, counter_2=0%, counter_3=0%

✓ RESET COMPLETO!
```

---

## ✅ Pronto! 🎉

Sua impressora está **desbloqueada** e pronta para imprimir!

Teste imprimindo uma página:
```bash
# Seu printer deverá funcionar normalmente
```

---

## ❌ Problemas Comuns

### "command not found: python"
**Solução:** Use `python3` em vez de `python`

```bash
python3 --version  # Verifique se tem Python 3
```

### "ModuleNotFoundError: No module named 'easysnmp'"
**Solução:** Você esqueceu de instalar as dependências!

```bash
pip3 install -r requirements.txt
```

### "Connection timeout"
**Checklist:**
- [ ] Impressora está **ligada**?
- [ ] Impressora está conectada na **WiFi**?
- [ ] IP está **correto**? (teste: `ping 192.168.1.100`)
- [ ] SNMP está **habilitado** no painel da impressora?

### "EEPROM read failed"
**Causa:** Seu modelo pode não ser suportado.

**Solução:** [Abra uma Issue](https://github.com/jmbento/epson-ink-pad-resetter/issues) com:
- Seu modelo exato (ex: L355, L3160, etc.)
- O erro completo que recebeu
- Sua versão de Python: `python3 --version`

Nós vamos adicionar suporte!

---

## 🎥 Quer Gravar um Vídeo?

Veja [VIDEO_NARRATION_SCRIPT.md](VIDEO_NARRATION_SCRIPT.md) para um roteiro completo!

---

## 🤝 Precisa de Ajuda?

- 📖 Leia o [README.md](README.md) completo
- 💬 Abra uma [Issue](https://github.com/jmbento/epson-ink-pad-resetter/issues)
- 🗣️ Participe das [Discussions](https://github.com/jmbento/epson-ink-pad-resetter/discussions)

---

**Dúvidas? Comenta na Issue! Vamos resolver junto! 🚀**