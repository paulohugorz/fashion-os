# Fashion OS v1

Sistema operacional para criar, produzir e lançar uma marca de moda com IA.

Este repositório une:
1. **Stack gratuita de moda com IA**
2. **Claude Fashion OS** — 22 agentes de pipeline de moda
3. **Fashion OS MVP FastAPI** — backend completo com SQLite

## O que vem dentro

| Pasta | Conteúdo |
|---|---|
| `app/` | FastAPI + SQLite (coleções, peças, fichas técnicas) |
| `.claude/agents/` | 22 agentes Claude — um para cada etapa do pipeline |
| `.claude/commands/` | `/nova-colecao`, `/criar-peca`, `/gerar-foto-produto` |
| `templates/` | Ficha técnica, ordem de produção, checklist de qualidade |
| `prompts/` | Croquis técnicos, fotografia editorial |
| `collections/` | Base inicial de peças (CSV) |
| `docs/` | Roadmap, fluxo operacional e plano mestre de desenvolvimento |
| `assets/` | Personas e modelos digitais |
| `comfyui/` | Preparação para geração de imagem (Fase 3) |
| `ollama/` | Preparação para LLM local (Fase 3) |
| `blender/` | Preparação para 3D (Fase 3) |
| `valentina/` | Preparação para modelagem 2D (Fase 3) |

## Como rodar o backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs
```

## Como usar no Claude Code

Abra o repositório no Claude Code e use:

```text
/nova-colecao coleção cápsula de calças femininas confortáveis e elegantes
/criar-peca calça preta com aparência de alfaiataria e mobilidade total
/gerar-foto-produto 10 fotos editoriais com modelos diversas
```

## Pipeline de moda (22 etapas)

```
Estratégia e Planejamento
→ Pesquisa Criativa
→ Direção de Criação
→ Design Técnico
→ Sourcing
→ Compras e Fornecimento
→ Custo e Precificação
→ Modelagem
→ Ficha Técnica
→ Guia de Produção
→ Piloto
→ Planejamento de Materiais
→ Ordens de Produção
→ Produção
→ Qualidade
→ Acabamentos e Embalagens
→ Cadastro PIM
→ Fotos e Vídeos
→ Conteúdos
→ Lançamentos
→ Vendas
→ Performance de Vendas
```

## Roadmap

| Fase | Status | Conteúdo |
|---|---|---|
| Fase 1 — Unificação | ✅ Concluída | FastAPI + SQLite, agentes Claude, comandos, templates, prompts |
| Fase 2 — Interface | 🔄 Em desenvolvimento | Next.js 14, cadastro visual, galeria, exportação PDF |
| Fase 3 — IA | Planejada | Ollama, ComfyUI, personas digitais |
| Fase 4 — Produção | Planejada | MRP, ordens de produção, qualidade, estoque |
| Fase 5 — Comercial | Planejada | PIM, conteúdo, lançamento, vendas, performance |

## Plano de desenvolvimento

Ver [`docs/planejamento/PLANO-MESTRE.md`](docs/planejamento/PLANO-MESTRE.md) para o plano técnico completo da Fase 2, fatiado por sprint com critérios verificáveis.
