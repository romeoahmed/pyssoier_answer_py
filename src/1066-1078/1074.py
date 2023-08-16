"""
Copyright 2023 Romeo Ahmed <ahmedorqwn@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    :   1074.py
@Time    :   2023/08/16 16:42:46
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

n = int(input())
doors = [True for i in range(n)]

for i in range(2, n + 1):
    for j in range(n):
        if (j + 1) % i == 0:
            doors[j] = not doors[j]

opened_doors = []
for index, value in enumerate(doors):
    if value:
        opened_doors.append(str(index + 1))

print(*opened_doors, sep=" ")
