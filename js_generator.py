from random import choice


JS_ADD_EVENT = "document.addEventListener('{event}', action);"


def _function_inner_body(lines: list):
    return '    ' + '\n    '.join(lines)


EVENTS = [
    'click',
    'contextmenu',
    'copy',
    'dblclick',
    'drag',
    'paste'
]


ACTIONS = [
    {
        'prep': 'let prank_blur_amt = 0.0;',
        'func': _function_inner_body([
            'prank_blur_amt += .1;',
            'document.body.style.filter = `blur(${prank_blur_amt}px)`;'
        ])
    },
    {
        'prep': 'let prank_brightness_amt = 100;',
        'func': _function_inner_body([
            'prank_brightness_amt -= 1;',
            'document.body.style.filter = `brightness(${prank_brightness_amt}%)`;'
        ])
    },
    {
        'prep': 'let prank_brightness_amt = 100;',
        'func': _function_inner_body([
            'prank_brightness_amt += 1;',
            'document.body.style.filter = `brightness(${prank_brightness_amt}%)`;'
        ])
    },
    {
        'prep': 'let prank_contrast_amt = 100;',
        'func': _function_inner_body([
            'prank_contrast_amt -= 1;',
            'document.body.style.filter = `contrast(${prank_contrast_amt}%)`;'
        ])
    },
    {
        'prep': 'let prank_contrast_amt = 100;',
        'func': _function_inner_body([
            'prank_contrast_amt += 1;',
            'document.body.style.filter = `contrast(${prank_contrast_amt}%)`;'
        ])
    },
    {
        'prep': 'let prank_hue_amt = 0;',
        'func': _function_inner_body([
            'prank_hue_amt += 4;',
            'document.body.style.filter = `hue-rotate(${prank_hue_amt}deg)`;'
        ])
    }
]


def get_js():
    event  = choice(EVENTS)
    action = choice(ACTIONS)

    js = '\n'.join([
        action['prep'],
        f'function action() {"{"}\n{action["func"]}\n{"}"}',
        JS_ADD_EVENT.format(event=event)
    ])

    return js


if __name__ == '__main__':
    print(get_js())
