import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import user_email, password_email, DEFAULT_SMTP, \
    DEFAULT_IMAP, MAIL_SELECT


class MailHandler:
    def __init__(self, user_login, password, smtp=DEFAULT_SMTP,
                 imap=DEFAULT_IMAP):
        self.user_login = user_login
        self.password = password
        self.smtp = smtp
        self.imap = imap

    def send_a_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg["From"] = self.user_login
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(message))

import unittest
from src.helpers.config import (Config, WINDOWS)


class TestClass(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_get_verbosity_level(self):
        con = self.config.get_verbosity_level(level="critical")
        self.assertEqual(con, 50, "Тест не выполнен")

        con = self.config.get_verbosity_level(level="error")
        self.assertEqual(con, 40, "Тест не выполнен")

        con = self.config.get_verbosity_level(level="warning")
        self.assertEqual(con, 30, "Тест не выполнен")

        con = self.config.get_verbosity_level(level="info")
        self.assertEqual(con, 20, "Тест не выполнен")

        con = self.config.get_verbosity_level(level="debug")
        self.assertEqual(con, 10, "Тест не выполнен")

        con = self.config.get_verbosity_level(level="console")
        self.assertEqual(con, 10, "Тест не выполнен")

        con = self.config.get_verbosity_level(level=None)
        self.assertEqual(con, "critical, error, warning, info, debug", "Тест не выполнен")

    def test_init_env_config_path(self):
        if WINDOWS:
            con = self.config.init_env_config_path()
            self.assertTrue(con, "It is not WINDOWS")
        if not WINDOWS:
            con = self.config.init_env_config_path()
            self.assertTrue(con, "It is WINDOWS")


if __name__ == "__main__":
    unittest.main()