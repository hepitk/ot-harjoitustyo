import unittest
from services.program_service import program_service


class TestProgramService(unittest.TestCase):
    def setUp(self):
        self.filename = "asiakirjapohjat/viranhaltijapäätös_määräalan_myynti_pohja"
        self.user_input_data = "Syötä kiinteistötunnus:"
        self.placeholder = "[kiinteistötunnus]"
        self.instruction = ""

    def test_create_replace_data_works(self):
        replace_data = program_service.create_replace_data(self.filename, self.user_input_data, self.placeholder, self.instruction)
        self.assertEqual(self.filename, replace_data.filename)
        self.assertEqual(self.user_input_data, replace_data.user_input_data)
        self.assertEqual(self.placeholder, replace_data.placeholder)
        self.assertEqual(self.instruction, replace_data.instruction)

