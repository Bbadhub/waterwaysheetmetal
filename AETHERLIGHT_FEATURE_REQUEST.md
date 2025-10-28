# ÆtherLight Feature Request: Chain of Thought Display in Sprint Panel

**Date:** 2025-10-27
**Project:** ÆtherLight Lumina VS Code Extension
**Component:** Sprint Panel (Voice Panel → Sprint Tab)
**Priority:** HIGH
**Type:** Feature Enhancement

---

## Summary

The Sprint Panel currently does NOT display Chain of Thought (CoT) fields from ACTIVE_SPRINT.toml tasks, limiting the panel's ability to show task context, reasoning, and documentation links. These fields exist in the TOML file but are not loaded or rendered in the UI.

---

## Current State

### What Works ✅
The Sprint Panel (`voicePanel.ts:1607-1698 getTaskDetailPanel()`) displays:
- Task ID and name
- Status (with toggle button)
- Description
- Estimated time and lines
- Agent
- Dependencies
- Patterns
- Performance target
- Phase
- Full task implementation (from PHASE_X_IMPLEMENTATION.md)

### What's Missing ❌
The following fields exist in ACTIVE_SPRINT.toml but are NOT displayed:
1. **`why`** - Explains why the task matters (business value)
2. **`context`** - Links task to documentation and strategy
3. **`reasoning_chain`** - Step-by-step logical progression (array)
4. **`success_impact`** - Concrete outcomes when task completed
5. **`notes`** - Additional context or warnings
6. **`files_to_create`** - Explicit file deliverables
7. **`files_to_modify`** - Files that will be changed
8. **`validation_criteria`** - Definition of "done"

### Technical Gap
**File:** `vscode-lumina/src/commands/SprintLoader.ts:36-55`

```typescript
export interface SprintTask {
    id: string;
    name: string;
    phase: string;
    description: string;
    estimated_time: string;
    estimated_lines: number;
    dependencies: string[];
    status: TaskStatus;
    agent: string;
    assigned_engineer: string;
    required_expertise: string[];
    performance_target?: string;
    patterns?: string[];
    deliverables?: string[];
    completed_date?: string;
    files_to_create?: string[];
    files_to_modify?: string[];
    validation_criteria?: string[];
    // MISSING: why, context, reasoning_chain, success_impact, notes
}
```

---

## Why This Matters

### Problem Statement
Without CoT fields visible in the Sprint Panel, users (and Claude Code AI) cannot:
- Understand WHY a task is needed (business justification)
- See CONTEXT linking task to documentation (WATERWAYS_SITE_ARCHITECTURE.md, etc.)
- Follow REASONING CHAIN showing how decisions were made
- Know SUCCESS IMPACT (what "done" looks like with concrete outcomes)
- Access VALIDATION CRITERIA (checklist for task completion)

### Real-World Impact
**Water Ways Sprint Example:**

**Task PLAN-001** has rich CoT in TOML:
```toml
why = """
Need complete business details to implement proper Schema markup (LocalBusiness).
Missing information blocks content writing for about page and contact page.
Geographic/service area data critical for local SEO targeting (Northwest Arkansas, OK, MO, KS).
"""

context = """
WATERWAYS_BUILD_PLAN.md identifies this as Priority 1 (Information Gathering).
COMPETITIVE_RESEARCH_REPORT.md shows competitors emphasize "Made in USA", facility location, years of experience.
Current site has limited business info - just phone/email (no address, hours, team details visible).
"""

reasoning_chain = [
    "1. WATERWAYS_SITE_ARCHITECTURE.md requires Schema LocalBusiness markup",
    "2. LocalBusiness schema needs: address, phone, hours, geo coordinates",
    "3. About page needs: founding year, team details, certifications",
    "4. KEYWORD_RESEARCH.md targets local geo keywords (Arkansas, Siloam Springs)",
    "5. Local SEO requires accurate NAP (Name, Address, Phone) consistency",
    "6. Competitor sites showcase 40+ years experience, facility details",
    "7. Ray is primary contact: (479) 957-3794 | Ray@WaterwaysSheetMetal.com",
    "8. Result: Single information gathering session → unblocks content, Schema, SEO"
]

success_impact = """
When PLAN-001 complete:
✅ All business details documented in one central place
✅ Schema LocalBusiness markup can be implemented (PLAN-001 → DEV-005)
✅ About page content can be written (PLAN-001 → PLAN-004)
✅ Contact page accurate (PLAN-001 → DEV-001)
✅ Local SEO foundation established (geographic targeting)
✅ Credibility signals identified (years in business, certifications)
"""
```

**But the Sprint Panel shows NONE of this!**

User clicks PLAN-001 and sees:
- Description: "Complete comprehensive business information checklist..."
- Estimated time: 2-3 hours
- Dependencies: []

They do NOT see:
- WHY this unblocks 4 other tasks
- CONTEXT from competitive research and architecture docs
- REASONING showing Schema markup → business info dependency
- SUCCESS IMPACT with checkmarks

---

## Proposed Solution

### Phase 1: Update SprintTask Interface

**File:** `vscode-lumina/src/commands/SprintLoader.ts`

```typescript
export interface SprintTask {
    id: string;
    name: string;
    phase: string;
    description: string;
    estimated_time: string;
    estimated_lines: number;
    dependencies: string[];
    status: TaskStatus;
    agent: string;
    assigned_engineer: string;
    required_expertise: string[];
    performance_target?: string;
    patterns?: string[];
    deliverables?: string[];
    completed_date?: string;
    files_to_create?: string[];
    files_to_modify?: string[];
    validation_criteria?: string[];

    // ✨ NEW: Chain of Thought fields
    why?: string;                    // Business justification
    context?: string;                // Strategic alignment & doc links
    reasoning_chain?: string[];      // Step-by-step logic
    success_impact?: string;         // Concrete outcomes (with checkmarks)
    notes?: string;                  // Additional warnings/info
}
```

### Phase 2: Update getTaskDetailPanel() UI

**File:** `vscode-lumina/src/commands/voicePanel.ts:1607-1698`

Add new sections after existing content (before "Full Task Implementation"):

```typescript
// After patterns section (line ~1676)

${task.why ? `
<div class="detail-section cot-section">
    <h4>💡 Why This Task Matters</h4>
    <div class="cot-content why-content">
        ${this.convertMarkdownToHtml(task.why)}
    </div>
</div>
` : ''}

${task.context ? `
<div class="detail-section cot-section">
    <h4>📚 Context & Documentation</h4>
    <div class="cot-content context-content">
        ${this.convertMarkdownToHtml(task.context)}
    </div>
</div>
` : ''}

${task.reasoning_chain && task.reasoning_chain.length > 0 ? `
<div class="detail-section cot-section">
    <h4>🧠 Reasoning Chain</h4>
    <ol class="reasoning-chain">
        ${task.reasoning_chain.map(step => `<li>${this.convertMarkdownToHtml(step)}</li>`).join('')}
    </ol>
</div>
` : ''}

${task.success_impact ? `
<div class="detail-section cot-section">
    <h4>🎯 Success Impact</h4>
    <div class="cot-content success-impact-content">
        ${this.convertMarkdownToHtml(task.success_impact)}
    </div>
</div>
` : ''}

${task.validation_criteria && task.validation_criteria.length > 0 ? `
<div class="detail-section cot-section">
    <h4>✅ Validation Criteria</h4>
    <ul class="validation-list">
        ${task.validation_criteria.map(criteria => `<li>${this.convertMarkdownToHtml(criteria)}</li>`).join('')}
    </ul>
</div>
` : ''}

${task.files_to_create && task.files_to_create.length > 0 ? `
<div class="detail-section">
    <h4>📝 Files to Create</h4>
    <div class="tag-list">
        ${task.files_to_create.map(file => `<span class="tag file-tag">${file}</span>`).join('')}
    </div>
</div>
` : ''}

${task.files_to_modify && task.files_to_modify.length > 0 ? `
<div class="detail-section">
    <h4>✏️ Files to Modify</h4>
    <div class="tag-list">
        ${task.files_to_modify.map(file => `<span class="tag file-tag">${file}</span>`).join('')}
    </div>
</div>
` : ''}

${task.notes ? `
<div class="detail-section cot-section notes-section">
    <h4>📌 Notes</h4>
    <div class="cot-content notes-content">
        ${this.convertMarkdownToHtml(task.notes)}
    </div>
</div>
` : ''}
```

### Phase 3: Update parseTomlTasks()

**File:** `vscode-lumina/src/commands/SprintLoader.ts` (~line 200)

Ensure TOML parser extracts CoT fields:

```typescript
private parseTomlTasks(tasksObj: any): SprintTask[] {
    const tasks: SprintTask[] = [];

    for (const [taskId, taskData] of Object.entries(tasksObj)) {
        tasks.push({
            id: taskData.id || taskId,
            name: taskData.name || 'Untitled Task',
            phase: taskData.phase || 'Unknown Phase',
            description: taskData.description || '',
            estimated_time: taskData.estimated_time || 'Not specified',
            estimated_lines: taskData.estimated_lines || 0,
            dependencies: taskData.dependencies || [],
            status: taskData.status || 'pending',
            agent: taskData.agent || 'unknown',
            assigned_engineer: taskData.assigned_engineer || this.currentEngineer,
            required_expertise: taskData.required_expertise || [],
            performance_target: taskData.performance_target,
            patterns: taskData.patterns,
            deliverables: taskData.deliverables,
            completed_date: taskData.completed_date,
            files_to_create: taskData.files_to_create,
            files_to_modify: taskData.files_to_modify,
            validation_criteria: taskData.validation_criteria,

            // ✨ NEW: Parse CoT fields
            why: taskData.why,
            context: taskData.context,
            reasoning_chain: taskData.reasoning_chain,
            success_impact: taskData.success_impact,
            notes: taskData.notes,
        });
    }

    return tasks;
}
```

### Phase 4: Add CSS Styling

**File:** `vscode-lumina/src/commands/voicePanel.ts` (in `<style>` block)

```css
/* Chain of Thought sections */
.cot-section {
    background: var(--vscode-editor-background);
    border-left: 3px solid var(--vscode-charts-blue);
    padding-left: 12px;
    margin-top: 16px;
}

.cot-content {
    font-size: 13px;
    line-height: 1.6;
    white-space: pre-wrap;
}

.why-content {
    color: var(--vscode-charts-purple);
}

.context-content {
    color: var(--vscode-charts-green);
}

.reasoning-chain {
    list-style: decimal;
    padding-left: 24px;
    margin: 8px 0;
}

.reasoning-chain li {
    margin: 6px 0;
    line-height: 1.5;
}

.success-impact-content {
    color: var(--vscode-charts-green);
    font-weight: 500;
}

.validation-list {
    list-style: none;
    padding-left: 0;
}

.validation-list li {
    margin: 6px 0;
    padding-left: 24px;
    position: relative;
}

.validation-list li::before {
    content: '☑️';
    position: absolute;
    left: 0;
}

.file-tag {
    background: var(--vscode-editorWidget-background);
    color: var(--vscode-editor-foreground);
    font-family: var(--vscode-editor-font-family);
    font-size: 11px;
}

.notes-section {
    border-left-color: var(--vscode-charts-orange);
}
```

---

## Benefits

### For Users (Brett)
✅ **Full task context** visible in panel (no more external doc lookups)
✅ **Documentation links** accessible (WATERWAYS_SITE_ARCHITECTURE.md, KEYWORD_RESEARCH.md)
✅ **Reasoning transparency** (understand why decisions were made)
✅ **Clear success criteria** (know when task is actually "done")
✅ **Dependency clarity** (see how tasks unlock each other in reasoning_chain)

### For Claude Code (AI Assistant)
✅ **Self-documenting tasks** (AI can understand purpose without asking)
✅ **Context-aware responses** (AI references documentation links in context field)
✅ **Decision rationale** (AI can validate approach against reasoning_chain)
✅ **Validation criteria** (AI knows exact definition of "done")

### For Sprint System
✅ **Pattern-SPRINT-001 compliance** (CoT fields now fully utilized)
✅ **Enhanced task template validated** (ENORM-010 implementation complete)
✅ **Documentation preservation** (historical reasoning never lost)

---

## Implementation Checklist

**Phase 1: Data Layer**
- [ ] Update `SprintTask` interface with CoT fields (SprintLoader.ts:36-55)
- [ ] Update `parseTomlTasks()` to extract CoT fields (SprintLoader.ts:~200)
- [ ] Test: Verify CoT fields load from ACTIVE_SPRINT.toml

**Phase 2: UI Layer**
- [ ] Add CoT sections to `getTaskDetailPanel()` (voicePanel.ts:1607-1698)
- [ ] Add CSS styling for CoT sections (voicePanel.ts style block)
- [ ] Test: Verify CoT fields display correctly in panel

**Phase 3: Validation**
- [ ] Test with Water Ways sprint (7 tasks with full CoT)
- [ ] Test with ÆtherLight Lumina sprint (tasks with varying CoT completeness)
- [ ] Verify markdown rendering in `why`, `context`, `success_impact` fields
- [ ] Verify list rendering for `reasoning_chain`, `validation_criteria`

**Phase 4: Documentation**
- [ ] Update SPRINT_SYSTEM_TOML_DECISION.md (document CoT field support)
- [ ] Update enhanced task template (ensure all fields documented)
- [ ] Add screenshot to docs showing CoT sections in panel

---

## Testing Instructions

**Test Sprint:** Water Ways Sheet Metal
**File:** `C:\Users\Brett\Dropbox\Ferret9 Global\Water Ways Sheet Metal\sprints\ACTIVE_SPRINT.toml`

**Test Cases:**
1. Open Water Ways folder in VS Code
2. Press ` (backtick) → Click Sprint tab
3. Click task PLAN-001
4. Verify displayed:
   - ✅ 💡 Why This Task Matters (paragraph with Schema markup justification)
   - ✅ 📚 Context & Documentation (links to WATERWAYS_BUILD_PLAN.md, COMPETITIVE_RESEARCH_REPORT.md)
   - ✅ 🧠 Reasoning Chain (8-step numbered list)
   - ✅ 🎯 Success Impact (6 checkmarked outcomes with dependencies)
   - ✅ 📝 Files to Create (BUSINESS_INFO.md tag)
5. Repeat for PLAN-002, PLAN-003, PLAN-004 (all have full CoT)

---

## Files Affected

### Modified Files
1. `vscode-lumina/src/commands/SprintLoader.ts` - Interface + parser
2. `vscode-lumina/src/commands/voicePanel.ts` - UI rendering + CSS

### Test Files
1. `Water Ways Sheet Metal/sprints/ACTIVE_SPRINT.toml` - Test data
2. `ÆtherLight_Lumina/sprints/ACTIVE_SPRINT.toml` - Reference implementation

---

## Related Issues

- **ENORM-010** - "Enhance Sprint Tasks with Chain of Thought Context" (completed)
- **Pattern-SPRINT-001** - Sprint System with TOML Source of Truth
- **Pattern-META-001** - Chain of Thought in Documentation

---

## Next Steps

1. **Create GitHub issue** in `ÆtherLight_Lumina` repo with this content
2. **Assign to appropriate engineer** (sprint tab implementation owner)
3. **Test implementation** against Water Ways sprint (real-world validation)
4. **Document in SPRINT_SYSTEM_TOML_DECISION.md** when complete

---

**Priority Justification:** HIGH - Without this feature, the enhanced sprint format (ENORM-010) has limited value. CoT fields exist in TOML but are invisible to users, defeating the purpose of self-documenting tasks.
