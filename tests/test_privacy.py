import unittest

from privacy import scrub_personal_data


class ReviewPrivacyTests(unittest.TestCase):
    def test_redacts_email_addresses(self):
        result = scrub_personal_data("Hubungi saya di person@example.com jika perlu")
        self.assertNotIn("person@example.com", result)
        self.assertIn("[REDACTED_EMAIL]", result)

    def test_redacts_indonesian_mobile_number_formats(self):
        for number in ("081234567890", "+6281234567890", "628123456789"):
            with self.subTest(number_format="Indonesian phone"):
                result = scrub_personal_data(f"Kontak: {number}")
                self.assertNotIn(number, result)
                self.assertIn("[REDACTED_PHONE]", result)

    def test_does_not_redact_regular_review_text_or_rating(self):
        text = "Rasa enak, pengiriman 2 hari, rating 5/5."
        self.assertEqual(scrub_personal_data(text), text)

    def test_scraper_data_redaction_is_idempotent(self):
        text = "Kontak 081234567890, email person@example.com"
        once = scrub_personal_data(text)
        self.assertEqual(scrub_personal_data(once), once)


if __name__ == "__main__":
    unittest.main()
