.PHONY: run test fmt lint type
run:
\tpython -m studyfrog.main
test:
\tpytest -q
fmt:
\tblack src tests
lint:
\truff check src tests || true
type:
\tmypy src || true
