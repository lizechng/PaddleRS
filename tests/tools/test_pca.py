# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tempfile

from testing_utils import CpuCommonTest, run_script


class TestPCA(CpuCommonTest):
    def test_script(self):
        with tempfile.TemporaryDirectory() as td:
            run_script(
                f"python pca.py --im_path ../tests/data/ssst/multispectral.tif --save_dir {td} --dim 5",
                wd="../tools")