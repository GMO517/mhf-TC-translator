# -*- coding: utf-8 -*-
"""working 目錄路徑契約（單一來源）。"""
from __future__ import annotations

from pathlib import Path

WORKING = Path(__file__).resolve().parent
ROOT = WORKING.parents[1]
L10N = WORKING.parent

CSV_DIR = WORKING / "csv"
BATCHES = WORKING / "batches"
BATCHES_ACTIVE = BATCHES / "active"
BATCHES_AWAITING_QA = BATCHES / "awaiting_qa"
BATCHES_LEGACY = BATCHES / "legacy"
STATE_DIR = WORKING / "state"
LOGS = WORKING / "logs"
CATALOGS = WORKING / "catalogs"
SCRATCH = WORKING / "scratch"
ISSUES = WORKING / "issues"
ISSUES_ARCHIVE = ISSUES / "archive"
OUTPUT = WORKING / "output"

STATE_FILE = STATE_DIR / "writeback-state.json"
WRITEBACK_LOG = LOGS / "writeback.md"
VALIDATE_LOG = LOGS / "validate.md"
ISSUES_QUEUE = ISSUES / "queue.md"


def ensure_dirs() -> None:
    for p in (
        CSV_DIR,
        BATCHES,
        BATCHES_ACTIVE,
        BATCHES_AWAITING_QA,
        BATCHES_LEGACY,
        STATE_DIR,
        LOGS,
        CATALOGS,
        SCRATCH,
        ISSUES,
        ISSUES_ARCHIVE,
        OUTPUT,
    ):
        p.mkdir(parents=True, exist_ok=True)
