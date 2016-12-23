
from django.conf import settings
try:
    import cProfile as profile
except ImportError:
    import profile

def profile_tests(*args, **kwargs):
    profile.runctx('run_tests(*args, **kwargs)',
                {'run_tests':run_tests,'args':args,'kwargs':kwargs},
                {},
                getattr(settings,'TEST_PROFILE',None)
            )

# file: settings.py #
TEST_RUNNER = 'profiling.profile_tests'
TEST_PROFILE = None