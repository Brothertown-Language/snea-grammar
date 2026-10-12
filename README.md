# snea-grammar — issue store

Git worktree on the orphan `issues-data` branch holding all issue specs,
plans, and artifacts for this repository. Not a regular directory — all git
operations run as `git -C .issues/ <command>` or via the local-issues tool;
the parent repo's `git add .issues/` is forbidden.

Folders are `{number}/` per issue, each holding `spec.md` and artifacts.

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
