# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Scaffold smoke test: the package imports and carries its version."""

import snea_grammar


def test_package_imports_with_version() -> None:
    assert snea_grammar.__version__ == "0.1.0"
