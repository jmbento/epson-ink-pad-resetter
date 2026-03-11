# 🤝 Contribuindo para Epson Ink Pad Resetter

Obrigado por querer ajudar! Este projeto é 100% comunitário.

## 🐛 Reportar Bugs

1. Verifique se o bug já foi reportado em [Issues](https://github.com/jmbento/epson-ink-pad-resetter/issues)
2. Se não, abra uma nova Issue com:
   - **Título descritivo** (ex: "L3160 com timeout de conexão")
   - **Modelo da impressora**
   - **Versão do Python** (`python --version`)
   - **Sistema operacional** (macOS/Linux/Windows)
   - **Saída completa do erro** (full traceback)
   - **Passos para reproduzir**

## 💡 Sugerir Melhorias

1. Use a label `enhancement` ao abrir Issue
2. Descreva o que gostaria de adicionar
3. Explique por que seria útil
4. Exemplos de uso são bem-vindos!

## 📝 Adicionar Suporte a Novo Modelo

### 1. Descubra os parâmetros

Se você tem uma impressora não suportada:

```bash
# Clone e instale
git clone https://github.com/jmbento/epson-ink-pad-resetter
cd epson-ink-pad-resetter
pip install -r requirements.txt

# Tente ler com debug:
python epson_resetter.py --ip 192.168.1.100 --operation read --verbose
```

### 2. Se funcionar, ótimo!
Abra uma Issue confirmando o modelo funciona.

### 3. Se não funcionar, precisamos dos parâmetros

Este projeto usa reverse-engineering. Se seu modelo não é suportado:

1. Instale WICReset em um Windows temporário
2. Execute e deixe logs em `%APPDATA%\WICReset\logs`
3. Compartilhe os logs (anonimizando dados sensíveis)
4. Abra uma Issue com os logs

Com isso conseguimos extrair a "senha" SNMP do seu modelo.

## 🔀 Pull Requests

### Antes de começar

1. **Fork** o projeto
2. **Crie uma branch** com nome descritivo:
   ```bash
   git checkout -b feature/suporte-l3300
   git checkout -b fix/timeout-snmp
   ```

### Código

- Siga [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Adicione comentários para código complexo
- Teste em múltiplas versões de Python (3.7, 3.8, 3.9, 3.10+)

### Commit & Push

```bash
git add .
git commit -m "feat: adicionar suporte L3300"
git push origin feature/suporte-l3300
```

### Submit PR

1. Abra Pull Request no GitHub
2. Descreva **O QUE** você mudou e **POR QUÊ**
3. Referencie Issues relacionadas: `Fixes #123`
4. Aguarde review

## 📚 Estrutura do Projeto

```
epson-ink-pad-resetter/
├── README.md                    # Documentação principal
├── CONTRIBUTING.md              # Este arquivo
├── LICENSE                      # GPL v3
├── requirements.txt             # Dependências
├── epson_resetter.py           # CLI single-printer
├── epson_resetter_pro.py       # CLI multi-printer
├── epson/
│   ├── __init__.py
│   ├── printer.py              # Classe EpsonPrinter
│   └── models.py               # Configurações de modelos
├── examples/
│   ├── single_printer.py       # Exemplo 1 impressora
│   ├── multi_printer.py        # Exemplo múltiplas
│   └── printers.json           # Config de exemplo
└── tests/
    ├── test_printer.py
    └── test_models.py
```

## ✅ Checklist antes de PR

- [ ] Código segue PEP 8
- [ ] Adicionei docstrings
- [ ] Testei em Python 3.7+
- [ ] Atualizei README se necessário
- [ ] Adicionei testes se aplicável
- [ ] Nenhuma senha/IP hardcoded
- [ ] GPL v3 header nos arquivos novos

## 📖 Documentação

Se está escrevendo docs:

- Use Markdown
- Português e/ou Inglês (bilíngue preferido)
- Exemplos práticos
- Links funcionais

## 🎓 Bom Primeiro Contrib?

Procure issues marcadas com `good-first-issue` no label!

## 💬 Dúvidas?

Abra uma Discussion em vez de Issue: [Discussions](https://github.com/jmbento/epson-ink-pad-resetter/discussions)

---

**Obrigado por contribuir! Você está ajudando milhares de pessoas a economizar dinheiro!** 🎉
