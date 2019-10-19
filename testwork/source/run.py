import importlib


def run_test_cases(type_: str, tc: str, run_ids: list):
    module = importlib.import_module('.run', type_)
    func = getattr(module, f'run_{type_}_test_case')
    func(tc, run_ids)
