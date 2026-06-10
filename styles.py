CSS = """
:root {
  --py-color:     #209dd7;
  --cpp-color:    #ecad0a;
  --accent:       #753991;
  --accent-hover: #8f4aaf;
  --text:         #e9eef5;
  --muted:        #6b7585;
  --border:       rgba(255,255,255,.10);
  --surface:      #1e2330;
  --btn-h:        40px;
  --btn-r:        7px;
  --btn-f:        0.83rem;
}

/* ── Layout ─────────────────────────────────────────── */
.gradio-container {
  max-width: 100% !important;
  padding: 0 28px !important;
}

/* ══════════════════════════════════════════════════════
   UNIFIED BUTTON BASE — every button same size/font
══════════════════════════════════════════════════════ */
.run-btn button,
.port-btn button,
.side-btn button,
.testcase-btn button,
.testcase-run-btn button {
  height: var(--btn-h) !important;
  min-height: var(--btn-h) !important;
  max-height: var(--btn-h) !important;
  font-size: var(--btn-f) !important;
  font-weight: 600 !important;
  border-radius: var(--btn-r) !important;
  line-height: 1 !important;
  padding: 0 20px !important;
  letter-spacing: 0.025em !important;
  transition: background 0.16s, box-shadow 0.16s !important;
  white-space: nowrap !important;
}

/* ══════════════════════════════════════════════════════
   BUTTON VARIANTS
══════════════════════════════════════════════════════ */

/* ▶ Run Python — blue */
.run-btn.py button {
  background: var(--surface) !important;
  border: 1px solid var(--py-color) !important;
  color: var(--py-color) !important;
}
.run-btn.py button:hover {
  background: rgba(32,157,215,.12) !important;
  box-shadow: 0 0 0 2px var(--py-color) inset !important;
}

/* ⇄ Port Code — purple accent */
.port-btn button {
  background: var(--accent) !important;
  border: 1px solid transparent !important;
  color: #fff !important;
}
.port-btn button:hover {
  background: var(--accent-hover) !important;
  box-shadow: 0 0 0 2px rgba(255,255,255,.15) inset !important;
}

/* ⚡ Testcase — yellow/amber outline */
.testcase-btn button {
  background: var(--surface) !important;
  border: 1px solid var(--cpp-color) !important;
  color: var(--cpp-color) !important;
}
.testcase-btn button:hover {
  background: rgba(236,173,10,.12) !important;
  box-shadow: 0 0 0 2px var(--cpp-color) inset !important;
}

/* ▶ Run TestCases — amber solid */
.testcase-run-btn button {
  background: var(--surface) !important;
  border: 1px solid var(--cpp-color) !important;
  color: var(--cpp-color) !important;
}
.testcase-run-btn button:hover {
  background: rgba(236,173,10,.12) !important;
  box-shadow: 0 0 0 2px var(--cpp-color) inset !important;
}

/* ══════════════════════════════════════════════════════
   UNIFIED DROPDOWN BASE — model + lang same height/style
══════════════════════════════════════════════════════ */
.controlls select,
.controlls .wrap,
.controlls input[type="text"] {
  height: var(--btn-h) !important;
  min-height: var(--btn-h) !important;
  font-size: var(--btn-f) !important;
  font-weight: 500 !important;
  border-radius: var(--btn-r) !important;
  border: 1px solid var(--border) !important;
  background: var(--surface) !important;
  color: var(--text) !important;
  padding: 0 12px !important;
}

/* Dropdown chevron color */
.controlls .wrap svg {
  color: var(--muted) !important;
}

/* ══════════════════════════════════════════════════════
   CONTROL ROWS — consistent spacing, items aligned
══════════════════════════════════════════════════════ */
.controlls {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  padding: 6px 0 !important;
  border-top: 1px solid var(--border) !important;
}

/* First controls row — no top border */
.controlls:first-of-type {
  border-top: none !important;
  padding-top: 10px !important;
}

/* Second controls row — separator line */
.controlls + .controlls {
  border-top: 1px solid var(--border) !important;
  padding-top: 8px !important;
}

/* ══════════════════════════════════════════════════════
   OUTPUT TEXT AREAS
══════════════════════════════════════════════════════ */
.py-out textarea {
  background: linear-gradient(180deg,
    rgba(32,157,215,.15),
    rgba(32,157,215,.07)) !important;
  border: 1px solid rgba(32,157,215,.30) !important;
  color: #7dd3f5 !important;
  font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
}

/* Generated Result + Testcases Result — both amber */
.cpp-out textarea {
  background: linear-gradient(180deg,
    rgba(236,173,10,.18),
    rgba(236,173,10,.07)) !important;
  border: 1px solid rgba(236,173,10,.35) !important;
  color: #f5cc5a !important;
  font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
}

/* Output labels */
.py-out label span,
.cpp-out label span {
  font-size: 0.75rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.05em !important;
  text-transform: uppercase !important;
  color: var(--muted) !important;
}
"""