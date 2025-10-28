# ÆtherLight Analyzer

This directory contains analysis artifacts for your codebase.

## Directory Structure

- `analysis/` - Analysis results (JSON + reports)
- `sprints/` - Generated sprint plans (PHASE_A/B/C.md)
- `patterns/` - Extracted patterns (Pattern-*.md)
- `config.json` - Configuration file

## Next Steps

1. **Analyze codebase:**
   ```bash
   aetherlight-analyzer analyze
   ```

2. **Generate sprint plans:**
   ```bash
   aetherlight-analyzer generate-sprints
   ```

3. **Review generated plans:**
   - `PHASE_A_ENHANCEMENT.md` - Add new features
   - `PHASE_B_RETROFIT.md` - Refactor existing code
   - `PHASE_C_DOGFOOD.md` - Integrate ÆtherLight SDK

4. **Execute sprint (optional):**
   ```bash
   aetherlight-analyzer execute-sprint A
   ```

## Configuration

Edit `config.json` to customize analysis settings:
- `languages`: Languages to parse
- `exclude`: Directories to skip
- `complexity_threshold`: Functions above this need refactoring
- `debt_threshold`: Debt score threshold (0-100)

---

**Built with Chain of Thought methodology**
