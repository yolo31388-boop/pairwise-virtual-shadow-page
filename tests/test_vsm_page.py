import pytest
import graphics.vsm_page as mod

CASES = [
    ("page_exclusive", (1,)),
    ("valid_after_readback", (1,)),
    ("evict_hysteresis", (1,)),
    ("page_table_commit", (1,)),
    ("invalidate_on_cull", (1,)),
    ("clear_on_realloc", (1,)),
    ("load_lights", (1,)),
    ("allocate", (1,)),
    ("sample", (1,)),
    ("present", (1,)),
    ("validate_pages", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
