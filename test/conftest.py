# pylint: disable=missing-docstring, invalid-name, unnecessary-dunder-call
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply

fake = Faker()

def generate_test_data(num_records):
    # Define operation mapping for add, subtract, and multiply operations
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))
        # Randomly choose one of the operations from the mapping
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        expected = operation_func(a, b)
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int,
                     help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
