"""Tests maze_game_controller."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import unittest
import numpy as np

import deepmind_lab
from python.tests.utils import maze_game_controller
from python.tests.utils import test_environment_decorator


class MazeGameControllerTest(unittest.TestCase):

  def setUp(self):
    self._env = test_environment_decorator.TestEnvironmentDecorator(
        deepmind_lab.Lab('tests/maze_navigation_test',
                         maze_game_controller.REQUIRED_OBSERVATIONS))
    self._controller = maze_game_controller.MazeGameController(self._env)
    self._env.reset()

  def testSpawnPosition(self):
    pos = self._controller.maze_position()
    self.assertTrue(np.array_equal(pos, [2, 3]))

  def testMoveToReachablePos(self):
    self.assertTrue(self._controller.move_to(2, 5))
    pos = self._controller.maze_position()
    self.assertTrue(np.array_equal(pos, [2, 5]))

  def testMoveToUnreachablePos(self):
    self.assertFalse(self._controller.move_to(20, 1))
    self.assertFalse(self._controller.move_to(3, 4))

  def testFailToGoTrhoughBlockedCorridor(self):
    self.assertFalse(self._controller.move_to(2, 5, blocked=[(1, 4)]))

  def testPickupLocations(self):
    self.assertTrue(np.array_equal(self._controller.pickup_location(0), [5, 1]))
    self.assertTrue(np.array_equal(self._controller.pickup_location(1), [6, 1]))
    self.assertTrue(np.array_equal(self._controller.pickup_location(2), [4, 3]))

  def testPathExists(self):
    path = self._controller.find_path(2, 5)
    self.assertItemsEqual(path, [(1, 3), (1, 4), (1, 5), (2, 5)])

  def testPathDoesNotExist(self):
    self.assertIsNone(self._controller.find_path(3, 4))

if __name__ == '__main__':
  if 'TEST_SRCDIR' in os.environ:
    deepmind_lab.set_runfiles_path(
        os.path.join(os.environ['TEST_SRCDIR'],
                     'org_deepmind_lab'))
  unittest.main()
