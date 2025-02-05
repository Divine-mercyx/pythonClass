import unittest
from tvSet.tv_set import *



class TestMyTvSet(unittest.TestCase):

    def test_that_tv_class_exists(self):
        myTv = TvSet()

    def test_that_tv_is_switched_off(self):
        myTv = TvSet()
        self.assertFalse(myTv.status())

    def test_that_tv_is_on_when_switched_on(self):
        myTv = TvSet()
        myTv.turn_on()
        self.assertTrue(myTv.status())

    def test_that_tv_is_off_when_turned_off_after_being_on(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.turn_off()
        self.assertFalse(myTv.status())

    def test_that_when_turn_on_volume_is_zero_when_first_turned_on(self):
        myTv = TvSet()
        myTv.turn_on()
        self.assertEqual(0, myTv.get_volume())

    def test_that_when_turn_off_you_cant_get_volume(self):
        myTv = TvSet()
        self.assertEqual(None, myTv.get_volume())
        myTv.turn_on()
        self.assertEqual(0, myTv.get_volume())

    def test_to_increase_volume(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        self.assertEqual(1, myTv.get_volume())
        myTv.increase_volume()
        myTv.increase_volume()
        self.assertEqual(3, myTv.get_volume())

    def test_that_increase_volume_doesnt_exceed_ten(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        self.assertEqual(10, myTv.get_volume())

    def test_to_increase_tv_volume_when_its_off(self):
        myTv = TvSet()
        myTv.increase_volume()
        myTv.turn_on()
        self.assertEqual(0, myTv.get_volume())

    def test_to_decrease_volume(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.decrease_volume()
        self.assertEqual(9, myTv.get_volume())

    def test_to_decrease_volume_while_being_off(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.turn_off()
        myTv.decrease_volume()
        myTv.turn_on()
        self.assertEqual(10, myTv.get_volume())

    def test_to_decrease_volume_lower_than_zero(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.decrease_volume()
        myTv.decrease_volume()
        myTv.decrease_volume()
        self.assertEqual(0, myTv.get_volume())

    def test_to_mute_tv(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.mute()
        self.assertEqual(0, myTv.get_volume())

    def test_to_increase_volume_then_mute_tv_then_unmute_tv_and_have_the_previous_volume_before_unmute(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.mute()
        self.assertEqual(0, myTv.get_volume())
        myTv.un_mute()
        self.assertEqual(2, myTv.get_volume())

    def test_that_tv_will_not_be_muted_and_unmuted_while_it_is_off(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.increase_volume()
        myTv.increase_volume()
        myTv.turn_off()
        myTv.mute()
        myTv.turn_on()
        self.assertEqual(2, myTv.get_volume())
        myTv.mute()
        myTv.turn_off()
        myTv.un_mute()
        myTv.turn_on()
        self.assertEqual(0, myTv.get_volume())

    def test_that_channel_can_be_changed_upward(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.change_up()
        myTv.change_up()
        self.assertEqual(3, myTv.get_channel())

    def test_that_channel_wont_change_when_its_off(self):
        myTv = TvSet()
        myTv.change_up()
        myTv.change_up()
        myTv.turn_on()
        self.assertEqual(1, myTv.get_channel())

    def test_that_channel_can_be_changed_downward(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.change_up()
        myTv.change_up()
        myTv.change_down()
        myTv.change_down()
        self.assertEqual(1, myTv.get_channel())

    def test_that_you_can_move_to_a_channel(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.search_channel(46)
        self.assertEqual(46, myTv.get_channel())

    def test_that_you_cant_move_to_invalid_channels(self):
        myTv = TvSet()
        myTv.turn_on()
        myTv.search_channel(56)
        self.assertEqual(1, myTv.get_channel())









if __name__ == '__main__':
    unittest.main()
