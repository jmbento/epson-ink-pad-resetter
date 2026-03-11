# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [1.0.0] - 2026-03-11

### Added
- Versão inicial
- Suporte para impressora única (epson_resetter.py)
- Suporte para múltiplas impressoras (epson_resetter_pro.py)
- Comunicação via SNMP
- Suporte para L355, L3160, L3250, L4160, M1170, ET-2850, ET-2860
- Leitura e reset de contador de almofada de tinta residual
- Operações em lote para múltiplas impressoras
- Exemplos de automação com cron
- Documentação abrangente em português
- Licença GPL v3
- Guia de contribuição

### Features
- ✅ Sem USB necessário
- ✅ Funciona via WiFi/Ethernet
- ✅ Multiplataforma (macOS, Linux, Windows)
- ✅ Gerenciamento de múltiplas impressoras
- ✅ 100% gratuito e open-source

### Limitações Conhecidas
- SNMP deve estar habilitado na impressora (geralmente padrão)
- Alguns modelos antigos podem não ser compatíveis
- Testes comunitários em progresso

## Roadmap

### v1.1.0 (Planejado)
- [ ] Interface gráfica (PyQt5)
- [ ] Dashboard web
- [ ] API REST
- [ ] Alertas por email/Slack
- [ ] Detecção automática de modelos

### v2.0.0 (Planejado)
- [ ] Suporte para impressoras Ricoh/Canon
- [ ] Banco de dados para rastrear resets
- [ ] Analytics avançado
- [ ] Aplicativo móvel

---

Para contribuir, veja [CONTRIBUTING.md](CONTRIBUTING.md)