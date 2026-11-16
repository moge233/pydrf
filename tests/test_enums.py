#! python3


import unittest

from pydrf.textchart import (
    BreedIndicator,
    CourseCodes,
    HeaderIndex,
    RaceDataIndex,
    RecordType,
    RestrictionCodes,
    SexRestrictions,
    SurfaceCodes,
)

STRING_ENUMS = (
    RecordType,
    BreedIndicator,
    RestrictionCodes,
    SexRestrictions,
    SurfaceCodes,
    CourseCodes,
)


class StringEnumTestCase(unittest.TestCase):

    def test_equal_to_same_member(self) -> None:
        for enum_type in STRING_ENUMS:
            for member in enum_type:
                with self.subTest(member=member):
                    self.assertTrue(member == enum_type(member.value))

    def test_equal_to_code_string(self) -> None:
        for enum_type in STRING_ENUMS:
            for member in enum_type:
                with self.subTest(member=member):
                    self.assertTrue(member == member.value)
                    self.assertTrue(member.value == member)

    def test_not_equal_to_other_type(self) -> None:
        for enum_type in STRING_ENUMS:
            for member in enum_type:
                with self.subTest(member=member):
                    self.assertFalse(member == 1)

    def test_hashable_and_consistent_with_code_string(self) -> None:
        for enum_type in STRING_ENUMS:
            for member in enum_type:
                with self.subTest(member=member):
                    self.assertIn(member, {member})
                    self.assertEqual(hash(member), hash(member.value))

    def test_record_type_matches_record_code(self) -> None:
        self.assertTrue(RecordType.STARTER == 'S')
        self.assertFalse(RecordType.STARTER == 'R')
        self.assertIn('S', {RecordType.STARTER: 'starter'})


class IndexTestCase(unittest.TestCase):

    def test_equality(self) -> None:
        self.assertTrue(HeaderIndex.TRACK_CODE_INDEX == HeaderIndex.TRACK_CODE_INDEX)
        self.assertFalse(HeaderIndex.TRACK_CODE_INDEX == HeaderIndex.RACE_DATE_INDEX)
        self.assertFalse(HeaderIndex.TRACK_CODE_INDEX == 2)

    def test_ordering(self) -> None:
        low = HeaderIndex.COUNTRY_CODE_INDEX
        high = HeaderIndex.TRACK_CODE_INDEX
        self.assertTrue(high > low)
        self.assertTrue(low < high)
        self.assertTrue(high >= low)
        self.assertTrue(high >= high)
        self.assertTrue(low <= high)
        self.assertTrue(low <= low)
        self.assertFalse(low > high)
        self.assertFalse(high < low)
        self.assertFalse(low >= high)
        self.assertFalse(high <= low)

    def test_ordering_across_index_types_unsupported(self) -> None:
        for compare in (
            lambda: HeaderIndex.TRACK_CODE_INDEX > RaceDataIndex.RACE_NUMBER_INDEX,
            lambda: HeaderIndex.TRACK_CODE_INDEX < RaceDataIndex.RACE_NUMBER_INDEX,
            lambda: HeaderIndex.TRACK_CODE_INDEX >= RaceDataIndex.RACE_NUMBER_INDEX,
            lambda: HeaderIndex.TRACK_CODE_INDEX <= RaceDataIndex.RACE_NUMBER_INDEX,
        ):
            with self.assertRaises(TypeError):
                compare()

    def test_hashable(self) -> None:
        self.assertIn(HeaderIndex.TRACK_CODE_INDEX, {HeaderIndex.TRACK_CODE_INDEX})


if __name__ == '__main__':
    unittest.main()
