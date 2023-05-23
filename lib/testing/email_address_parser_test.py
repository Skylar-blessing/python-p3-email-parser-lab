from email_address_parser import EmailAddressParser

class TestEmailAddressParser:
    def test_instantiates_with_a_single_argument(self):
        '''instantiates with a single argument, a string.'''
        parser = EmailAddressParser("john@doe.com, person@somewhere.org")
        assert parser.email_addresses == "john@doe.com, person@somewhere.org"

    def test_contains_parse_method(self):
        '''contains a method called "parse".'''
        parser = EmailAddressParser("")
        assert callable(getattr(parser, "parse", None))

    def test_parses_emails_with_spaces(self):
        '''finds emails with spaces in between.'''
        parser = EmailAddressParser("john@doe.com person@somewhere.org")
        assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

    def test_parses_emails_with_commas(self):
        '''finds emails with commas in between.'''
        parser = EmailAddressParser("john@doe.com, person@somewhere.org")
        assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

    def test_parses_emails_with_commas_and_spaces(self):
        '''finds emails with commas and spaces in between.'''
        parser = EmailAddressParser("talk@talk.com, john.jones@flatironschool.com, alexa@amazon.com")
        assert parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"]