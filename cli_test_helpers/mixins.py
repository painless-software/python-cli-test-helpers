"""
Mixins for all context managers (decorators).  Not for direct, public use.
"""

import logging


class LoggingIsolationMixin:
    """
    Mixin that provides automatic logging configuration isolation.

    Isolates logging configuration by temporarily clearing logging handlers
    when entering the context and restoring them when exiting.  This allows
    code under test to call ``logging.basicConfig()`` successfully even when
    test frameworks (like pytest) have already configured logging handlers.

    All context managers use this mixin.
    """

    def __enter__(self):
        """Save and clear logging handlers before entering the context."""
        self._old_handlers = logging.root.handlers[:]
        logging.root.handlers.clear()
        if hasattr(super(), "__enter__"):  # cooperative inheritance (MRO)
            return super().__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Restore logging handlers after exiting the context.

        Closes and removes any handlers that were added during the context.
        """
        handlers_to_close = [
            handler
            for handler in logging.root.handlers
            if handler not in self._old_handlers
        ]

        for handler in handlers_to_close:
            handler.close()
            logging.root.handlers.remove(handler)

        logging.root.handlers[:] = self._old_handlers

        if hasattr(super(), "__exit__"):  # cooperative inheritance (MRO)
            return super().__exit__(exc_type, exc_val, exc_tb)
        return None
