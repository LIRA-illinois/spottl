import unittest

import spottl
from spottl import twa


class TranslateTest(unittest.TestCase):
    def test_translate(self):
        spec: str = "F(a & b) & G(c & d)"
        aut: twa = spottl.translate(spec, "Buchi", "state-based", "complete")
        aut_hoa: str = aut.to_str("hoa")
        target: str = 'HOA: v1\nStates: 3\nStart: 1\nAP: 4 "a" "b" "c" "d"\nacc-name: Buchi\nAcceptance: 1 Inf(0)\nproperties: trans-labels explicit-labels state-acc complete\nproperties: deterministic stutter-invariant very-weak\n--BODY--\nState: 0 {0}\n[2&3] 0\n[!2 | !3] 2\nState: 1\n[0&1&2&3] 0\n[!0&2&3 | !1&2&3] 1\n[!2 | !3] 2\nState: 2\n[t] 2\n--END--'
        print(aut_hoa)
        self.assertEqual(aut_hoa, target)
