# This file is part of ADG: Anti-DDOS Guard.
#
# ADG: Anti-DDOS Guard is licensed under the GNU General Public License v3.0.
# See the LICENSE file for more details.
#
# Copyright (C) 2024 Armen-Jean Andreasian.
class BlackList(set):
    def __new__(cls, *args, **kwargs):
        forbidden_methods = (
            'remove', 'pop', 'clear', 'discard', 'update', 'difference_update',
            'intersection_update', 'symmetric_difference_update'
        )

        obj = super().__new__(cls)

        # disabling destructive methods, Raising TypeError 'NoneType' object is not callable
        for method in forbidden_methods:
            if hasattr(obj, method):
                setattr(obj, method, None)
        return obj
