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
