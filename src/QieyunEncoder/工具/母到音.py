# -*- coding: utf-8 -*-

'''
將母轉換爲音。
'''

_音到母表 = [
    ['脣', '幫滂並明'],
    ['舌', '端透定泥知徹澄孃來'],
    ['齒', '精清從心邪莊初崇生俟章昌常書船日'],
    ['牙', '見溪羣疑'],
    ['喉', '影曉匣云以'],
]

_d母到音 = {母: 音 for 音, 母們 in _音到母表 for 母 in 母們}


def 母到音(母: str):
    '''
    將母轉換爲音。

    ```python
    >>> 母到音('並')
    '脣'
    >>> 母到音('羣')
    '牙'
    ```
    '''
    return _d母到音[母]
