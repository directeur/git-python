# test_diff.py
# Copyright (C) 2008 Michael Trier (mtrier@gmail.com) and contributors
#
# This module is part of GitPython and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

from test.testlib import *
from git import *

class TestDiff(object):
    def setup(self):
        self.repo = Repo(GIT_REPO)
    
    def test_list_from_string_new_mode(self):
        output = fixture('diff_new_mode')
        diffs = Diff.list_from_string(self.repo, output)
        assert_equal(1, len(diffs))
        assert_equal(10, len(diffs[0].diff.splitlines()))
