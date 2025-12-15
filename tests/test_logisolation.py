"""Tests for our tests helpers.  8-}."""

import logging
import tempfile
from pathlib import Path

from cli_test_helpers import ArgvContext, EnvironContext, RandomDirectoryContext


def test_argv_context_logging_isolation():
    """
    Does ArgvContext isolate logging configuration?

    Verifies that ArgvContext temporarily clears logging handlers, allowing
    code under test to call logging.basicConfig() successfully even when
    test frameworks have already configured logging.
    """
    original_handlers = logging.root.handlers[:]
    mock_handler = logging.NullHandler()
    logging.root.handlers.append(mock_handler)

    try:
        assert mock_handler in logging.root.handlers, "Test setup failed"

        with tempfile.TemporaryDirectory() as tmpdir:
            logfile = Path(tmpdir) / "test.log"

            with ArgvContext("test_script.py", str(logfile)):
                handlers_before = logging.root.handlers[:]
                assert not handlers_before, "Handlers not cleared"

                logging.basicConfig(filename=str(logfile), level=logging.INFO)

                logger = logging.getLogger(__name__)
                logger.info("Test message")

            assert mock_handler in logging.root.handlers, "Handlers not restored"

            assert logfile.exists(), "Log file should have been created"
            log_content = logfile.read_text()
            assert "Test message" in log_content, "Unexpected log file content"

    finally:
        logging.root.handlers = original_handlers


def test_environ_context_logging_isolation():
    """
    Does EnvironContext isolate logging configuration?

    Verifies that EnvironContext temporarily clears logging handlers, allowing
    code under test to call logging.basicConfig() successfully even when test
    frameworks have already configured logging.
    """
    original_handlers = logging.root.handlers[:]
    mock_handler = logging.NullHandler()
    logging.root.handlers.append(mock_handler)

    try:
        assert mock_handler in logging.root.handlers, "Test setup failed"

        with tempfile.TemporaryDirectory() as tmpdir:
            logfile = Path(tmpdir) / "environ_test.log"

            with EnvironContext(TEST_VAR="test_value"):
                handlers_before = logging.root.handlers[:]
                assert not handlers_before, "Handlers not cleared"

                logging.basicConfig(filename=str(logfile), level=logging.INFO)

                logger = logging.getLogger(__name__)
                logger.info("Test message from EnvironContext")

            assert mock_handler in logging.root.handlers, "Handlers not restored"

            assert logfile.exists(), "Log file should have been created"
            log_content = logfile.read_text()
            assert "Test message" in log_content, "Unexpected log file content"

    finally:
        logging.root.handlers = original_handlers


def test_random_directory_context_logging_isolation():
    """
    Does RandomDirectoryContext isolate logging configuration?

    Verifies that RandomDirectoryContext temporarily clears logging handlers,
    allowing code under test to call logging.basicConfig() successfully even
    when test frameworks have already configured logging.
    """
    original_handlers = logging.root.handlers[:]
    mock_handler = logging.NullHandler()
    logging.root.handlers.append(mock_handler)

    try:
        assert mock_handler in logging.root.handlers, "Test setup failed"

        with RandomDirectoryContext():
            logfile = Path("random_dir_test.log")

            handlers_before = logging.root.handlers[:]
            assert not handlers_before, "Handlers not cleared"

            logging.basicConfig(filename=str(logfile), level=logging.INFO)

            logger = logging.getLogger(__name__)
            logger.info("Test message from RandomDirectoryContext")

            assert logfile.exists(), "Log file should have been created"
            log_content = logfile.read_text()
            assert "Test message" in log_content, "Unexpected log file content"

        assert mock_handler in logging.root.handlers, "Handlers not restored"

    finally:
        logging.root.handlers = original_handlers
