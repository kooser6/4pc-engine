import data.tests.threat_tests
import threat
import unittest

class TestThreatModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(threat.valid_key(12), False)
        self.assertEqual(threat.valid_key(10), False)
        self.assertEqual(threat.valid_key(19), False)
        self.assertEqual(threat.valid_key(18), False)
        self.assertEqual(threat.valid_key(16), False)
        self.assertEqual(threat.valid_key(threat.valid_keys[33]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[44]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[55]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[66]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[77]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[88]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[99]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[111]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[122]), True)
        self.assertEqual(threat.valid_key(threat.valid_keys[133]), True)
        self.assertEqual(threat.is_pawn_threat(228, 213, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(229, 212, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(229, 214, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(230, 213, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(230, 215, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(231, 214, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(231, 216, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(232, 215, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(232, 217, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(233, 216, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(233, 218, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(234, 217, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(234, 219, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(235, 218, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(82, 99, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(98, 83, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(98, 115, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(114, 99, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(114, 131, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(130, 115, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(130, 147, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(146, 131, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(146, 163, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(162, 147, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(162, 179, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(178, 163, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(178, 195, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(194, 179, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(52, 69, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(53, 68, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(53, 70, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(54, 69, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(54, 71, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(55, 70, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(55, 72, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(56, 71, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(56, 73, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(57, 72, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(57, 74, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(58, 73, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(58, 75, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(59, 74, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(93, 108, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(109, 92, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(109, 124, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(125, 108, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(125, 140, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(141, 124, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(141, 156, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(157, 140, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(157, 172, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(173, 156, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(173, 188, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(189, 172, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(189, 204, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(205, 188, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 228, threat.directions[0] + 213, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 229, threat.directions[0] + 212, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 229, threat.directions[0] + 214, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 230, threat.directions[0] + 213, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 230, threat.directions[0] + 215, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 231, threat.directions[0] + 214, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 231, threat.directions[0] + 216, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 232, threat.directions[0] + 215, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 232, threat.directions[0] + 217, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 233, threat.directions[0] + 216, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 233, threat.directions[0] + 218, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 234, threat.directions[0] + 217, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 234, threat.directions[0] + 219, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[0] + 235, threat.directions[0] + 235, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 82, threat.directions[3] + 99, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 98, threat.directions[3] + 83, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 98, threat.directions[3] + 115, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 114, threat.directions[3] + 99, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 114, threat.directions[3] + 131, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 130, threat.directions[3] + 115, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 130, threat.directions[3] + 147, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 146, threat.directions[3] + 131, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 146, threat.directions[3] + 163, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 162, threat.directions[3] + 147, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 162, threat.directions[3] + 179, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 178, threat.directions[3] + 163, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 178, threat.directions[3] + 195, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[3] + 194, threat.directions[3] + 179, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 52, threat.directions[1] + 69, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 53, threat.directions[1] + 68, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 53, threat.directions[1] + 70, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 54, threat.directions[1] + 69, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 54, threat.directions[1] + 71, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 55, threat.directions[1] + 70, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 55, threat.directions[1] + 72, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 56, threat.directions[1] + 71, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 56, threat.directions[1] + 73, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 57, threat.directions[1] + 72, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 57, threat.directions[1] + 74, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 58, threat.directions[1] + 73, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 58, threat.directions[1] + 75, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[1] + 59, threat.directions[1] + 74, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 93, threat.directions[2] + 108, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 109, threat.directions[2] + 92, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 109, threat.directions[2] + 124, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 125, threat.directions[2] + 108, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 125, threat.directions[2] + 140, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 141, threat.directions[2] + 124, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 141, threat.directions[2] + 156, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 157, threat.directions[2] + 140, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 157, threat.directions[2] + 172, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 173, threat.directions[2] + 156, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 173, threat.directions[2] + 188, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 189, threat.directions[2] + 172, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 189, threat.directions[2] + 204, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_pawn_threat(threat.directions[2] + 205, threat.directions[2] + 188, data.tests.threat_tests.board_xre), False)
        self.assertEqual(threat.is_knight_threat(245, 212, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(245, 214, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(250, 217, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(250, 219, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(97, 83, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(97, 115, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(177, 195, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(177, 163, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(37, 68, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(37, 70, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(42, 73, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(42, 75, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(110, 92, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(110, 124, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(190, 172, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(190, 204, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 245, threat.directions[0] + 212, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 245, threat.directions[0] + 214, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 250, threat.directions[0] + 217, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 250, threat.directions[0] + 219, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 97, threat.directions[0] + 83, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 97, threat.directions[0] + 115, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 177, threat.directions[0] + 195, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 177, threat.directions[0] + 163, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 37, threat.directions[0] + 68, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 37, threat.directions[0] + 70, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 42, threat.directions[0] + 73, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 42, threat.directions[0] + 75, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 110, threat.directions[0] + 92, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 110, threat.directions[0] + 124, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 190, threat.directions[0] + 172, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_knight_threat(threat.directions[0] + 190, threat.directions[0] + 204, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_bishop_threat(245, 228, data.tests.threat_tests.board_bfb), True)
        self.assertEqual(threat.is_bishop_threat(245, 194, data.tests.threat_tests.board_bfb), False)
        self.assertEqual(threat.is_bishop_threat(245, 140, data.tests.threat_tests.board_bfb), True)
        self.assertEqual(threat.is_bishop_threat(245, 125, data.tests.threat_tests.board_bfb), True)
        self.assertEqual(threat.is_bishop_threat(245, 110, data.tests.threat_tests.board_bfb), False)
        self.assertEqual(threat.is_rook_threat(199, 71, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 195, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 204, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 215, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 55, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 194, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 205, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 231, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_rook_threat(199, 39, data.tests.threat_tests.board_rfr), False)
        self.assertEqual(threat.is_rook_threat(199, 193, data.tests.threat_tests.board_rfr), False)
        self.assertEqual(threat.is_rook_threat(199, 206, data.tests.threat_tests.board_rfr), False)
        self.assertEqual(threat.is_rook_threat(199, 247, data.tests.threat_tests.board_rfr), False)
        self.assertEqual(threat.is_queen_threat(199, 71, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 195, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 204, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 215, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 55, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 194, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 205, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 231, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 39, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 193, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 206, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 247, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 131, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 114, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 124, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 109, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 216, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 233, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 214, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 229, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_queen_threat(199, 97, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 244, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 250, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(199, 94, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_queen_threat(198, 998, data.tests.threat_tests.board_qfq), False)
        self.assertEqual(threat.is_king_threat(87, 70, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 71, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 72, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 86, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 88, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 102, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 103, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 104, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_king_threat(87, 53, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 54, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 55, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 56, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 57, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 73, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 89, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_king_threat(87, 105, data.tests.threat_tests.board_txc), False)
        self.assertEqual(threat.is_threat(228, 213, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(229, 212, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(229, 214, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(230, 213, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(230, 215, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(231, 214, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(231, 216, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(232, 215, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(232, 217, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(233, 216, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(233, 218, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(234, 217, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(234, 219, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(235, 218, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(82, 99, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(98, 83, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(98, 115, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(114, 99, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(114, 131, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(130, 115, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(130, 147, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(146, 131, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(146, 163, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(162, 147, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(162, 179, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(178, 163, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(178, 195, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(194, 179, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(52, 69, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(53, 68, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(53, 70, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(54, 69, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(54, 71, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(55, 70, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(55, 72, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(56, 71, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(56, 73, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(57, 72, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(57, 74, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(58, 73, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(58, 75, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(59, 74, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(93, 108, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(109, 92, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(109, 124, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(125, 108, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(125, 140, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(141, 124, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(141, 156, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(157, 140, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(157, 172, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(173, 156, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(173, 188, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(189, 172, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(189, 204, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(205, 188, data.tests.threat_tests.board_xre), True)
        self.assertEqual(threat.is_threat(245, 212, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(245, 214, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(250, 217, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(250, 219, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(97, 83, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(97, 115, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(177, 195, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(177, 163, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(37, 68, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(37, 70, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(42, 73, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(42, 75, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(110, 92, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(110, 124, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(190, 172, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(190, 204, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(245, 228, data.tests.threat_tests.board_bfb), True)
        self.assertEqual(threat.is_threat(245, 140, data.tests.threat_tests.board_bfb), True)
        self.assertEqual(threat.is_threat(245, 125, data.tests.threat_tests.board_bfb), True)
        self.assertEqual(threat.is_threat(199, 71, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 195, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 204, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 215, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 55, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 194, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 205, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 231, data.tests.threat_tests.board_rfr), True)
        self.assertEqual(threat.is_threat(199, 71, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 195, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 204, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 215, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 55, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 194, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 205, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 231, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 131, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 114, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 124, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 109, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 216, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 233, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 214, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(199, 229, data.tests.threat_tests.board_qfq), True)
        self.assertEqual(threat.is_threat(87, 70, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 71, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 72, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 86, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 88, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 102, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 103, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(87, 104, data.tests.threat_tests.board_txc), True)
        self.assertEqual(threat.is_threat(16, 16, data.tests.threat_tests.board_txc), False)

class TestStateModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(state.is_draw(0, data.tests.state_tests.board_xre, 50, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_draw(0, data.tests.state_tests.board_xre, 49, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), False)
        self.assertEqual(state.is_draw(1, data.tests.state_tests.board_xre, 49, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), False)
        self.assertEqual(state.is_draw(2, data.tests.state_tests.board_xre, 49, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), False)
        self.assertEqual(state.is_draw(3, data.tests.state_tests.board_xre, 49, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), False)
        self.assertEqual(state.in_checkmate(3, data.tests.state_tests.noncheckmate_board_one, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-']), False)
        self.assertEqual(state.in_checkmate(0, data.tests.state_tests.nocheckmate, [[False, False], [False, False], [False, False], [False, False]], ['-', '-', '-', '-']), False)
        self.assertEqual(state.in_checkmate(0, data.tests.state_tests.checkmate, [[False, False], [False, False], [False, False], [False, False]], ['-', '-', '-', '-']), True)
        self.assertEqual(state.is_draw(0, data.tests.state_tests.board_xre, 49, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], [[0, data.tests.state_tests.board_xre], [0, data.tests.state_tests.board_xre], [0, data.tests.state_tests.nocheckmate], [0, data.tests.state_tests.nocheckmate]]), True)
        self.assertEqual(state.is_draw(0, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_draw(1, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_draw(2, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_draw(3, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.in_stalemate(0, data.tests.state_tests.stalemate, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-']), True)
        self.assertEqual(state.in_stalemate(1, data.tests.state_tests.stalemate, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-']), True)
        self.assertEqual(state.in_stalemate(2, data.tests.state_tests.stalemate, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-']), True)
        self.assertEqual(state.in_stalemate(3, data.tests.state_tests.stalemate, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-']), True)
        self.assertEqual(state.is_gameover(0, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_gameover(1, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_gameover(2, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_gameover(3, data.tests.state_tests.stalemate, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), True)
        self.assertEqual(state.is_gameover(3, data.tests.state_tests.noncheckmate_board_one, 33, [[True, True], [True, True], [True, True], [True, True]], ['-', '-', '-', '-'], []), False)
        self.assertEqual(state.is_gameover(0, data.tests.state_tests.nocheckmate, 33, [[False, False], [False, False], [False, False], [False, False]], ['-', '-', '-', '-'], []), False)
        self.assertEqual(state.is_gameover(0, data.tests.state_tests.checkmate, 33, [[False, False], [False, False], [False, False], [False, False]], ['-', '-', '-', '-'], []), True)

if __name__ == '__main__':
    unittest.main()