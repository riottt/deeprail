# Contributing

Keep Book, Docs, Standard, Workflows, Runtime and Harness responsibilities distinct.

Before proposing structural changes:

```bash
./scripts/generate
./scripts/check
python3 -m unittest discover -s tests
```

Do not silently change stable module identities or promote candidate content to a public canonical release.
